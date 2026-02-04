import datetime
import win32com.client

def create_scheduled_task(task_name, run_time):
    # Connect to the Task Scheduler service
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()

    # Access the root folder (where tasks are stored by default)
    root_folder = scheduler.GetFolder('\\')

    # Create a new task definition
    task_def = scheduler.NewTask(0)

    # --- Set up the Trigger (when the task runs) ---
#  *** Trigger (Weekly) ***
    TR_WEEKLY = 1 # Task trigger type for weekly = 3
    trigger = task_def.Triggers.Create(TR_WEEKLY)
    trigger.StartBoundary = run_time.isoformat()
    # trigger.DaysOfWeek = 1
    # trigger.WeeksInterval = 1 # Run every week

    # --- Set up the Action (what the task does) ---
    # For an executable action, use type 0 (TASK_ACTION_EXEC)
    ACTION_TYPE_EXEC = 0
    action = task_def.Actions.Create(ACTION_TYPE_EXEC)
    action.Path = "E:\prayer-partners\dist\email_prayer_buddies.exe" # Full path to your executable
    # action.Arguments = f'"{script_path}"' # Path to the script you want to run

    # --- Set up Task Settings and Registration Info ---
    task_def.RegistrationInfo.Description = 'Prayer Buddy Random Emailer'
    task_def.Settings.Enabled = True
    task_def.Settings.StopIfGoingOnBatteries = False

    # --- Register the task ---
    # TASK_CREATE_OR_UPDATE = 6
    # TASK_LOGON_TYPE_INTERACTIVE_TOKEN = 3 (runs when the user is logged in)
    TASK_CREATE_OR_UPDATE = 6
    TASK_LOGON_TYPE_INTERACTIVE_TOKEN = 3 

    root_folder.RegisterTaskDefinition(
        task_name,
        task_def,
        TASK_CREATE_OR_UPDATE,
        '', # User (empty for current user, often username is needed)
        '', # Password (empty if no password required for login type)
        TASK_LOGON_TYPE_INTERACTIVE_TOKEN # Run only when user is logged on
    )

    print(f"Task '{task_name}' created successfully.")

if __name__ == "__main__":
    task_name = "PrayerBuddyEmailer"
    # script_to_run = r"E:\prayer-partners\email_prayer_buddies.py"
    run_at = datetime.datetime.now() + datetime.timedelta(minutes=1)

    create_scheduled_task(task_name, run_at)
