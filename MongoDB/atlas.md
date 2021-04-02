# Python Application Connection

username: simon
password: codeforfun2020

```py
import pymongo
client = pymongo.MongoClient("mongodb+srv://simon:codeforfun2020@cluster0.23jm7.mongodb.net/retryWrites=true&w=majority")
# Test connection
for name in client.list_database_names():
    print(name)

# libraryDB: Document, books: collection
# MongoDB atlas will create "libraryDB and books" is not exists
collection = client.libraryDB.books
booksData = [

      {
         "id":"01",
         "language": "Java",
         "edition": "third",
         "author": "Herbert Schildt"
      },

      {
         "id":"07",
         "language": "C++",
         "edition": "second",
         "author": "E.Balagurusamy"
      }
   ]

collection.insert_many(booksData)

```
