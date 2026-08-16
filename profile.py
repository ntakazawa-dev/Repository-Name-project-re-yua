import json
import os

PROFILE_FILE = "profile.json"

def load_profile():

    if os.path.exists(PROFILE_FILE):

        with open(PROFILE_FILE, "r", encoding="utf-8") as f:
            profile = json.load(f)

    else:

         profile = {
            "nickname": "",
            "personality": "",
            "favorite_food": "",
            "hobby": "",
            "strength": ""
        }
         
         with open(PROFILE_FILE, "w", encoding="utf-8") as f:
            json.dump(profile, f, ensure_ascii=False, indent=4)

    return profile       

def analyze_profile(memory):

     profile = {
         
         "nickname": 
             memory["profile"]["name"],
         
         "favorite_food":
             memory["profile"]["likes"],
        
         "goal":
             memory["profile"]["goals"],

         "affection":
             memory["relationship"]["affection"]
    }

     return profile

def save_profile(profile):

    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=4)
