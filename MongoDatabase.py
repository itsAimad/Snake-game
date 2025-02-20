import random
from datetime import datetime

from pymongo import MongoClient


def mongo_connection():
    # client
    client = MongoClient("CONNECT TO YOUR MONGODB LOCALHOST")

    # db
    db = client["SnakeGame"]
    scores_collections = db["Scores"]

    # query = scores_collections.insert_one({"Date":datetime.now().strftime("%m-%d-%y %H:%M:%S"),"Score":random.randint(400,1000)})

    # if (query):
    #         return True
    # else:
    #     return False

    return scores_collections


# if __name__ == "__main__":
#     if(mongo_connection()):
#         print("YEES")
#     else:
#         print("nooo")