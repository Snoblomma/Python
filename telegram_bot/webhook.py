from pprint import pprint
import requests

bot_token = '393173429:AAFjTTKp9c3SqCxe2ynIed8rI4e6GIohpQ0'
test_url = "https://fd654599.ngrok.io/{}".format(bot_token)

def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

r = requests.get(get_url("setWebhook"), data={"url": test_url})
r = requests.get(get_url("getWebhookInfo"))
pprint(r.status_code)
pprint(r.json())