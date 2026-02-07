from wins_scheduler import *
from weekly_reminders import *

if __name__ == "__main__":
    task_name = "WeeklyReminderSender"
    
    if len(sys.argv)>1:
        exe_path = sys.argv[1] 
        arg_path = sys.argv[2] #"E:\prayer-partners\directory.xlsx"
    run_at = datetime.datetime.now() + datetime.timedelta(minutes=1)
     
    subject,content,dayofweek = check_for_weekly_reminders()
    create_scheduled_task(task_name, run_at, exe_path, arg_path, 'Check for weekly reminders', 2, weekday=None, interval_str=None)

