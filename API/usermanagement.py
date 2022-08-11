# usermanagement.py | M.Z-2022

import pyrebase
import hashlib
import json

class usermanagement():

    def __init__(self):
        self.firebaseConfig = {
            "apiKey": "AIzaSyAfNGIj7JGdK3NZ22i496pkAvQrmvffVyA",
            "authDomain": "ia2-digitalsoltuions.firebaseapp.com",
            "databaseURL": "https://ia2-digitalsoltuions-default-rtdb.firebaseio.com/",
            "projectId": "ia2-digitalsoltuions",
            "storageBucket": "ia2-digitalsoltuions.appspot.com",
            "messagingSenderId": "1059336754959",
            "appId": "1:1059336754959:web:b9aa02ea8761cea2a0907a",
            "measurementId": "G-MBS44P89K1"  
        };

        self.firebase=pyrebase.initialize_app(self.firebaseConfig)
        self.auth=self.firebase.auth()
        self.db=self.firebase.database()

    def firebase_login(self, email_address, unhashed_password):
        print("Logging In...")
        try:
            hashed_password=str(hashlib.md5(unhashed_password).encode()).hexdigest()
            firebase_login=self.auth.sign_in_with_email_and_password(email_address, hashed_password)
            # Debug
            print("Successfully Logged In! ")

            uuid_ident=self.auth.get_account_info(firebase_login['idToken'])
            # print(uuid_ident)

            self.token=firebase_login['idToken']
            self.uuid=uuid_ident["users"][0]["localId"]
            # print(self.uuid, self.token)

            # Output Identity to JSON | identity.json
            identity = {
                "uuid" : self.uuid,
                "token" : self.token
            }
            jobject=json.dumps(identity, ident=4)
            with open("API/identity.json", "w") as outfile:
                outfile.write(jobject)
        except:
            # Debug
            print("Incorrect! E-Mail or Password! ")
            return
            
    def firebase_register(self, email_address, unhashed_password):
        print("Registering... ")
        try:
            hashed_password=str(hashlib.md5(unhashed_password).encode()).hexdigest()
            firebase_register=self.auth.create_user_with_email_and_password(email_address, hashed_password)
        except:
            # Debug
            print("Email Already Exists! ")
            return
        return

    def write_db(self, child, data):
        try:
            with open("API/identity.json") as infile:
                jobject=json.load(infile)
            # To Load UUID, | jobject["uuid"] | jobject["token"]
            commit=self.db.child(jobject["uuid"]).child(child).set(data, jobject["token"])
            commit()
        except:
            return

    def read_db(self, child):
        try:
            with open("API/identity.json") as infile:
                jobject=json.load(infile)
            # To Load UUID, | jobject["uuid"] | jobject["token"]
            retrive=self.db.child(jobject["uuid"]).child(child).get(jobject["token"])
            print(retrive.val())
            return retrive.val()
        except:
            return


