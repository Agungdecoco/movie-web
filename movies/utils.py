import json
from movies.models import Movies
import os

def load_movies():
    file_path = os.path.join(os.path.dirname(__file__), '../movies.json')
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        Movies.objects.create(
            name=item['name'],
            description=item['description'],
            img_path=item['imgPath'],
            duration=item['duration'],
            genre=item['genre'],
            language=item['language'],
            mpaa_rating_type=item['mpaaRating']['type'],
            mpaa_rating_label=item['mpaaRating']['label'],
            user_rating=int(item['userRating'])
        )
