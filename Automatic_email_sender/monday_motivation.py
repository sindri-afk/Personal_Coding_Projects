#nota mitt eigið email hér. 
import datetime as dt
import random as rd
import smtplib

MY_EMAIL = "sindrirafnpython@gmail.com"
PW = "nlkm vwzy evrs buml"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("/Users/sindribjarkason/Desktop/Háksólinn í Reykjavík/Línuleg Algebra m. Tölvunarfræði/Github/Personal_Coding_Projects/Automatic_email_sender/quotes.txt") as file:
        all_quotes = file.readlines()
        number = rd.randint(0, 100)
        correct_quote = rd.choice(all_quotes)


    with smtplib.SMTP("smtp.gmail.com") as connection: 
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PW)
        connection.sendmail(from_addr=MY_EMAIL, 
                        to_addrs="sindribjarka@gmail.com", 
                        msg=f"Subject: Happy Monday Bitch\n\n{correct_quote}")  ## Subject: Money\n\nsome text is crucial for am automatic email so it 


# á eftir að negla því upp í python anywhere
        