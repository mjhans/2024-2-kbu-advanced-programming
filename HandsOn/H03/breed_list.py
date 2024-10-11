import requests

base_endpoint = "https://dog.ceo/api"
all_breeds_endpoint = f"{base_endpoint}/breeds/list/all"
done_status_code = (200, 201, 204, 301, 302)

response = requests.get(all_breeds_endpoint)
# print(response)


def http_get_response(resp):
    return_value = {}
    if resp.status_code in done_status_code:
        return_value = resp.json()
    else:
        return_value = {}
    return return_value
    

try:
    dict_response = http_get_response(requests.get(all_breeds_endpoint))
    breed_list = dict_response.get('message',{}).keys()
    
    for breed_name in dict_response.get('message',{}).keys():
        print(breed_name)
        image_url = f"{base_endpoint}/breed/{breed_name}/images"
        print(image_url)
        response = requests.get(image_url)
        
        if response.status_code in done_status_code:
            print(response)
            dict_response = response.json()
            print(dict_response.get('message',[]))
        # for breed in dict_response.get('message',{}).keys():
        #     #print(breed)
        #     breed_list.append(breed)
except Exception as e:
    print(f"Error: {e}") 