# Solution 1: Deploy app to Heroku by command
1. sign up an account in www.heroku.com
2. Login to your account in www.heroku.com
3. Clikc New button on the top right corner of dashboard.
4. Give a app name and create an app.
5. Download Heroku ClI and install it
6. At terminal run the following 
    ```shell
    heroku login
    ```
7. First thing to make sure your app is initialized as git repo
    - if not, run the folloiwng command. simon
    ```shell
    git init
    # connect the local repo to remote heroku app
    heroku git:remote -a your-app-name
    ```
    - if it is existing git repository, 
    ```shell
    # connect the local repo to remote heroku app
    heroku git:remote -a your-app-name
    ```
8. Push to heroku
    ```shell
    git add .
    git commit -am "make it better"
    git push heroku master
    ```
9. Now the app does works on heroku because heroku doesn't know how to run the app, you have to do the following thing
10. Create Procfile
    ```shell
    touch Procfile
    ```
11. Put the following content in Procfile
    ```js
    # index.js is the app file.
    web: node index.js
    ```
12.  Set the port like following 
    ```js
    var PORT = process.env.port || 3000
    ```
13. Push to heroku
    ```shell
    git add .
    git commit -am "make it better"
    git push heroku master
    ```
14. Once it done, the app should work well on heroku.



### debug
```shell
heroku logs --tai --app your-app-name
```
- make sure package.json has the start script. index.js is the main file of your app.
```json
"scripts" : {
    "test": "...",
    "start": "node index.js" 

}
```

# Solution 2: Deploy app from Github to Heroku

1. Choose GitHub/Coonect to GitHub
2. Connect to Github by authorizing Heroku
3. find the repo name in Github, then clike connect button
4. make sure the branch is what you want to deploy
5. Clikc "enable Automatic deploys"
6. First time, please click "deploy branch"
7. click "view" button
