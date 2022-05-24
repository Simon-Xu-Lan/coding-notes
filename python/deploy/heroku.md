# Push Flask App to heroku for webhosting

- https://www.youtube.com/watch?v=Li0Abz-KT78

## Steps

1. create a project folder and cd to the project folder
2. create vitrual environment in the project foder, and activate it

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

7. Init repo if , add to repo. commit to repo

```
git Init
git add .
git commit -m "initial commit"
```

8. Heroku login

```
heroku login
```

9. create app to heroku

```
heroku create
```

10. option: change domain name

```
heroku rename <domain name>
```

11. push code to heroku master and publish with

```console
git push heroku master
```

## Another reference: 100 days code - Setup a WSGI server with gunicorn

- https://www.udemy.com/course/100-days-of-code/learn/lecture/22970414#search

https://belly-biodiversity-samples.herokuapp.com/
