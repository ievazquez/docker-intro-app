import httpx
from typing import Optional
from models.movie_model import MovieModel

#from models import movie_model

async def get_movie(title:str) -> Optional[MovieModel]:
    url = f"https://movieservice.talkpython.fm/api/search/{title}"
    async with httpx.AsyncClient() as client:
        resp : httpx.Response = await client.get(url)
        resp.raise_for_status()

        data = resp.json()

    print(resp, resp.text)
    results = data["hits"]
    if not results:
        return None

    print(results[0])
    movie = MovieModel(**results[0])

    #return results[0]
    return movie




