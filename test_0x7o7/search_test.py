# -*- coding: utf-8 -*-
import requests

headers = {
    'accept': 'application/json',
}

params = {
    'sortDirection': 'asc',
    'create_time': '["2023-08-13 08:29:16","2023-08-24 08:29:17"]',
    'currentPage': '0',
    'sortBy': 'create_time',
    'eachPage': '3',
}

response = requests.get('http://127.0.0.1:8000/test/v1', params=params, headers=headers)
print(response.content.decode('utf-8'))