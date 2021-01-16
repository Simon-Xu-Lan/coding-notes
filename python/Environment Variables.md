- Enviroment Variables

  - Convenience
  - Security
  - a variable that accessible only when the environment is active
  - Usually used for an app with multiple environment , we can use env variable to store variable with same name and different value to store environment specific data
  - Only one environment can be active at a time.

- Set up Enviroment variable for python code
  - at terminal type the following and then hit enter.
    **export OWM_API_KEY=bac6bdea9c179d427565c0bc9f8fc351**
    - OWM_API_KEY is the variable name
    - no space
    - no quote
- Check enviroment variable at terminal
  **env**

- modify env variable

  - just simply export new value
    **export OWM_API_KEY=NEW_VALUE**

- Access to the enviroment varialbe during coding
  ```py
    import os
    opi_key = os.environ.get("OWM_API_KEY")
  ```
- Example

  - https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5

  ```py
    import os

    # Set environment variables
    os.environ['API_USER'] = 'username'
    os.environ['API_PASSWORD'] = 'secret'

    # Get environment variables
    USER = os.getenv('API_USER')
    PASSWORD = os.environ.get('API_PASSWORD')

    # Getting non-existent keys
    FOO = os.getenv('FOO') # None
    BAR = os.environ.get('BAR') # None
    BAZ = os.environ['BAZ'] # KeyError: key does not exist.

    # Note that using getenv() or the get() method on a dictionary key will return None if the key does not exist.
    # However, in the example with BAZ, if you reference a key in a dictionary that does not exist it will raise a KeyError.

    https://stackoverflow.com/questions/4906977/how-to-access-environment-variable-values

    - Use the Repl.it documentation to work out how to create a .env file in Repl.it and store your Environment Variables in there.
      https://docs.repl.it/repls/secret-keys#:~:text=env%20files%20are%20used%20for,see%20the%20contents%20of%20the%20.

    - .env file
      https://img-a.udemycdn.com/redactor/raw/2020-07-27_14-49-17-73eb2d5ac7a886b723619c856c429935.png?Ge9GL1reEAGugXK6Te2wjxXzzIa91r5Eylc82huwF2LkeKsNA0KBRGto6cbi8Ht1BXQZvyQG3P-90cJWiiZqgktck1Dz-sbCADXd75sAaJ66pJorhEoYG8PWpb96VxgdHDmvHmIUJPLjvKf8xWQnEHJxXprOcl4MNj-txkHAZcwGWYWO
      


  ```
