from datetime import datetime
import pandas # too read csv files.
import random
import smtplib
today = datetime.now()
today_tuple = (today.month, today.day)
MY_EMAIL = "sindrirafnpython@gmail.com"
MY_PW = "nlkm vwzy evrs buml"


data = pandas.read_csv("birthdays.csv")

# create a dict comprehendsion
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows() }
# check if today matches a birthday:
if today_tuple in birthdays_dict:
    birthday_boy_or_girl = birthdays_dict[today_tuple]

    file_path = f"/Users/sindribjarkason/Desktop/Háksólinn í Reykjavík/Línuleg Algebra m. Tölvunarfræði/Github/Personal_Coding_Projects/Automatic_email_sender/birthday_paragraph{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_boy_or_girl["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PW)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=birthday_boy_or_girl["email"],
            msg=f"Subject: Happy Birthday\n\n{contents}"
            )
   