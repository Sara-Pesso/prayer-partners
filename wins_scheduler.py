import datetime
import win32com.client
from pathlib import Path
import sys

def create_scheduled_task(task_name, run_time, exe, arg, description, TR, weekday=None, interval_str=None):
    # Connect to the Task Scheduler service
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()

    # Access the root folder (where tasks are stored by default)
    root_folder = scheduler.GetFolder('\\')

    # Create a new task definition
    task_def = scheduler.NewTask(0)

    # --- Set up the Trigger (when the task runs) ---
    # *** Trigger ***
    # TASK_TRIGGER_TIME (1): Triggers a task at a specific date and time.
    # TASK_TRIGGER_DAILY (2): Triggers a task on a daily schedule, with a specified interval.
    # TASK_TRIGGER_WEEKLY (3): Triggers a task on a weekly schedule.
    # TASK_TRIGGER_MONTHLY (4): Triggers a task on a monthly schedule.
    # TASK_TRIGGER_MONTHLYDOW (5): Triggers a task on a monthly schedule based on the day of the week (e.g., the first Monday of the month).
    # TASK_TRIGGER_EVENT_ON_ID (5) (older API): Used in the older Task Scheduler 1.0 API, generally replaced by event triggers in 2.0.
    # TASK_TRIGGER_EVENT (6): Triggers a task when a specific system event occurs (e.g., from the Windows Event Log).
    # TASK_TRIGGER_REGISTRATION_AT (7): Triggers a task when it is registered or updated.
    # TASK_TRIGGER_IDLE (8): Triggers a task when the system enters an idle state.
    # TASK_TRIGGER_LOGON (9): Triggers a task when a specific user logs on to the computer.
    # TASK_TRIGGER_SESSION_STATE_CHANGE (11): Triggers a task when a terminal server session state changes (e.g., connect, disconnect, lock, unlock). 

    trigger = task_def.Triggers.Create(TR)
    trigger.StartBoundary = run_time.isoformat()

    match TR:
        case 2: #DAILY, on schedule
            interval_dict = {"hour": "PT1H"}
            trigger.Repetition.Interval = interval_dict[interval_str]
            # Set the duration to run indefinitely ("P100Y" for 100 years, effectively indefinite)
            # trigger.Repetition.Duration = "P100Y" 

        case 3: # WEEKLY
            daysofweek_bitmask = {"Sunday":1,
                                  "Monday":2,
                                  "Tuesday":4,
                                  "Wednesday":8,
                                  "Thursday":16,
                                  "Friday":32,
                                  "Saturday":64}
            trigger.DaysOfWeek = daysofweek_bitmask[weekday]
            trigger.WeeksInterval = 1 # Run every week

    # --- Set up the Action (what the task does) ---
    action = task_def.Actions.Create(0)
    action.Path = exe  # Full path to your executable
    action.Arguments = arg  # Path to the script you want to run

    # --- Set up Task Settings and Registration Info ---
    task_def.RegistrationInfo.Description = description
    task_def.Settings.Enabled = True
    task_def.Settings.StopIfGoingOnBatteries = False

    # --- Register the task ---
    TASK_CREATE_OR_UPDATE = 6
    TASK_LOGON_TYPE_INTERACTIVE_TOKEN = 3  #(runs when the user is logged in)

    root_folder.RegisterTaskDefinition(
        task_name,
        task_def,
        TASK_CREATE_OR_UPDATE,
        '', # User (empty for current user, often username is needed)
        '', # Password (empty if no password required for login type)
        TASK_LOGON_TYPE_INTERACTIVE_TOKEN # Run only when user is logged on
    )

    print(f"Task '{task_name}' created successfully.")

    ## Add task name to txt list, so it can be located and deleted later if desired
    created_task_list = Path("./created_task_list.txt")
    if not created_task_list.exists():
        with open(created_task_list, 'w') as file:
            file.write(task_name + "\n")

    else:
        with open(created_task_list, "a") as file:
            file.write(task_name + "\n")

def delete_scheduled_task(task_name):
    try:
        # Connect to the Task Scheduler service
        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        
        # Get the specified task folder
        root_folder = scheduler.GetFolder('\\')
        
        # Delete the task
        # The second argument (0 in this case) represents flags; 
        # 0 means no flags are used for this operation.
        root_folder.DeleteTask(task_name, 0)
        
        print(f"Task '{task_name}' successfully deleted.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Could not delete task '{task_name}'. Ensure the task name and folder path are correct and you have sufficient permissions.")

# delete_scheduled_task("PrayerBuddyEmailer")

