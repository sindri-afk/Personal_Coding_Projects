## Hér ætla ég að skoða hvernig ég nota SMTP og datetime Module: 
## emailinn: sindrirafnpython@gmail.com
## pw: sVVSLgT&V1#hpYaKR4us
## App_password = "nlkm vwzy evrs buml"
import smtplib

# easy way, 1:
'''my_email = "sindrirafnpython@gmail.com"
pw = "nlkm vwzy evrs buml"
connection = smtplib.SMTP("smtp.gmail.com") ## creating an object, og specify-a locationið sem er smtp.gmail.com
connection.starttls() # TLS stendur fyrir transport layer security, 
# "It's a way of securing our connection with our email server", if someone intercepts our email it will be encrypted.
connection.login(user=my_email, password=pw)
connection.sendmail(from_addr=my_email, 
                    to_addrs="sindribjarka@gmail.com", 
                    msg="Subject: Happy Monday Bitch\n\nThis is the body of my email.")  ## Subject: Money\n\nsome text is crucial for am automatic email so it 
                    # doesn't only have a body but also a subject.
connection.close()'''

# a likkle nicer way: 
my_email = "sindrirafnpython@gmail.com"
pw = "nlkm vwzy evrs buml"
with smtplib.SMTP("smtp.gmail.com") as connection: 
    connection.starttls()
    connection.login(user=my_email, password=pw)
    connection.sendmail(from_addr=my_email, 
                    to_addrs="sindribjarka@gmail.com", 
                    msg="Subject: Happy Monday Bitch\n\nThis is the body of my email.")  ## Subject: Money\n\nsome text is crucial for am automatic email so it 
    connection.close()