##from fastapi import FastAPI
import fastapi
import uvicorn
import movie_data
from models.movie_model import MovieModel

#app = FastAPI()
app = fastapi.FastAPI()

@app.get("/")
def index():
    return { "message":"Hello world" }

@app.get("/api/movie/{title}", response_model = MovieModel)
async def movie_search(title:str):
    movie = await movie_data.get_movie(title)
    #movie :MovieModel =  await movie_data.get_movie(title)

    if not movie:
        raise fastapi.HTTPException(status_code=404)

    #return movie
    return movie.dict()

if __name__ == "__main__":
    uvicorn.run(app)

