import webbrowser

info = {
    "title": "Infinity War",
    "release_year": 2018,
    "IMDB_rating": 8.6,
    "trailer": webbrowser.open("https://www.youtube.com/watch?v=6ZfuNTqbHE8"),

}
print("Title:", info["title"])
print("Release year:", info["release_year"])
print("IMDB rating:", info["IMDB_rating"])
print("Trailer:", info["trailer"])
