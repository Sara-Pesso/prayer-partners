from wins_scheduler import *

if __name__ == "__main__":
    task_name = "SendWeeklyReminders"
    
    if len(sys.argv)>1:
        exe_path = sys.argv[1] 
        arg_path = sys.argv[2] #"E:\prayer-partners\directory.xlsx"
    run_at = datetime.datetime.now() + datetime.timedelta(minutes=1)
     
    create_scheduled_task(task_name, run_at, exe_path, arg_path, 'Send weekly reminders for each day', 2, weekday=None, interval_str='day')