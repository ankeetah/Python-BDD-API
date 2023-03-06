import requests
from utilities.configurations import *
from utilities.resources import *

urldel = getConfig()['API']['endpoint'] + APIresources.DeleteBook
headers = {"Content-Type": "application/json"}


def after_scenario(context, scenario):
    del_response = requests.post(urldel, json={"ID": context.bookID}, headers=headers,)
    print(del_response.status_code)
    print(del_response.json())
    assert del_response.status_code == 200
    res_json = del_response.json()
    print(res_json["msg"])
