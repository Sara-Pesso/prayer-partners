# import win32com.client
# import datetime

# def create_weekly_task(task_name, script_path, run_time_hour, run_time_minute, days_of_week_mask, days_interval=1):
#     """
#     Creates a weekly scheduled task using win32com.
    
#     :param task_name: Name for the scheduled task.
#     :param script_path: Full path to the Python script to run.
#     :param run_time_hour: Hour of the day to run (0-23).
#     :param run_time_minute: Minute of the hour to run (0-59).
#     :param days_of_week_mask: A bitmask of the days of the week (e.g., 1 for Sunday, 2 for Monday, 64 for Saturday. 
#                               To run on Monday and Wednesday, use 2 | 8 = 10).
#     :param days_interval: The interval between weeks (e.g., 1 for every week, 2 for every two weeks).
#     """
#     scheduler = win32com.client.Dispatch('Schedule.Service')
#     scheduler.Connect()
#     root_folder = scheduler.GetFolder('\\') # Access the root folder

#     # Task Definition
#     task_def = scheduler.NewTask(0)
    
#     # Registration Info
#     reg_info = task_def.RegistrationInfo
#     reg_info.Description = f'Runs the script {script_path} weekly.'

#     # Principal (Security Context)
#     principal = task_def.Principal
#     principal.LogonType = 3 # TASK_LOGON_S4U (Service for User), common for running without user logged on
#     principal.RunLevel = 1 # TASK_RUNLEVEL_LSA (Run with highest privileges)

#     # Settings
#     settings = task_def.Settings
#     settings.Enabled = True
#     settings.StopIfGoingOnBatteries = False
#     settings.DisallowStartIfOnBatteries = False

#     # Trigger - Set up a Weekly Trigger
#     TRADITIONAL_WEEKLY_TRIGGER = 4 # TASK_TRIGGER_WEEKLY
#     trigger = task_def.Triggers.Create(TRADITIONAL_WEEKLY_TRIGGER)
#     trigger.StartBoundary = datetime.datetime.now().isoformat()
#     trigger.DaysOfWeek = days_of_week_mask
#     trigger.Interval = days_interval

#     # Action - Define what to run
#     EXEC_ACTION = 0 # TASK_ACTION_EXEC
#     action = task_def.Actions.Create(EXEC_ACTION)
#     action.Path = "C:\\path\\to\\your\\python.exe" # Full path to your Python executable
#     action.Arguments = f'"{script_path}"' # Full path to your Python script
#     action.WorkingDirectory = "C:\\path\\to\\your\\script_folder" # Optional: set working directory

#     # Register the task
#     TASK_CREATE_OR_UPDATE = 6 # Create or update the task
#     TASK_LOGON_TYPE_S4U = 3 # Security Logon Type
#     root_folder.RegisterTaskDefinition(
#         task_name,
#         task_def,
#         TASK_CREATE_OR_UPDATE,
#         '', # User (empty for S4U logon type to use system/service account)
#         '', # Password
#         TASK_LOGON_TYPE_S4U
#     )

#     print(f"Task '{task_name}' scheduled successfully for weekly execution.")

# # Example usage: Schedule a script to run every Monday and Wednesday at 9:30 AM
# # Sunday=1, Monday=2, Tuesday=4, Wednesday=8, Thursday=16, Friday=32, Saturday=64
# # Mask for Monday and Wednesday is 2 + 8 = 10
# create_weekly_task(
#     task_name="MyWeeklyPythonTask",
#     script_path="C:\\Users\\YourUser\\Scripts\\my_script.py",
#     run_time_hour=9,
#     run_time_minute=30,
#     days_of_week_mask=10, 
#     days_interval=1
# )


import win32com.client
import datetime

# 1. Connect to Task Service
scheduler = win32com.client.Dispatch('Schedule.Service')
root_folder = scheduler.GetFolder('\\')

# 2. Create Task Definition
task_def = scheduler.NewTask(0)
reg_info = task_def.RegistrationInfo
reg_info.Description = 'Run weekly, or immediately if missed'

# 3. Define Weekly Trigger
trigger = task_def.Triggers.Create(2) # 2 = TASK_TRIGGER_WEEKLY
trigger.DaysOfWeek = 1 # e.g., Sunday
# Set StartBoundary to a past time for "ASAP"
trigger.StartBoundary = (datetime.datetime.now() - datetime.timedelta(minutes=1)).isoformat()
trigger.RunIfStartedAfterTimeout = True # Run if missed [5]

# 4. Define Action
action = task_def.Actions.Create(0) # 0 = TASK_ACTION_EXEC
action.Path = r'C:\Path\To\Python.exe'
action.Arguments = r'C:\Path\To\Script.py'

# 5. Register Task
root_folder.RegisterTaskDefinition(
    'MyWeeklyTask',
    task_def,
    6, # TASK_CREATE_OR_UPDATE
    None, # User
    None, # Password
    3 # TASK_LOGON_NONE
)
