**Set up**

1. Make sure you've got the correct smtp address for your email provider:

- smtp address of email provider
  - Gmail: smtp.gmail.com
  - Hotmail: smtp.live.com
  - Outlook: outlook.office365.com
  - Yahoo: smtp.mail.yahoo.com
  - If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"

2. Make sure you've enabled less secure apps if you are sending from a Gmail account.
1. Manage your Google Account
1. Security
1. Signing in to Google

   - Use your phone to sign in => off
   - 2-step Verification => off

   4. Less secure app access => on

1. Try to go through the Gmail Captcha here while logged in to the Gmail account:

   - https://accounts.google.com/DisplayUnlockCaptcha

1. Add a port number by changing your code to this:

   - smtplib.SMTP("smtp.gmail.com", port=587)

**SMTP**

- Simple Mail Transfer Protocal

**smtplib**

- Python smtplib Documentation
  - https://docs.python.org/3/library/smtplib.html
- Demo code

```py
  import smtplib

  my_email = "codeforfun2020@gmail.com"
  password = "Bettiscanada2"
  # Create an object from SMTP class
  connection = smtplib.SMTP("smtp.gmail.com", port=587)
  # make the connection secure using TLS
  connection.starttls()
  connection.login(user=my_email, password=password)
  connection.sendmail(
      from_addr=my_email,
      to_addrs="codeforfun2020@yahoo.com",
      msg="Subject:Hello\n\nThis is the body of my email."
  )
  connection.close()

  # use with key word, no need to use close(). it will close the connection automatically
  # Create an object from SMTP class
  with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
      # make the connection secure using TLS
      connection.starttls()
      connection.login(user=my_email, password=password)
      connection.sendmail(
          from_addr=my_email,
          to_addrs="codeforfun2020@yahoo.com",
          msg="Subject:Hello\n\nThis is the body of my email."
      )
```

**TLS**

- Transport Layer Security

**Error**

- UnicodeEncodeError: 'ascii' codec can't encode character u'\u201c' in position 34: ordinal not in range(128)

  - https://stackoverflow.com/questions/24264892/unicodeencodeerror-ascii-codec-cant-encode-character-u-u201c-in-position-3
  - use .encode() to encode the string:
  - demo code

  ```py
    import smtplib
    import datetime as dt
    from random import choice

    MY_EMAIL = "codeforfun2020@gmail.com"
    PASSWORD = "Bettiscanada2"

    now = dt.datetime.now()
    day_of_week = now.weekday()

    if day_of_week == 0:
        with open("quotes.txt") as file:
            quotes_list = file.readlines()
            quote = choice(quotes_list)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # make the connection secure using TLS
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="codeforfun2020@yahoo.com",
                msg=f"Subject:Monday Motivation\n\n{quote}".encode("utf-8")
            )
  ```
