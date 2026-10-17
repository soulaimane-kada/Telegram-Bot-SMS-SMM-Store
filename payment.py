import http.client
import json


# CREATE COINBASE INVOICE
async def Crypto_coinbase_invoice(full_user, the_amount, credits):
    conn = http.client.HTTPSConnection("api.commerce.coinbase.com")
    payload = json.dumps({
          "name": f"USER ID : {full_user.id}",
          "description": f"This invoice is for '{full_user.first_name}', User id : {full_user.id}, Amount : {float(the_amount)} USD, In credits : {float(credits)}",
          "local_price": {
            "amount": float(the_amount),
            "currency": "USD"
          },
          "pricing_type": "fixed_price",
          "requested_info": []
        })
    headers = {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'X-CC-Version': '2018-03-22',
          'X-CC-Api-Key': '5c39c5aa-f42a-4cd6-9063-408a98caae89'
        }
    conn.request("POST", "/checkouts", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
        
    payment_url = f"https://commerce.coinbase.com/checkout/{data.get('data').get('id')}"
    return [payment_url, data.get('data').get('id')]


# CANCEL COINBASE INVOICE
async def Cancel_Crypto_coinbase_invoice(checkout_id):
    conn = http.client.HTTPSConnection("api.commerce.coinbase.com")
    payload = ''
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'X-CC-Version': '2018-03-22',
      'X-CC-Api-Key': '5c39c5aa-f42a-4cd6-9063-408a98caae89'
    }
    conn.request("DELETE", f"/checkouts/{checkout_id}", payload, headers)


# CHECK COINBASE PAYMENT STATUS
async def check_coinbase_payment_status(charge_id):
    conn = http.client.HTTPSConnection("api.commerce.coinbase.com")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-CC-Version': '2018-03-22',
        'X-CC-Api-Key': '5c39c5aa-f42a-4cd6-9063-408a98caae89'
    }
    conn.request("GET", f"/charges/{charge_id}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)

    payment_status = data.get('data').get('timeline')[0].get('status')
    return payment_status

