from pymongo import MongoClient


# Get database and collection
client = MongoClient()
db = client.test
all_anime = db.anime_info


# Get anime containing keyword
def search(query, is_title=None):

    if is_title == True:
        return all_anime.find_one({"title": query})
    elif is_title is None:
        return all_anime.find({"title": {"$regex": query, "$options": "i"}})
