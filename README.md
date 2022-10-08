# Django customer management App
## Functions
- User registration, login and logout
- For a user to register, will need to give a username, email and password
- All the quiz questions are multiple choice
- If the user already did a question, it will then be excluded from visibility
- Show courses, classes and exams only if user is authenticated

# Usage
1. First clone the project locally and then go into the directory
```
git clone https://github.com/Orcha02/back-academo.git
cd backAcademo
```
2. Start up the web-server:
```
./manage.py runserver OR python manage.py runserver
```
3. In your web-browser, load up the following url
```
http://127.0.0.1:8000/login
```
4. Create a super user to populate the database
```
python manage.py createsuperuser
```
5. In your web-browser, load up the following url

```
http://127.0.0.1:8000/admin
```
# Developer
- Daniel Ortega Chaux