# Alt Blog

Alt Blog is a blog web application. User able to create, edit/update, delete, or read posts.

## Running Locally

Make sure you have Python 3.7.7 [downloads](https://www.python.org/downloads/).

To start and run the local development server,

1. Initialize and activate a virtual environment:

On macOS and Linux:

```
$ cd YOUR_PROJECT_DIRECTORY_PATH/
$ python3 -m venv [env_name]
$ source [env_name]/bin/activate
```

On Windows:

```
$ cd YOUR_PROJECT_DIRECTORY_PATH/
$ py -m venv [env_name]
$ .\[env_name]\Scripts\activate
```

2. Install the dependencies:

```
$ pip install -r requirements.txt
```

3. Run the development server:

.flaskenv file provides development server

```
$ flask db upgrade
$ flask run
```

4. Navigate to Home page [http://localhost:5000](http://localhost:5000)

## Screenshots

![homepage](screenshots/homepage.png)

![postspage](screenshots/postpage.png)
