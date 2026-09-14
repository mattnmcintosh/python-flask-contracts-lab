#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/int:id')
def contractor_info(id):
    has_contractor = any(contract.get("id") == id for contract in contracts)
    if has_contractor:
        information = next(contract["contract_information"] for contract in contracts if contract["id"] == id)
        return make_response(information, 200, {})
    else:
        information = "Contract not found"
        return make_response(information, 404, {})

@app.route('/customer/string:customer_name')
def customer_info(customer_name):
    has_customer = any(customer == customer_name for customer in customers)
    if has_customer:
        information = ""
        return make_response(information, 204, {})
    else:
        information = f"{customer_name} was not found in the existing customers"
        return make_response(information, 404, {})

if __name__ == 'main':
    app.run(port=5555, debug=True)