import datetime as dt
import random
import smtplib

my_email = "juanzopyhontest@gmail.com"
password = "9RxalRa@jT0o9aMe"

# add port number 587,
# Make sure you've enabled less secure apps if you are sending from a Gmail account.
# (Refer to the video in the next lesson for steps).activate less secure app access in Google Account +
# Try to go through the Gmail Captcha here while logged in to the Gmail account:
# https://accounts.google.com/DisplayUnlockCaptcha

now = dt.datetime.now()
weekday = dt.datetime.weekday(now)
print(weekday)

f = open("quotes.txt", "r")
quotes_list = f.readlines()
random_quote = random.choice(quotes_list)

if weekday == 5:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="juanzopythontest@yahoo.com",
                            msg=f"Subject:Quote van de dag\n\n{random_quote}"
                            )