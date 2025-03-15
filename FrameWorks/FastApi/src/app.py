from fastapi import FastAPI
app =FastAPI()

@app.get('/')
def home():
    return 'hello world'
@app.get('/about')
def about():
    obj={
        "name":'santu',cd 
        "age":'12',

    }
    return obj