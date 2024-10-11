import requests

base_endpoint = "https://dog.ceo/api"
all_breeds_endpoint = f"{base_endpoint}/breeds/list/all"
done_status_code = (200, 201, 204, 301, 302)
breed_all_images_dict = {}
response = requests.get(all_breeds_endpoint)
# print(response)

def http_get_response(resp):
    # return_value = {}
    # if resp.status_code in done_status_code:
    #     return_value = resp.json()
    # else:
    #     return_value = {}
    # return return_value
    
    #return  resp.json() if (resp.status_code in done_status_code) else None
    
    try:
        if resp.status_code not in done_status_code:
            raise Exception(f"Error: {resp.status_code}")
             
        response_dict = resp.json()
        if response_dict is None:
            raise Exception("Error: response_dict is None")
            
        if response_dict.get("status", "failed"):
            raise Exception(f"Error: {response_dict.get('message', 'failed')}")

    except Exception as e:
        raise Exception(f"Error: {e}")
    

try:
    dict_response = http_get_response(requests.get(all_breeds_endpoint))
    breed_list = dict_response.get('message',{}).keys()
    
    for breed_name in breed_list:
        image_url = f"{base_endpoint}/breed/{breed_name}/images"
        dict_response = http_get_response(requests.get(image_url))
        breed_all_images_dict[breed_name] = dict_response.get('message',[])
    
    for breed_name, breed_image_urls in breed_all_images_dict.items():
        for breed_image_url in breed_image_urls:
            print(f"{breed_name = }, {breed_image_url = }")
except Exception as e:
    print(f"Error: {e}") 