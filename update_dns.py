import requests
import os
from dotenv import load_dotenv

# Loading environment variables from the .env file
load_dotenv()

# Function that finds new public IP and assigned it to public_ip.
def get_public_ip():
    response = requests.get('https://api.ipify.org').text
    return response

public_ip = get_public_ip()
print(f'Public IP: {public_ip}')

# Function that gets the DNS record ID from cloudflare api.
def get_dns_record_id(api_key, zone_id, record_name):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?type=A&name={record_name}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    if data["success"]:
        for record in data["result"]:
            if record["name"] == record_name:
                return record["id"]
    raise Exception(f"DNS record {record_name} not found.")

# Function to update the dns record with the new public ip.
def update_dns_record(api_key, zone_id, record_id, record_name, new_ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "type": "A",
        "name": record_name,
        "content": new_ip,
        "ttl": 120,
        "proxied": False
    }
    response = requests.put(url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    if data["success"]:
        print(f"Successfully updated DNS record: {record_name} to IP: {new_ip}")
    else:
        raise Exception(f"Failed to update DNS record: {data['errors']}")

if __name__ == "__main__":
    api_key = os.getenv('API_KEY')
    zone_id = os.getenv('ZONE_ID')
    record_name = os.getenv('RECORD_NAME') # The DNS record that will be updated
    new_ip = public_ip # The new IP address

try:
    record_id = get_dns_record_id(api_key, zone_id, record_name)
    update_dns_record(api_key, zone_id, record_id, record_name, new_ip)
except Exception as e:
    print(f"An error occured: {e}")
