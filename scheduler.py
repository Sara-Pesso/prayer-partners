import schedule
import time
from plyer import notification
from email_prayer_buddies import *


def send_notification():
    notification.notify(
    title = "Take A Break!!!",
    timeout = 10
    )

schedule.every().day.at("11:25").do(weekly_prayer_buddies)

while True:
    schedule.run_pending()
