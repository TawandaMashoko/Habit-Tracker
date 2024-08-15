import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "tawanda"
TOKEN = "2ehj2k3j22ed"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "graph1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response_1 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response_1.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8.20",
}

#response3 = requests.post(url=pixel_creation_endpoint,json=pixel_data, headers=headers)
#print(response3.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "2"
}
#response_4 = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response_4.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response_5 = requests.delete(url=delete_endpoint, headers=headers)
print(response_5.text)