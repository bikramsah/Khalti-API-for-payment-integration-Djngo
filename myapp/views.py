import json
from django.shortcuts import redirect, render
import uuid
import requests
# Create your views here.
def home(request):
    id = uuid.uuid4()
    print(id)
    return render(request,'myapp/index.html',{'uuid':id})

def initkhalti(request):
    url = "https://a.khalti.com/api/v2/epayment/initiate/"
    return_url = request.POST.get('return_url')
    website_url = request.POST.get('return_url')
    amount = request.POST.get('amount')
    purchase_order_id = request.POST.get('purchase_order_id')


    print("url",url)
    print("return_url",return_url)
    print("web_url",website_url)
    print("amount",amount)
    print("purchase_order_id",purchase_order_id)
    payload = json.dumps({
        "return_url": return_url,
        "website_url": website_url,
        "amount": amount,
        "purchase_order_id": purchase_order_id,
        "purchase_order_name": "test",
        "customer_info": {
        "name": "Bibek Dahal",
        "email": "test@khalti.com",
        "phone": "9800000001"
        }
    })

    # put your own live secet for admin
    headers = {
        'Authorization': 'key b885cd9d8dc04eebb59e6f12190aoo90',
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(json.loads(response.text))

    print(response.text)
    new_res = json.loads(response.text)
    # print(new_res['payment_url'])
    print(type(new_res))
    return redirect(new_res['payment_url'])
    return redirect("home")

def verifyKhalti(request):
    url = "https://a.khalti.com/api/v2/epayment/lookup/"
    if request.method == 'GET':
        headers = {
            'Authorization': 'key b885cd9d8dc04eebb59e6f12190ae017',
            'Content-Type': 'application/json',
        }
        pidx = request.GET.get('pidx')
        data = json.dumps({
            'pidx':pidx
        })
        res = requests.request('POST',url,headers=headers,data=data)
        print(res)
        print(res.text)

        new_res = json.loads(res.text)
        print(new_res)
        

        if new_res['status'] == 'Completed':
            # user = request.user
            # user.has_verified_dairy = True
            # user.save()
            # perform your db interaction logic
            pass
        
        # else:
        #     # give user a proper error message
        #     raise BadRequest("sorry ")

        return redirect('home')
    

        