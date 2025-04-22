import requests
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("AIRTABLE_TOKEN")
base_id = os.getenv("AIRTABLE_BASE_ID")
table_id = os.getenv("AIRTABLE_TABLE_ID")

url = f"https://api.airtable.com/v0/{base_id}/{table_id}"
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)
print(response.json())