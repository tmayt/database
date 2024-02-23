import requests

def get_data(user,key):
    url = f"https://database.tmayt.ir/get-data?user={user}&key={key}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def set_data(key,value,user):
    url = "https://database.tmayt.ir/set-data"

    payload = {'key': key,
    'value': value,
    'user': user}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.json()

# set_data(user="test",key="myvar",value="12345678")

print(get_data(user="test",key='myvar'))