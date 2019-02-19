import requests
import json
import os

ENDPOINT = "http://127.0.0.1:8000/api/status/"
ENDPOINT_ = "http://127.0.0.1:8000/api/status/41"
Auth_ENDPOINT = "http://127.0.0.1:8000/api/token/auth/"
refresh_ENDPOINT = Auth_ENDPOINT + 'refresh'
# http://127.0.0.1:8000/api/token/auth/refresh

image_path = os.path.join(os.getcwd(), "dog.jpg")


def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


# do(method='post', data={'content': "new text from the test script", 'user': 2})

# do(method='put', data={
#    'id': 22, 'content': "edit the 22 from the test script", 'user': 2})

# do(method='delete', data={'id': 26})

#############################################################################

def do_img(method='post', data={}, is_json=True, img_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    if img_path is not None:
        with open(image_path, 'rb') as image:
            file_data = {
                'image': image
            }
            r = requests.request(method, ENDPOINT, data=data,
                                 headers=headers, files=file_data)
    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


# do_img(method='post', data={'user': 2, "content": ""}, is_json=False,
#        img_path=image_path)

# do_img(method='put', data={'id': 27, 'user': 2,
#                            "content": ""}, is_json=False, img_path=image_path)

#############################################################################

get_endpoint = ENDPOINT + str(41)
post_data = json.dumps({"content": "test from script"})

# r = requests.get(get_endpoint)
# print(r.text)

# r2 = requests.get(ENDPOINT_)
# print(r2.status_code)

post_headers = {
    'content-type': 'application/json'
}

# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response.text)


#############################################################################

data = {
    "username": "ahmed",
    "password": "qwer1234",
}

# r = requests.post(Auth_ENDPOINT, data=data)
# print(r.json())

headers = {
    "Content-Type": "application/json"
}

r_refresh = requests.post(
    refresh_ENDPOINT, data=json.dumps(data), headers=headers)
print(r_refresh.json())
