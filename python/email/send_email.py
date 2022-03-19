import smtplib
from config import password

# my_email = "xulan20907@gmail.com"
# print(password)
# # Create an object from SMTP class
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# # make the connection secure using TLS
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="xulan20907@gmail.com",
#     msg="Subject:Hello\n\nThis is the body of my email."
# )
# connection.close()


# Only sent to 
def gmail_to(from_addrs, password, to_addrs, message_subject, message_text):
    # Create an object from SMTP class
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    # make the connection secure using TLS
    connection.starttls()
    connection.login(user=from_addrs, password=password)
    connection.sendmail(
        from_addr=from_addrs,
        to_addrs=to_addrs,
        msg=f"Subject:{message_subject}\n\n{message_text}"
    )
    connection.close()

# Show how to call function gmail_to
from_addrs = "xulan20907@gmail.com"
to_addrs = "lxu@instructors.2u.com"
message_subject = "Hello"
message_text = "This test again"

gmail_to(
    from_addrs=from_addrs, 
    password=password,
    to_addrs=to_addrs, 
    message_subject=message_subject, 
    message_text=message_text
)


# To, CC and BCC
def gmail_to_cc(
        from_addrs, 
        password, 
        to_addrs, 
        cc_addrs, 
        bcc_addrs, 
        message_subject, 
        message_text):

    message = "From: %s\r\n" % from_addrs \
            + "To: %s\r\n" % to_addrs \
            + "CC: %s\r\n" % ",".join(cc_addrs) \
            + "Subject: %s\r\n" % message_subject \
            + "\r\n" \
            + message_text
    
    to_addrs = [to_addrs] + cc_addrs + bcc_addrs

    # Create an object from SMTP class
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    # make the connection secure using TLS
    connection.starttls()
    connection.login(user=from_addrs, password=password)
    connection.sendmail(
        from_addr=from_addrs,
        to_addrs=to_addrs,
        msg=message
    )
    connection.close()


from_addrs = "xulan20907@gmail.com"
to_addrs = "xulan20907@gmail.com"
cc_addrs = ["codeforfun2020@gmail.com", "lxu@instructors.2u.com"]
bcc_addrs = ["simonxu102316@gmail.com"]
message_subject = "Hello"
message_text = "This is test"

gmail_to_cc(
    from_addrs=from_addrs,
    password=password,
    to_addrs=to_addrs,
    cc_addrs=cc_addrs,
    bcc_addrs=bcc_addrs,
    message_subject=message_subject,
    message_text=message_text
)