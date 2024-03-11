import requests


# baseURL = 'https://jsonplaceholder.typicode.com/'
# -------------------------------- GET Request ------------------------------- #
# response = requests.get(f'{baseURL}/posts')
# data = response.json()
# print( len(data) )
# print(data[0])

# ------------------------------- POST Request ------------------------------- #
# post_data = {
#     'userId': 1,
#     'title': 'title2',
#     'body': 'post2'
# }

# response = requests.post(f'{baseURL}/posts', json=post_data)
# new_post_id = response.json()
# print(new_post_id)


# -------------------------------- PUT Request ------------------------------- #
# updated_post_data = {
#     "userId": 1,
#     "title": "title2",
#     "body": "post2 post2 post2post2"
# }

# response = requests.put(f'{baseURL}/posts/1', json=updated_post_data)
# data = response.json()
# print(data)

# -------------------------------- PATCH Request ------------------------------- #
# updated_post_data = {
#     "body": "post2 post2 post2post2"
# }

# response = requests.patch(f'{baseURL}/posts/1', json=updated_post_data)
# data = response.json()
# print(data)

# ------------------------------ Delete Request ------------------------------ #
# # Sending a DELETE request
# response = requests.delete(f'{baseURL}/posts/1')

# print(response.json())

# # Checking if the deletion was successful
# if response.status_code == 200:
#     print("The post was successfully deleted.")
# else:
#     print(f"Failed to delete the post. Status code: {response.status_code}")


# ------------------------------ Response Object ----------------------------- #
# response = requests.get(f'{baseURL}/posts')

# # print(f'response.headers = {response.headers}')
# print(f'response.headers.Pragma = {response.headers['Pragma']}')

# print(f'response.ok = {response.ok}')
# print(f'response.status_code = {response.status_code}')
# print(f'response.request.headers = {response.request.headers}')
# # print(f'response.text = {response.text}')

# ---------------------------- Handling Exceptions --------------------------- #
# try:
#     # response = requests.get(f'{baseURL}/post')
#     response = requests.get('https://api.example.com/resource')
#     response.raise_for_status() # will raise an HTTPError if the status is 4xx or 5xx
# except requests.exceptions.HTTPError as errh:
#     print ("Http Error:",errh)
# except requests.exceptions.ConnectionError as errc:
#     print ("Error Connecting:",errc)
# except requests.exceptions.Timeout as errt:
#     print ("Timeout Error:",errt)
# except requests.exceptions.RequestException as err:
#     print ("OOps: Something Went Wrong!",err)
# finally:
#     print(f'response.status_code = {response.status_code}')


# ----------------------------- Send Query Params ---------------------------- #
# https://jsonplaceholder.typicode.com/posts?userId=1


# # Define the base URL
# url = 'https://jsonplaceholder.typicode.com/posts'

# # Define the query parameters
# query_params = {
#     'userId': 1,
#     '_limit': 5
# }

# # # Send a GET request with query parameters
# # # response = requests.get(url, params=query_params)
# response = requests.get(url, params=query_params)
# # response = requests.request('get', url, params=query_params)
# posts = response.json()

# # Print the retrieved posts
# for post in posts:
#     print(post)


# ------------------------------- Send Headers ------------------------------- #
# headers = {
#     'User-Agent': 'My Client',
# }
# response = requests.get(f'{baseURL}/posts', headers=headers)
# print(f'response.request.headers = {response.request.headers}')


# --------------------------------- Examples --------------------------------- #
# baseURL = 'https://v2.jokeapi.dev/joke/Programming'

# try:
#     r = requests.get(baseURL)
#     r.raise_for_status()
#     if r.ok:
#         joke = r.json()
#         print(joke['setup'])
#         print(joke['delivery'])
#     else:
#         print(f'response status: {r.status_code}')
# except requests.exceptions.RequestException as err:
#     print ("OOps: Something Went Wrong!",err)





