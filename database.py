from pymongo import MongoClient


# Get database and collection
client = MongoClient()
db = client.test
all_anime = db.anime_info


# Add anime to database
def add(title, url, alt_titles=[], episodes=[], resolution=[]):
    all_anime.insert_one({
        "title": title,
        "url": url,
        "alt_titles": alt_titles,
        "episodes": episodes,
        "resolution": resolution
    })


# Update the anime list
def update_anime(anime):
    for i in range(5):
        title = anime[i].string.strip()
        url = "https://kissanime.to" + anime[i]["href"]
        add(title, url)

    # for a in all_anime.find():
    #     print(a)
    # print(anime[16].string.strip())
    # print(posts.find_one({"author": anime}))
