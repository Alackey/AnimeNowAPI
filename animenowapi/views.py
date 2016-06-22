from animenowapi import app, db
from flask import request, jsonify


# Get anime matching query
@app.route("/search")
def search():
    if request.method == "GET":

        # Get anime that contain a keyword or match the given title
        animes_found = db.search(query=request.args.get("query"))

        # Aggregate titles from animes found in database
        titles = []
        for anime in animes_found:
            titles.append(anime["title"])

        return jsonify({"titles": titles})


# Get the url of an anime
@app.route("/animeurl")
def animeurl():
    if request.method == "GET":

        # Get the anime information
        anime = db.search(
            query=request.args.get("query"),
            is_title=True
        )

        # If not anime is found
        if anime is None:
            return jsonify({"url": "Error: Title not found", "Error": True})

        return jsonify({"url": anime["url"]})
