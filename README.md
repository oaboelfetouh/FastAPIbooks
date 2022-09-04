# API Books project with admin feature V1.0
Check the Documentation in : 
This project was made from A to Z by Omar Aboelfetouh
Linkedin : 

# About the project
## the regular tool
- See all the books
- See  a particular book
- Comment on each book
- See all the comments about a particular book

## the admin tool
- Add books 
NOTE: the admin cannot have the regular user's permission, FIX THAT

## tasks
1 - create the models: Admin, user, book
DONE

2 - Create the Database of books, users, and admins
DONE

3 - Create the Authentication Flow
DONE

4 - Create APIs: Post (create a new book(admin tool), A regular user in the DB, comment/review)
DONE

5 - Create APIs: Get (All books, Specific book with ID, All comments/reviews of 1 book)
DONE

6- Create a cach data structure to store the Comments of each book
DONE

7 - Do better Documentation :))
(Extra) 8 - Make a nice UI on Figma to pass to the Frontend developer



## THE SECURITY SYSTEM EXPLAINED
1
you create a schema first 
** oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") **

2
Create the login function that returns the token ( the path has to be '/token')
the login function verifies the user and if it exists in the DB it returns the token which you can use in the app

3
create a get_user() dependency that returns your user and depends on the token :)) 
it won't return any user without that token 
It returns the user from the right data table 

5
Create your APIs that depends on the user
So those APIs won't work without a user and  a user won't be here without a token, and a token needs to login, and the login verifies you username and passcode :))

# API Books project with admin feature V1.1
## problems in v1.0
- Can't Use the admin tools, the admin doesn't work, and incomplete
- Add some APIs
    Get data about books
    Make users add books to be approved by the admin!
