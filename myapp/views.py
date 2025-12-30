import json
import uuid
import requests
from django.shortcuts import redirect, render
from django.http import HttpResponse


def home(request):
    id = uuid.uuid4()
    return render(request, 'myapp/index.html', {'uuid': id})


def initkhalti(request):
    url = "https://a.khalti.com/api/v2/epayment/initiate/"

    return_url = "http://127.0.0.1:8000/verify/"
    amount = int(request.POST.get('amount')) * 100  # MUST be paisa
    purchase_order_id = request.POST.get('purchase_order_id')

    payload = {
        "return_url": return_url,
        "website_url": "http://127.0.0.1:8000/",
        "amount": amount,
        "purchase_order_id": purchase_order_id,
        "purchase_order_name": "test",
    }

    headers = {
        'Authorization': 'Key b885cd9d8dc04eebb59e6f12190aoo90',
        'Content-Type': 'application/json',
    }

    response = requests.post(url, json=payload, headers=headers)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    new_res = response.json()

    if "pidx" in new_res:
        return redirect(f"https://pay.khalti.com/?pidx={new_res['pidx']}")

    return HttpResponse(new_res)


def verifyKhalti(request):
    return redirect('home')
