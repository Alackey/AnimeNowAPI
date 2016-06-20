from pymongo import MongoClient


# Get database and collection
client = MongoClient()
db = client.test
all_anime = db.anime_info


# Get anime containing keyword
def search(query):
    return all_anime.find({"title": {"$regex": query}})
