# Kevin Lee's paper

- https://medium.com/analytics-vidhya/database-management-nosql-vs-sql-or-mongodb-vs-mysql-cfa351caf25a

# to start mongod:

## Mac:

- if use homebrew installed mongoDB:
  - brew services start mongodb-community@4.4
- if not use homebrew installed mongoDB:
  - mongod --config /usr/local/etc/mongod.conf --fork

## Windows:

- skip

# to start mongo:

## Windows:

- mongo in command line

## Mac:

- mongo in terminal

# Basic Shell Operations

https://docs.mongodb.com/manual/reference/mongo-shell/

# Switch to database

- Start up a new database by switching to it. The db does not exist until you create a collection.

```
use travel_db
```

# Show the current db by running db.

```
db
```

# Show current databases in existence

```
show dbs
```

# Create a collection

```
db.createCollection("destinations")
```

# See all collections in a database

```
show collections
```

# Insert data

- Insert data into the travel_db database with this command.

  - NOTE: This will also create the collection automatically, the contents of the insert are basically a JavaScript object, and include an array.

```
db.destinations.insert({"continent": "Africa", "country": "Morocco",
                        "major_cities": ["Casablanca", "Fez", "Marrakech"]})
```

- As a class, come up with 3-5 more countries and insert them into the db using the same syntax as above.

```
db.destinations.insert({"continent": "Europe", "country": "France",
                        "major_cities": ["Paris", "Marseille", "Bordeaux"]})

db.destinations.insert({"continent": "North America", "country": "USA",
                        "major_cities": ["Washington DC", "New York City", "San Francisco"]})
```

# Find data

- Find all data in a Collection with `db.[COLLECTION_NAME].find()`

  - The MongoDB \_id was created automatically.

  - This id is specific for each doc in the collection.

```
db.destinations.find()
```

- Adding .pretty() makes the data more readable.

```
db.destinations.find().pretty()
```

- Find specific data by matching a field.

```
db.destinations.find({"continent": "Africa"})
db.destinations.find({"country": "Morocco"})
```

- Try a few queries with the examples we came up with as a class.

  - Also, pick something that will find more than one entry so we can see how it will return all matches.

  - Find specific data by matching an \_id.

```
db.destinations.find({_id: ObjectId("<ID Number Here>")})

db.destinations.find({_id: ObjectId("5416fe1d94bcf86cd785439036")})
```

# Update

- Use the travel_db

```shell
db
use travel_db
```

- Insert two countries in Africa

```shell
db.destinations.insert({'country': 'Egypt', 'continent': 'Africa', major_cities: ['Cairo', 'Luxor']})
db.destinations.insert({'country': 'Nigeria', 'continent': 'Africa', major_cities: ['Lagos', 'Kano']})
```

## Update the first

- Show how to update data using `db.[COLLECTION_NAME].update()`

```shell
db.destinations.update({"country": "Egypt"}, {$set: {"continent": "Antarctica"}})
```

- Note that the above will only update the first entry it matches.

## Update multiple

- To update multiple entries, you can add `{multi:true}`, all countries listed as being in Africa will now show Antarctica as their continent

```shell
db.destinations.update({"continent": "Africa"}, {$set: {"continent": "Antarctica"}}, {multi: true})
```

- Alternatively, we can use this syntax to update more than one record.

```shell
db.destinations.updateMany({"continent": "Africa"}, {$set: {"continent": "Antarctica"}})
```

## Update to insert if not exist

- Ask the class what they think will happen when you run this command, even though a capital doesn't exist.

```shell
db.destinations.update({"country": "Morocco"}, {$set: {"capital": "Rabat"}})
```

- Answer: it will add the capital field to the document and show the field can now be updated with the same command.

```shell
db.destinations.update({"country": "Morocco"}, {$set: {"capital": "RABAT"}})
```

## update - push

- Show how to push to an array with `$push`.

```shell
db.destinations.update({"country": "Morocco"}, {$push: {"major_cities": "Agadir"}})
```

## update - create if not exist

- The upsert option updates a document if one exists; it otherwise creates a new document.

````shell
db.destinations.update({'country': 'Canada'}, {$set: {'capital': 'Ottawa'}}, {upsert: true})


# Delete
* Show how to delete an entry with `db.[COLLECTION_NAME].remove({justOne: true})`.

```shell
db.destinations.remove({"country": "Morocco"}, {justOne: true})
````

## Show how to empty a collection with `db.[COLLECTION_NAME].remove()`.

```shell
db.destinations.remove({})
```

## drop a collection with `db.[COLLECTION_NAME].drop()`.

```shell
db.destinations.drop()
```

## drop a database

```shell
db.dropDatabase()
```
