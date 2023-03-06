import requests
from payLoad import *
import configparser
from utilities.configurations import *
from utilities.resources import *

# urladd = getConfig()['API']['endpoint'] + APIresources.AddBook
# urldel = getConfig()['API']['endpoint'] + APIresources.DeleteBook
# headers = {"Content-Type": "application/json"}
# for i in range(1, 3):
#
#     add_response = requests.post(urladd, json=addPL(i),
#                                  headers=headers, )
#
#     print(add_response.json())
#     final_res = add_response.json()
#     print(add_response.status_code)
#     bookID = final_res['ID']
#     print(bookID)
#
#     #delet the added entry
#
#     del_response = requests.post(urldel, json={"ID": bookID}, headers=headers,)
#     print(del_response.status_code)
#     print(del_response.json())


#auth basics

urlgit = "https://api.github.com/user"
gitres = requests.get(urlgit, auth=('ankeetah', getPassword()))
print(gitres.status_code)
print(gitres.json())

#session manager

sessionManager = requests.session()
sessionManager.auth = auth=('ankeetah', getPassword())

urlrepo = "https://api.github.com/user/repos"
repo_response = sessionManager.get(urlrepo)
print(repo_response)
print(repo_response.status_code)

