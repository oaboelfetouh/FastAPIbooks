from models import user, user_pydantic,userIn_pydantic, admin, admin_pydantic, book, book_pydantic, bookIn_pydantic

from jose import JWTError, jwt
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt

from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from passlib.hash import bcrypt

from passlib.hash import bcrypt
from tortoise.contrib.fastapi import register_tortoise

JWT_SECRET = 'MyNameIsOmarMohamedAboelfetouh&IDoArt'
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# the cach data
comments = dict()

async def verify_user(username: str, password: str):
    user__ = await user.get(username=username)
    if not user:
        return False
    if not user__.verify_password(password):
        return False
    return user__

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        user = await user.get(id=payload.get('id'))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )

    return await user_pydantic.from_tortoise_orm(user)

#login and get the token
@app.post('/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_ = await verify_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )
    user_obj = await user_pydantic.from_tortoise_orm(user_)
    token = jwt.encode(user_obj.dict(), JWT_SECRET)
    return {'access_token' : token, 'token_type' : 'bearer'}

# create a user
@app.post('/users')
async def create_user(user_: userIn_pydantic):
     user_obj = user(username=user_.username, password_hash=bcrypt.hash(user_.password_hash))
    
     await user_obj.save()
     return await user_pydantic.from_tortoise_orm(user_obj)
     """
     why the input is hash_passcode? why not just password?
     """
     
     
# USER TOOLS
@app.post('/comments')
async def post_comment(user: user_pydantic = Depends(get_current_user),bookid : int = Body(), comment : str = Body()):
    comments[1].append(comment)
    return comment
    
@app.get('/comments')
async def get_comment(user : user_pydantic = Depends(get_current_user), bookid: int = Body()):
    return comments[bookid]

@app.get('/books')
async def get_books(user : user_pydantic = Depends(get_current_user)):
    return await book.all()
    
app.get('/book')
async def get_book(user : user_pydantic = Depends(get_current_user), id : int = Query()):
    return await book.filter(id = id)


# ADMIN TOOLS
async def get_admin(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        admin = await admin.get(id=payload.get('id'))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )

    return await admin_pydantic.from_tortoise_orm(admin)
    
@app.post('books')
async def create_book( book:bookIn_pydantic, admin : admin_pydantic = Depends(get_admin)):
    book_obj = book(name = book.name, Author = book.Author)
    await book_obj.save()
    return book_pydantic.from_tortoise_orm(book_obj)


register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True
)
