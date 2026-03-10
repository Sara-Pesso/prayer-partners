from wins_scheduler import *
if __name__ == "__main__":
    task_name = "PrayerBuddyEmailer"
    
    if len(sys.argv)>1:
        exe_path = sys.argv[1] #= "E:\prayer-partners\dist\email_prayer_buddies.exe"
        arg_path = sys.argv[2] #"E:\prayer-partners\directory.xlsx"
    run_at = datetime.datetime.now() + datetime.timedelta(minutes=1)
     
    create_scheduled_task(task_name, run_at, exe_path, arg_path, 'Prayer Buddy Random Emailer', 3, weekday="Sunday", interval_str=None)

