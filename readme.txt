2/5/2026
To see the Prayer Buddy Weekly Emailer function:

pyinstaller --onefile -w 'E:\prayer-partners\email_prayer_buddies.py'
pyinstaller --onefile -w 'E:\prayer-partners\schedule_prayer_buddies.py'
.\dist\schedule_prayer_buddies.exe "E:\prayer-partners\dist\email_prayer_buddies.exe" "E:\prayer-partners\directory.xlsx"

In current form, this sets up a task to email the random partners in 1 minute.

For the #prayer-request function:

pyinstaller --onefile -w 'E:\prayer-partners\mass_notifications.py'
pyinstaller --onefile -w 'E:\prayer-partners\schedule_prayer_request_check.py'
.\dist\schedule_prayer_request_check.exe "E:\prayer-partners\dist\mass_notifications.exe" "E:\prayer-partners\directory.xlsx"
