import requests

base_endpoint = "https://dog.ceo/api"
all_breeds_endpoint = f"{base_endpoint}/breeds/list/all"
done_status_code = (200, 201, 204, 301, 302)

response = requests.get(all_breeds_endpoint)
# print(response)

try:
    dict_response = response.json()
    if response.status_code in done_status_code:
        for breed in dict_response.get('message',{}).keys():
            print(breed)
except Exception as e:
    print(f"Error: {e}") 