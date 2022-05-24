# Push Flask App to heroku for webhosting

- https://www.youtube.com/watch?v=Li0Abz-KT78

# Prepare
1. sign up an account in www.heroku.com
2. Login to your account in www.heroku.com
3. Clikc New button on the top right corner of dashboard.
4. Give a app name and create an app.
5. Download Heroku ClI and install it
    - search Heroku CLI in the web
    - https://www.youtube.com/watch?v=D2GLVoiEZyE
## Steps

1. create a project folder and cd to the project folder
2. create virtual environment in the project foder, and activate it
- Option A: activate existing virtual environment
    ```shell
    conda activate mlenv
    ```
- Option B:
    - inside the project folder run the following command, which would create a folder "venv" inside the project folder

    ```shell
    python3 -m venv venv
    ```

    - activate vitural environment, resulting in "(venv) (base) simonxu@SimonXus-MacBook-Pro <project folder name>"

    ```
    source venv/bin/activate
    ```

3. Install "gunicorn"

```
pip install gunicorn
```

4. Create "Procfile" file in the project folder. p is in captalized.

```
touch Procfile
```

5. edit Procfile - add the following line to the Procfile and save and close

- tell the web server that the main app name is main. if the main app uses other name, change main to it.
- make sure not "app:main"

```
web: gunicorn main:app
```

6. create requirements.txt in the project folder, make sure all dependencies are install at the venu environment/project folder
    - Pandas version for heroku 0.8.1

```
pip freeze > requirements.txt
```
- edit reqiurements.txt to remove all the packages that are not used in your app. 
    - Only includes the packaged that are used in your app, which reduce the size of heroku app.

7. Init repo if current working directory is not repo, add to repo. commit to repo

```
git Init
git add .
git commit -m "initial commit"
```

8. Heroku login

```
heroku login
```

9. Connect the local repo to remote heroku app
- Option A:  create app to heroku if you didn't create app in heruko.com

    ```
    heroku create
    ```

- Option B: 
    ```shell
    # connect the local repo to remote heroku app
    heroku git:remote -a your-app-name
    ```

10. option: change domain name

```
heroku rename <domain name>
```

11. push code to heroku master and publish with
    - master or main

```console
git push heroku master
```

# debug
## find error message related to your app deployment
```shell
heroku logs --tail --app your-app-name
```

## Numpy issue
- 
## Another reference: 100 days code - Setup a WSGI server with gunicorn
- https://stackoverflow.com/questions/33588763/heroku-not-recognizing-numpy-in-requirements-txt

- https://www.udemy.com/course/100-days-of-code/learn/lecture/22970414#search

https://belly-biodiversity-samples.herokuapp.com/
