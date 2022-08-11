# poll.py | M.Z-2022

import requests
import json

class poll():
    def apipoll():
        rqst=requests.get("https://akabab.github.io/superhero-api/api/all.json")
        if rqst.status_code == 200:
            temp=rqst.json()
            with open("API/temprqst.json", 'w') as f:
                json.dump(temp, f)

            # Debug   
            print("Succesfully Dumped API! ")
