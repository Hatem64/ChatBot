from flask import Flask , request
import json
import os,sys
from pprint import pprint
from pymessenger import Bot

from w import generate_user_response

VERIFICATION_TOKEN = "hello"
PAGE_ACCESS_TOKEN =  "EAAHNcnwIXFsBAKPxQr5aZBWuWK3wWWS8J3gE4nlozJ7pWBaddLwIB7N06fierxs6QbJQfkP15DPZAyzUZA4MSJYBi4XPPJuxqQcrl1D7bA7RvBXtJafq9v7r5OK1iliFBt6r43yjT5989JfYgrx9ujgpCW7bZAsTZAfozSeb8c3BzSIPJzGBD"
app = Flask(__name__)

bot = Bot(PAGE_ACCESS_TOKEN)



@app.route('/', methods =['GET'])
def verify() :
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN:
            return "Verification token mismatch" , 403
        return request.args["hub.challenge"] , 200
    return "Hello-world" , 200



@app.route('/', methods=['POST'])
def webhook():

    data = request.get_json()
    printmsg(data)
    process_data(data)
    return "okk",200



def process_data(data):
    if data["object"]=="page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                sender_id = messaging_event["sender"]["id"]
                recipient_id = messaging_event["recipient"]["id"]
                if messaging_event.get("message"):
                    if "text" in messaging_event["message"]:
                        messaging_text = messaging_event["message"]["text"]
                    else:
                        messaging_text = "no text"
                    response = generate_user_response(messaging_text)
                    bot.send_text_message(sender_id, response)




def printmsg(msg):
    pprint(msg)

    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug=True, port=80)

