import json
import os

MEMORY_FILE="memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return{
            "profile":{
                "name":"",
                "likes":[],
                "dislikes":[],
                "goals":[]
            },
            "memories":[],
            "relationship":{
              "affection":0
            }
        }
    else:
        with open(MEMORY_FILE,"r",encoding="utf-8")as f:
            memory = json.load(f)

     # 古いmemory.jsonに足りない項目があれば追加する
    if "profile" not in memory:
        memory["profile"] = {}

    if "name" not in memory["profile"]:
        memory["profile"]["name"] = ""

    if "likes" not in memory["profile"]:
        memory["profile"]["likes"] = []

    if "dislikes" not in memory["profile"]:
        memory["profile"]["dislikes"] = []

    if "goals" not in memory["profile"]:
        memory["profile"]["goals"] = []

    if "memories" not in memory:
        memory["memories"] = []

    if "relationship" not in memory:
        memory["relationship"] = {}

    if "affection" not in memory["relationship"]:
        memory["relationship"]["affection"] = 0

    save_memory(memory)
    return memory   


def save_memory(memory):
    with open(MEMORY_FILE,"w",encoding="utf-8")as f:
        json.dump(memory,f,ensure_ascii=False,indent=4)
