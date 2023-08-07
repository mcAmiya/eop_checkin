import requests
from push import Pushplus
import app_config

pushplus = Pushplus(key=app_config.pushplus_key)

url = app_config.EOP_checkin_url

payload = {}

headers = {
    'Cookie': app_config.EOP_cookie,
}

response = requests.request("POST", url, headers=headers, data=payload)

res = app_config.check_fail + response.text
if response.text == 'success':
    res = app_config.check_success
elif response.text == 'already':
    res = app_config.check_already
print(res)
pushplus.send(res, title=app_config.pushplus_title)

