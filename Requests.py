import requests


# # Send a GET request
# response = requests.get("https://jsonplaceholder.typicode.com/posts")

# # Inspect the response
# print("Status Code:", response.status_code)  # 200 means success
# print("Response Body:", response.text)      # Response content as a string
# print("JSON Data:", response.json())        # Parse JSON directly (if applicable)

# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": "foo",
#     "body": "bar",
#     "userId": 1
# }

# response = requests.post(url, json=data)  # Use `json` for JSON data
# print("Status Code:", response.status_code)
# print("Response JSON:", response.json())

url = "https://api.github.com/search/repositories"
headers = {"User-Agent": "my-app"}
params = {"q": "requests+language:python"}

response = requests.get(url, headers=headers, params=params)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
