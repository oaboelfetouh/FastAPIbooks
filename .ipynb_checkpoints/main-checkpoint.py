import jwt
from fastapi import FastAPI, Depends, HTTPException, status
from models import user, admin, book, user_pydantic, userIn_pydantic, admin_pydantic, book_pydantic, bookIn_pydantic
from passlib.hash import bcrypt

JWT_SECRET = 'MyNameIsOmarMohamedAboelfetouh&IDoArt'
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# the cach data
comments = dict()

async def verify_user(username: str, password: str):
user = await user.get(username=username)
if not user:
    return False
if not user.verify_password(password):
    return False
return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        user = await User.get(id=payload.get('id'))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )

    return await User_Pydantic.from_tortoise_orm(user)

#login and get the token
@app.post('/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await verify_user(form_data.username, form_data.password)
    if not user:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid username or password'
    )
    user_obj = await user_pydantic.from_tortoise_orm(user)
    token = jwt.encode(user_obj.dict(), JWT_SECRET)
    return {'access_token' : token, 'token_type' : 'bearer'}

# create a user
@app.post('/users')
async def create_user(user: userIn_pydantic)
     user_obj = user(username=user.username, password_hash=bcrypt.hash(user.password_hash))
     await user_ibj.save()
     return await User_Pydantic.from_tortoise_orm(user_obj)
     
# USER TOOLS
@app.post('/comments')
async def post_comment(user: user_pydantic = Depends(get_current_user),bookid : int = Body() comment : str = Body()):
    comments[1].append(comment)
    return comment
    
@app.get('/comments')
async def get_comment(user : user_pydantic = Depends(get_current_user), bookid: int = Body()):
    return comments[bookid]

@app.get('/books')
async def get_books(user : user_pydantic = Depends(get_current_user))
    return await book.all()
    
app.get('/book')
async def get_book(user : user_pydantic = Depends(get_current_user), id : int):
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
async def create_book(admin : admin_pydantic = Depends(get_admin), book:bookIn_pydantic):
    book_obj = book(name = book.name, Author = book.Author)
    await book_obj.save()
    return book_pydantic.from_tortoise_orm(book_obj)
