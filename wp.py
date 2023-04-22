import json
import requests
import time

# Whatsapp API endpoint
url = 'http://Whatsapp-Api-URL'

# Add your api key
auth_key = 'Bearer $2b$10$NTCAqVeMGRyuEPxOecyxVOo8La1iSLvwtcK7D4CnE1g4NSKDpAMLu'

# Message file
message_file = 'mesaj.txt'

# Phone list
phones_file = 'telefonlar.txt'

# Read the msgs from file
with open(message_file, 'r') as f:
    message = f.read()

# Read the numbers from file
with open(phones_file, 'r') as f:
    phones = [line.strip() for line in f.readlines()]

# Api request for each number
for phone in phones:
    payload = {
        'phone': phone,
        'message': message,
        'isGroup': False
    }

    # Sending request
    response = requests.post(url, headers={
        'Authorization': auth_key,
        'Content-Type': 'application/json',
        'Accept': '*/*'
    }, data=json.dumps(payload))

    # If unsuccess, provide error response
    if response.status_code != 200:
        print(f'Hata kodu: {response.status_code} - Hata mesajı: {response.text}')
    else:
        print(f'{phone} numarasına mesaj gönderildi.')

    # wait 10 secs between each msg
    time.sleep(10)
