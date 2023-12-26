import requests

url = 'https://api.chatkore.com/v1/images/generations'
headers = {
    'Content-Type': 'application/json',
    # 转发秘钥
    'Authorization': 'Bearer sk-xxxx'
}
data = {
    "model": "dall-e-3",
    "prompt": "A cute baby sea otter",
    "n": 1,
    "size": "1024x1024"
}

response = requests.post(url, headers=headers, json=data)

print(response.json())