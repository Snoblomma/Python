
def process_message(update):
    data = {}
    data["chat_id"] = update["message"]["from"]["id"]
    data["text"] = "I can hear you!"
    r = requests.post(get_url("sendMessage"), data=data)