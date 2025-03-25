import requests

response_post = requests.post("http://localhost:8000/ips/", json={"ambiguous_ip": "1903476"})
print("POST Response:", response_post.json())

response_get = requests.get("http://localhost:8000/ips/")
print("GET Response:", response_get.json())