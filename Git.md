- What is Git / GitHub

  - Git and GitHub are tools that help people collaborate and safely store their code.
  - GitHub is an online space to store code.
  - GitHub also allows you to share code with other people and work together on projects.
  - Git

    - a software application that runs on your machine
    - allows you to add things to GitHub
    - and to download things from GitHub.

    - Git is a version control software that runs on your computer.

    - Git tracks tracks changes to any files in your project.

      - If you have a working application and you accidentally break it, you can roll it back to a previous point.
      - ou can go back to any point in time that you saved.

    - It allows you to add (push) and download (pull) code from your online code repository on GitHub.
      - This functionality is similar to the Dropbox client that syncs your local files with Dropbox.
    - If you used git and saved (pushed) frequently enough, you can roll back to exactly the point where you took a wrong turn.

- What is GitHub?

  - GitHub is a web-based storage solution for developers.
  - It's like the developer's Dropbox or Google Drive.
  - It's also a version control system.
  - Cloud storage, version control, and source code management all in one!
  - GitHub is an online space to work collaboratively on projects and keep your code safe.

- Git tracks your changes to the source code via commits, and syncs with a remote source, like GitHub
- via push (to send your commits to the remote)
- pull (to retrieve commits from the remote) commands.

- How do I use Git and GitHub?

  - Create a new repository
  - Copy the link
  - In terminal, cd into the directory where you want your repo to live
  - Clone the repo using git clone <repo name>
  - cd into the repo
  - Add a file
  - Stage the changes in your current working directory using git add .
  - Commit the changes using git commit -m "some message"
  - Push the changes using git push origin main

- Feature Branching

  - The main idea behind feature branching is that all feature development should take place in a dedicated branch rather than pushing directly to the main branch.
  - How to work

    - Create a new branch.
    - Then, all changes to our repository (additions, modifications, or deletion) are made inside this branch.
    - We then commit our changes, and push them to the remote source (GitHub).
    - Once the branch has been pushed to the remote, we open a Pull Request.
    - Once the Pull Request has been made, there will very often be automated tests that run to ensure that your modifications to not break the working application.
    - Pull Requests also initiate a discussion about the changes you've committed, and generally have to be approved by someone else on the team. That person (or entire team) will review your changes to make sure that everything is in order.
    - Once any concerns have been addressed and the Pull Request has been approved, the modified code is merged into the main branch.

  - Steps

    - cd into the repo directory
    - Create and switch to a new branch using git checkout -b new-branch-name
    - Make the changes to your repository that you desire
    - Stage the changes using git add -A
    - Commit the changes using git commit -m "some message"
    - Push the changes using git push origin new-branch-name
    - Navigate to your GitHub repository in your browser
    - On the Pull requests tab, create a new pull request

  - To switch between existing branches

    - git checkout branch-name
    - Note that you do not need the -b flag in your git checkout command this time because we are not creating a new branch.

  - To merge your changes into main, and update your local repository with those changes:
    - On GitHub, merge the Pull Request you created.
    - On your computer, switch back to your main branch using git checkout main
    - Pull the updates from the remote server with git pull

- Terminology

  - Version Control System (VCS) or Source Code Manager (SCM)
    - A VCS allows you to:
      - revert files back to a previous state
      - revert the entire project back to a previous state,
      - review changes made over time,
      - see who last modified something that might be causing a problem, who introduced an issue and when, and more.
  - Commit (snapshot):
    - Git thinks of its data like a set of snapshots of a mini file system.
    - Every time you commit, or save the state of your project in Git,
    - it basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot.
  - Repository (repo):
    - A directory that contains your project work,
    - as well as a few files(hidden by default in Mac OS X) which are used to communicate with Git.
    - Repositories can exist either locally on your computer or as a remote copy on another computer.
  - Working Directory:
    - The files that you see in your computer's file system.
    - When you open your project files up on a code editor, you're working with files in the Working Directory.
    - This is in contrast to the files that have been saved (in commits!) in the repository.
    - When working with Git, the Working Directory is also different from the command line's concept of the current working directory which is the directory that your shell is "looking at" right now.
  - Checkout:
    - When content in the repository has been copied to the Working Directory.
    - It is possible to checkout many things from a repository; a file, a commit, a branch, etc.
  - Staging Area or Staging Index or Index:
    - A file in the Git directory that stores information about what will go into your next commit.
    - You can think of the staging area as a prep table where Git will take the next commit.
    - Files on the Staging Index are poised to be added to the repository
  - SHA:
    - A SHA is basically an ID number for each commit.
    - It is a 40-character string composed of characters (0–9 and a–f) and calculated based on the contents of a file or directory structure in Git.
    - "SHA" is shorthand for "SHA hash". A SHA might look like this:
      - e2adf8ae3e2e4ed40add75cc44cf9d0a869afeb6
  - Branch:

    - A branch is when a new line of development is created that diverges from the main line of development.
    - This alternative line of development can continue without altering the main line.
    - Going back to the example of save point in a game, you can think of a branch as where you make a save point in your game and then decide to try out a risky move in the game. If the risky move doesn't pan out, then you can just go back to the save point. The key thing that makes branches incredibly powerful is that you can make save points on one branch, and then switch to a different branch and make save points there, too.

  - git init
    - Create brand new repositories(repos) on your computer
    - Running the git init command sets up all of the necessary files and directories that Git will use to keep track of everything.
    - This is where git records all of the commits and keeps track of everything!
    - All of these files are stored in a directory called .git
      - (notice the . at the beginning - that means it'll be a hidden directory on Mac/Linux).
    - This is where git records all of the commits and keeps track of everything!
  - git clone
    - Copy existing repos from somewhere else to your local computer
  - git status
    - Check the status of a repo

- Adding an existing project to GitHub using the command line:

  - https://stackoverflow.com/questions/50025872/how-do-i-connect-a-local-folder-to-an-existing-github-repo/50026014
    - git init # Initialize the local directory as a Git repository.
    - git add . # Add files
    - git commit -m "First commit" # Commit your changes
    - git remote add origin <Remote repository URL> # # Add remote origin
    - git remote -v # Verifies the new remote URL
    - git push origin master # Push your changes

- Check existing git url at local git repo

  - git remote -v
    - result:
      - origin https://github.com/Simon-Xu-Lan/data_hw1_excel_challenge.git (fetch)
      - origin https://github.com/Simon-Xu-Lan/data_hw1_excel_challenge.git (push)
  - or git config --get remote.origin.url
    - result:
      - https://github.com/Simon-Xu-Lan/data_hw1_excel_challenge.git

- error: src refspec master does not match any.

  - Fixed by
    - git push origin HEAD:main
    - https://stackoverflow.com/questions/4181861/message-src-refspec-master-does-not-match-any-when-pushing-commits-in-git

- git commit -m #
  - ignore the message
