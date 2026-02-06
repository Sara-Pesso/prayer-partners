from directory import *
from emailer import *
from datetime import datetime, timedelta, date
from wins_scheduler import create_scheduled_task, delete_scheduled_task

def schedule_weekly_reminder(task_name, exe, arg, description, TR, dayofweek):
    day_to_int = {"Sunday":6,
                    "Monday":0,
                    "Tuesday":1,
                    "Wednesday":2,
                    "Thursday":3,
                    "Friday":4,
                    "Saturday":5}
    
    today = datetime.now()
    days_until_first_reminder = today - day_to_int[dayofweek]
    
    datetime_send_first_reminder = today + timedelta(days=days_until_first_reminder)

    create_scheduled_task(task_name, datetime_send_first_reminder, exe, arg, description, TR, weekday=dayofweek)


# Create Weekly/etc. Reminders 

# Remove Reminders if no longer needed