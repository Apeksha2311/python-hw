import requests
import json


URL = 'http://127.0.0.1:8000/studentapi/'

#get requests (read data)
'''
def GetData(id=None):
    d={}
    if id is not None:
        d = {'id':id}

    json_data = json.dumps(d)
    r = requests.get(url =URL , data = json_data)
    return r.json()

get_data=GetData(1)
print(get_data)



#2 -post request
def PostData():
    d = {
        'name':'Virat',
        'roll':123,
        'course':'Django'
        }
    json_data = json.dumps(d)

    r = requests.post(url =URL,data = json_data)
    return r.json()

post_data = PostData()
print(post_data)

#3 put request(update data)

def UpdateData():
    d={
        'id':2,
        'name':'Anushka',
        'course':'CSS'
        }

    json_data = json.dumps(d)

    r = requests.put(url=URL ,data = json_data)

    return r.json()

update_data = UpdateData()
print(update_data)
'''

#delete request
def DeleteData():
    d={
        'id':1
        }
    json_data=json.dumps(d)

    r = requests.delete(url=URL ,data = json_data)

    return r.json()
deleted_data=DeleteData()
print(deleted_data)










