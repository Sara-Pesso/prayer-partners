import smtplib
import ssl
from email.message import EmailMessage
from directory import *
import win32com

# Email account details
USERNAME = "pessognellisa20@gmail.com"
PASSWORD = "axyf rity yzjb hcdo" # Use an App Password

def email_composer(message_content, message_subject, username, distro_xlsx):
    names, name_to_email, email_distro = get_directory(distro_xlsx) #"E:\prayer-partners\directory.xlsx"
    for email_address in email_distro:
        # Create the EmailMessage object
        msg = EmailMessage()
        msg.set_content(message_content)
        msg['Subject'] = message_subject #"Prayer Reminder: " + date.today().strftime("%Y-%m-%d")
        msg['From'] = username
        msg['To'] = email_address #receiver email

        # Define the SMTP server and port (for Gmail with implicit TLS/SSL)
        smtp_server = "smtp.gmail.com"
        port = 465  # For SSL

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to the server and send the email
        try:
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(USERNAME, PASSWORD)
                server.send_message(msg)
            print("Email sent successfully!")
        except smtplib.SMTPException as e:
            print(f"Error: {e}")




def create_scheduled_task(task_name, run_time, exe, arg, description, TR, weekday=None):
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