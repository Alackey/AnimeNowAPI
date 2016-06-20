from pymongo import MongoClient


# Get database and collection
client = MongoClient()
db = client.test
all_anime = db.anime_info


# Checks if the anime exists in the database
def in_db(title):
    if all_anime.find_one({"title": title}) is not None:
        return True
    return False


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
def update_anime(anime_list):
    for anime in anime_list:
        title = anime.string.strip()
        url = "https://kissanime.to" + anime["href"]
        print(in_db(title))
        # add(title, url)

    # for a in all_anime.find():
    #     print(a)
    # print(anime[16].string.strip())
    # print(posts.find_one({"author": anime}))
