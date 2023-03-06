from behave import *
import requests
from payLoad import *
import configparser
from utilities.configurations import *
from utilities.resources import *


@given('book details needs to be added')
def step_impl(context):
    context.urladd = getConfig()['API']['endpoint'] + APIresources.AddBook
    context.headers = {"Content-Type": "application/json"}


@when('we execute the add book')
def step_impl(context, isbn, aisle):
    context.add_response = requests.post(context.urladd, json=addPL(isbn, aisle), headers=context.headers, )
    print(context.add_response.json())
    context.final_res = context.add_response.json()


@then('book is successfully added')
def step_impl(context):
    # res_json = context.add_response.json()

    print(context.add_response.json())
    print(context.add_response.status_code)
    res_json = context.add_response.json()
    context.bookID = res_json['ID']
    print(context.bookID)
    assert res_json["Msg"] == "successfully added"


@when('we execute the add book with {isbn} and {aisle} number')
def step_impl(context, isbn, aisle):
    context.add_response = requests.post(context.urladd, json=addPL(isbn, aisle), headers=context.headers, )
    print(context.add_response.json())
    context.final_res = context.add_response.json()






