# import csv file

```sql
COPY accidents
FROM '/home/[your_user_name]/accidents.csv'
WITH CSV HEADER DELIMITER',';

-- another solution:
COPY flight_delays FROM '/home/dataguy/sql_ready.csv' DELIMITER ',' CSV HEADER;
```

# Access remote sever

- https://data36.com/data-coding-101-install-python-sql-r-bash/

## For Mac/Linux Users:

- On terminal, type:
- ssh [username]@[IP address]
  - the [Username] is root
  - [IP Address] is the IP Address from the DigitalOcean droplet tab

# Sign in postgresql to superuser's account

- When you installed SQL, it automatically generated one more user on your server called postgres.
- This new user is an SQL superuser.
- sign in to this superuser’s account with this command:
  - sudo -i -u postgres\*
  ```terminal
  sudo -i -u postgres
  ```
  - The superuser will be able to access SQL with this simple command (type it):
  ```terminal
  psql
  ```

## let’s generate a new user, so you can access your database in the future with your normal user too (which is the preferred way).

## You can exit from postgreSQL and go back to bash!

\q

## log out from the superuser as well and go back to your normal user

exit

## login with your normal user to your SQL database with this command:

psql -U dataguy -d postgres

## Exit from postgreSQL

\q

# SQL writing order:

1. SELECT
2. FROM
3. WHERE
4. GROUP BY
5. ORDER BY
6. LIMIT

# SQL execution order - That computer uses:

- Simple

1. FROM
2. WHERE
3. GROUP BY
4. SELECT
5. ORDER BY
6. LIMIT

- SQL first checks which data table we will work with.
- Then it checks the filters.
- After that it groups the data.
- Finally it gets the data
- and if necessary, sorts it
- and prints only the first X rows.

## the order of the SQL keywords your computer sees when processing your query:

1. FROM
2. ON
3. JOIN
4. WHERE
5. GROUP BY
6. SELECT
7. DISTINCT
8. ORDER BY
9. LIMIT

# SQL Indentations and new lines:

- Spaces and line breaks do not affect the outcome of an SQL query.
- The only thing that matters is the semicolon (;) that clearly indicates the end of the SQL query.

# SQL style:

- Use line breaks at least before the main SQL keywords (e.g. SELECT, FROM, WHERE, etc.).
- Actually, I prefer to use line breaks before column names, table names, and each WHERE condition too…
- Use indentation for column names, WHERE conditions (especially with AND, OR) and similars!
- Stay consistent!

- Exqmple:

```sql
SELECT
  animal,
  water_need
FROM
  zoo
WHERE
  animal LIKE '_____'
  AND animal <> 'tiger'
  AND water_need > 200;
```

# Visualize your SQL data in Google Data Studio!

## connect Google Data Studio to PostgreSQL https://data36.com/connect-google-data-studio-postgresql/

0.  Register for Google Data Studio. https://datastudio.google.com/u/0/

- It’s free; all you need is a gmail email address.

1.  Add a new Data Source!

# in SQL, you can’t use nested functions, like MIN(AVG(depdelay))

- aggregate function calls cannot be nested.

# SQL subquery syntax requirements

- your inner query must go between parentheses (( and ))
- subquery in FROM must have an alias
  - your inner query must get a new “name” with aliasing
  - so after the parentheses add this: AS new_name… except that of course you should replace new_name with something more meaningful. 🙂

# SQL CASE (the “if statement” of SQL)

```sql
SELECT COUNT(*),
  CASE WHEN depdelay < 0 THEN 'early'
       WHEN depdelay > 0 THEN 'late'
       ELSE 'ontime'
  END as segment
FROM flight_delays
GROUP BY segment
LIMIT 10;
```

- the CASE WHEN part of your query categorizes the flights, based on the depdelay column, into 3 categories.

```sql
SELECT *,
  CASE WHEN depdelay < 0 THEN 'early'
       WHEN depdelay > 0 THEN 'late'
       ELSE 'ontime'
  END as segment
FROM flight_delays
LIMIT 10;
```

- CASE WHEN statement is creating a new column at the end of the table.

# HAVING

- HAVING is for filtering on the results of SQL functions like COUNT(), SUM(), AVG(), etc.
- HAVING is the new WHERE – at least for the aggregated values in your SQL query.

```sql
SELECT COUNT(*) as nmbr,
       dest
FROM flight_delays
GROUP BY dest
HAVING COUNT(*) > 10000;
```

- **The only unfortunate thing is that you can’t use your aliases with your HAVING, so you need to type the whole COUNT(\*) function again**

# Extra parameters when create table

- NOT NULL:
  - If you add this, you can’t add NULL values to the given column.
- UNIQUE:
  - If you add this, you can’t add the same value to the column twice.
  - This is especially important when you store unique user IDs, for instance.
- PRIMARY KEY:
  - Practically speaking, this is a combination of NOT NULL and UNIQUE
  - but it also has some technical advantages.
  - You can have only one PRIMARY KEY column per table.
