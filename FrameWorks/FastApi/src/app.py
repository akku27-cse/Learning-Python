from fastapi import FastAPI
app =FastAPI()

@app.get('/')
def home():
    return 'hello world'
@app.get('/about')
def about():
    obj={
        "name":'santu',
        "age":'12',

    }
    return obj
@app.get('/user_input/{user_name}')
def user_Name(user_name):
    return {
        "user_name":user_name,
        "age":"21"
    }
    