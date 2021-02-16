# instruction

- we will need two separate but related software for the SQL part of the course:
  - Postgres - PostgreSQL, also known as Postgres, is a relational database management system.
  - pgAdmin - it is a a web application used as the user interface (UI) for Postgres
- attached are the instructions for installing the required software. below are some important notes:
  1. pgAdmin comes with the installation of Postgres - please be sure to CHECK this during the installation.
  2. another component - Stack Builder - can complicate our settings down the road. please be sure to UNCHECK this during installation.
  3. i use postgres as username and password - this makes it easy to remember.
  4. keep the default port of 5432 when prompted. if you are defaulted to a different port, then you have another version of SQL installed. i would recommend uninstalling it first before and restart the installation process.

# Installing pgAdmin and Postgres on a Mac

Similar to coding with Python using Visual Studio Code, SQL requires a code editor with the ability to execute the scripts developers (you!) create.

## Before you Begin

- Remember to choose the installation package specific to your operating system and download the latest version.

- Be prepared to record a password, this will be needed later!

## Download Link(s)

- [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

## Instructions

- After downloading the latest version of PostgreSQL 11, double click on the `postgresql-11.x-osx` file. **Note:** exact file version may be slightly different.

  ![postgresql-11.1-1-osx.png](../Images/postgresql-11.1-1-osx.png)

- Go through the Setup Wizard and install PostgreSQL. Keep the default location as: `/Library/PostgreSQL/11`.

- Select the components to be installed. **Be sure to un-check `Stack Builder`.**

  ![postgres_components.png](../Images/stack_builder_mac.png)

- Next, add your Data Directory. Keep the default location as: `/Library/PostgreSQL/11/data`.

- Next, enter `postgres` as the password. **Be sure to record this password for future use.**

- Keep the default port as `5432` and in the Advanced Options, set the locale as `[Default locale]`.

- The final screen will be the `Pre Installation Summary`.

- When you are done you should have a folder in your Applications with these files.

  ![PostgreSQL_folder.png](../Images/PostgreSQL_folder.png)

- To confirm the installation, start `pgAdmin` (this will open in a new browser window) and connect to the default server by clicking on it and entering the password if prompted.

# Installing pgAdmin and Postgres on Windows

Similar to coding with Python using Visual Studio Code, SQL requires a code editor with the ability to execute the scripts developers (you!) create.

## Before you Begin

- Remember to choose the installation package specific to your operating system and download the latest version.

- Be prepared to record a password, this will be needed later!

## Download Link(s)

- [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

- [Installation Instructions](https://www.enterprisedb.com/docs/en/11.0/PG_Inst_Guide_v11/toc.html)

## Instructions

- After downloading the latest version of PostgreSQL 11, double click on the `postgresql-11.x-windows-x64.exe` file.

- **Note:** exact file version may be slightly different.

  ![postgresql-11.1-1-windows-x64.png](../Images/postgresql-11.1-1-windows-x64.png)

- Go through the Setup Wizard and install PostgreSQL. Keep the default location as: `/Library/PostgreSQL/11`.

- Select the components to be installed. **Un-check the option to install [Stack Builder](https://www.enterprisedb.com/docs/en/9.3/pginstguide/PostgreSQL_Installation_Guide-08.htm#P230_11507)**.

  ![stack_builder.png](../Images/stack_builder_pc.png)

- Next, add your Data Directory. Keep the default location as: `/Library/PostgreSQL/11/data`.

- Next, enter `postgres` as the password. **Be sure to record this password for future use.**

- Keep the default port as `5432` and in the Advanced Options, set locale as as `[Default locale]`.

- The final screen will be the `Pre Installation Summary`.

- When you are done, the `Postgres 11` folder can be accessed from the start menu of your computer.

  - This folder contains the `pgAdmin 4` application, which will be used throughout this unit.

  - To confirm the installation, start `pgAdmin` (this will open in a new browser window) and connect to the default server by clicking on it and entering the password if prompted.
