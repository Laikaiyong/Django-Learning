**SETUP**

To clone and run this application, you'll need Git and Python installed on your computer. From your command line:
```
$ git clone https://github.com/sheraaax/django-tutorial-mysite-master.git
```

Create a virtual environment to install dependencies in and activate it:
```
$ py -m venv venv

$ venv\Scripts\activate - Windows
$ source venv/bin/activate - Linux
```

Then install the dependencies:
```
(venv) $ pip install -r requirements.txt
```
Note the (ccbeenv) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.


**USAGE**

Makemigrations and migrate to apply Django models to dbsqlite database:
```
(venv) $ py manage.py makemigrations
(venv) $ py manage.py migrate
```

Create a superuser with this command and fill in the form accordingly from terminal:
```
(venv) $ py manage.py createsuperuser
```

You can run the app on your browser by:
```
(venv) $ py manage.py runserver
```

You can access the app on your browser by using any of these URLs:
```
http://127.0.0.1:8000/admin/
```

Login the admin site with the credentials created during createsuperuser. <br>
Admin site is like viewing your database with a user friendly interface.

To add data, inside Polls, click on Add, and fill in the form. Click save.

<img width="1280" alt="Screenshot 2022-06-01 at 5 01 36 PM" src="https://user-images.githubusercontent.com/50538795/171368105-cd79faf5-72ca-4666-ae91-c22055e43101.png">

You can also add Choices for Questions you have created.

<img width="1280" alt="Screenshot 2022-06-01 at 5 05 36 PM" src="https://user-images.githubusercontent.com/50538795/171368838-3a1d969a-376d-42f4-84cd-a1c7dc9a92b5.png">

To view the Questions you have created, you can navigate to this URL:
```
http://127.0.0.1:8000/polls/
```
