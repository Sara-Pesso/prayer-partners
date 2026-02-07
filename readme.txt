2/5/2026
To see the Prayer Buddy Weekly Emailer function:

pyinstaller --onefile -w 'E:\prayer-partners\email_prayer_buddies.py'
pyinstaller --onefile -w 'E:\prayer-partners\schedule_prayer_buddies.py'
.\dist\schedule_prayer_buddies.exe "E:\prayer-partners\dist\email_prayer_buddies.exe" "E:\prayer-partners\directory.xlsx"

In current form, this sets up a task to email the random partners in 1 minute.

For the #prayer-request function: verified 2/6/206 1843

pyinstaller --onefile -w 'E:\prayer-partners\prayer_requester.py'
pyinstaller --onefile -w 'E:\prayer-partners\schedule_prayer_request_check.py'
.\dist\schedule_prayer_request_check.exe "E:\prayer-partners\dist\prayer_requester.exe" "E:\prayer-partners\directory.xlsx"

Creating weekly reminders:

pyinstaller --onefile -w 'E:\prayer-partners\weekly_reminders.py'
pyinstaller --onefile -w 'E:\prayer-partners\schedule_weekly_reminders.py'
.\dist\schedule_weekly_reminders.exe "E:\prayer-partners\dist\weekly_reminders.exe" "E:\prayer-partners\directory.xlsx" "CustomWeeklyReminder" "Friday" "reminder email subject" "reminder email content"