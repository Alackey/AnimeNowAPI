from pymongo import MongoClient


client = MongoClient()
db = client.test

posts = db.posts

post = {
    "author": "Mike",
    "tags": ["python", "flask", "restful"]
}

post_id = posts.insert_one(post).inserted_id
print(post_id)
print(posts.find_one())
