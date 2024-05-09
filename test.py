import requests
import json

movie_name = "Avengers Endgame"

url = f"https://api.themoviedb.org/3/search/movie?query={movie_name}&include_adult=false&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9"
                     ".eyJhdWQiOiIxOTM5NDBlOWViMDFkYjI0YjljZWNlNzg1NjMyYmQwMSIsInN1YiI6IjY2"
                     "MTU3MTY2MTVhNGExMDE3ZGY4OWJhMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ"
                     ".dAuFL1oq35UB4Jlpcv"
                     "7izNRp5UMSO7eFvBXJAhBiPnA"
}

response = requests.get(url, headers=headers).text
all_movies = json.loads(response)

movie_inp = input("Select the full name: ")

for movie in all_movies["results"]:
    print(movie["title"])
    print(movie["overview"])
    print(movie["poster_path"])

print(all_movies["results"][0]["title"])

