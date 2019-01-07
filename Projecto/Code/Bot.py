import requests
import json
import time
import sys

def main(argv):
    if len(argv) < 3:
        print("Usage: <bot_id> <message_period> <message>")
        return
    if int(argv[1]) < 0:
        print("Period must be higher than 0")
        return
    message = ' '.join(argv[2:])
    payload = {'ID': argv[0] , 'Message': message}

    while True:
        r = requests.post("http://127.0.0.1:5000/API/Bots/SendMessages", json=payload)
        data = r.json()
        json_acceptable_string = data.replace("'", "\"")
        msg = json.loads(json_acceptable_string)
        if not(str(msg["Status"]) == "OK"):
            print("Authentication Failed")
            return

        time.sleep(int(argv[1]))

if __name__ == '__main__':
    main(sys.argv[1:])
