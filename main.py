from fastapi import FastAPI

app = FastAPI()


#Route for home page
@app.get('/')
def index():
    return {'data': {'name': 'Tony'}}


@app.get('/about')
def about():
    return {'data': 'about page'}

