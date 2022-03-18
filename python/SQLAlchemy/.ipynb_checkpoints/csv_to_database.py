import sqlalchemy
from sqlalchemy import create_engine
conn=create_engine('sqlite:///breweries.sqlite').connect()
df=pd.read_csv('breweries.csv', index_col='index')
df.to_sql('breweries', conn)
# use PRAGMA table_info to get column names
# conn.execute('PRAGMA table_info(breweries); ').fetchall()
sql_rm_query='ALTER TABLE breweries RENAME TO breweries_old; '
sql_crt_query='CREATE TABLE breweries (\
                  id bigint primary key,\
                  name text,\
                  website text,\
                  address text,\
                  city text,\
                  state text\
                  ); '
sql_ins_query='INSERT INTO breweries SELECT * FROM breweries_old; '
sql_drp_query='DROP TABLE breweries_old'
conn.execute(sql_rm_query)
conn.execute(sql_crt_query)
conn.execute(sql_ins_query)
conn.execute(sql_drp_query)

# Normally, loading a DataFrame into a table can be done quickly with to_sql().
# However, it doesn’t not allow a column to be defined as the Primary Key, which would be useful for our database. 
# Since SQLite doesn’t allow significant changes to existing tables, 
# we use a series of sql commands to create a new table with a primary key and insert into it the data from the old table.