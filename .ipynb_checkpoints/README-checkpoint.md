# API Books project with admin feature
Chech the Documentation in : 
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
NOTE : the admin cannot have the regular user's premission, FIX THAT

## tasks
1 - creat the models : Admin, user, book
DONE

2 - Create the Database of books, users, and admins
DONE

3 - Create the Authentication Flow
DONE

4 - Create APIs: Post (create a new book(admin tool), A regular user in the DB, comment/review)
DONE

5 - Create APIs: Get (All books, Specific book with ID, All comments/reviews of 1 book)
DONE

6- Create a cach datastructure to store the Comments of each book
DONE

7 - Do better Documentation :))
(Extra) 8 - Make a nice UI on Figma to pass to the Frontend developer



## THE SECURITY SYSTEM EXPLAINED
1
you create a schema first 
** oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") **

2
Create the login function that returns the token ( the path has to be '/token')
the login function verifies thay user and if it exists in the DB it returns the token which you can use in the app

3
creat a get_user() depency that returns your user and depends on the token :)) 
it wont return any user without that token 
It returns the user from the right data table 

5
Creat your apis that depends on the user
SO those APIs wont work without a user, and  a user wont be here without a token, and a token needs to login, and the login  verify you username and passcode :))
