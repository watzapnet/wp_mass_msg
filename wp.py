# -*- coding: utf-8 -*-

import json
import requests
import time
from datetime import timedelta

# Whatsapp API endpoint
url = 'http://WP-API-URL'

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

# Start time
start_time = time.monotonic()

# Success count
success_count = 0

# Failure count
failure_count = 0

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
        failure_count += 1
    else:
        print(f'{phone} numarasına mesaj gönderildi.')
        success_count += 1

    # wait 10 secs between each msg
    time.sleep(10)

# End time
end_time = time.monotonic()

# Elapsed time
elapsed_time = end_time - start_time

# Total count
total_count = success_count + failure_count

# Create HTML output
html_output = f"""
<html>
    <body>
        <h2>Whatsapp Mesaj Gönderme Raporu</h2>
        <p>Toplam gönderilen mesaj sayısı: {total_count}</p>
        <p>Toplam başarılı mesaj sayısı: {success_count}</p>
        <p>Toplam başarısız mesaj sayısı: {failure_count}</p>
        <p>Toplam geçen süre: {str(timedelta(seconds=elapsed_time))}</p>
        <p>Mesaj gönderimi tamamlandı.</p>
    </body>
</html>
"""

# Save HTML output to file
with open('output.html', 'w') as f:
    f.write(html_output)

print("Rapor başarıyla oluşturuldu ve 'output.html' dosyasına kaydedildi.")
