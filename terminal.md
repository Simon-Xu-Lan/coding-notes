- **Folder:** `14-Post-Author-Joins/Unsolved`

- **INSTRUCTIONS:**

  The goal of this exercise is to modify our find queries in both post-api-routes.js and author-api-routes.js to use Sequelize's "include" option. We can use "include" to say that we want to return associated data.

  1. Open the folder slacked out to you

  2. Run `npm install`

  3. Open the `config` folder and update the `config.json` file's `development` object to match your own local MySQL database.

  4. Navigate to the `post-api-routes.js` file.

  5. Add the "include" option to the queries specified in the comments. This is a feature called "eager loading". We want to "include" the Author model. Examples can be found here:
     <https://sequelize.org/master/manual/eager-loading.html>

  6. Navigate to the `author-api-routes.js` file and add the "include" option to the queries specified in the comments. Here we want to "include" the Post model.

  7. If successful the application should now be fully functional. After you create a few Authors with a few posts, try navigating to either `localhost:8080/api/posts` or `localhost:8080/api/authors` to make sure the JSON returned for both routes includes all of the data.

  **Hint**: The "include" key goes on the same options object as the "where" attribute we've been using. Examples can be found at the link supplied.

  - Basic command
   - mkdir <FOLDER NAME>
      - make new folder
   - touch <File name>
      - create a new file
   - rm 
      - remove a file 
   - rm -d folder name
      - remove a folder
   - echo "text" > filename
      - write text into file
   - open a file
      - mac
         - open file name
      - windows
         - explore file name
   
- copy folder
   cp -R source_dir destination_dir
   #example
   cp -R /etc /etc_backup
   Source:devconnected.com

- copy file

| | |
| --- | --- |
| pwd |         # print working directory |
| ls |       # list files in directory |
| cd |        # change directory
| ~  |         # home directory
| .. |         # up one directory
| -  |         # previous working directory
| help |       # get help
| -h   |       # get help
| --help |      # get help
| man  |       # manual
| cat  |       # output the contents of a file
| mkdir |       # create new directory
| open |       # open a file with the associated program, a directory with Finder, or a URL with the default web browser
| ps   |       # list all running processes
| kill |       # terminate existing process
| rmd  |      # permanently delete file
| rmdir |       # remove directory


## .gitignore
- look at .gitignore file
  - **vim .gitignore**
