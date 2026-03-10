2/5/2026
To see the Prayer Buddy Weekly Emailer function: verified 2/13/2026 2238

pyinstaller --onefile -w 'E:\prayer-partners\email_prayer_buddies.py'
pyinstaller --onefile -w 'E:\prayer-partners\schedule_prayer_buddies.py'
.\dist\schedule_prayer_buddies.exe "E:\prayer-partners\dist\email_prayer_buddies.exe" "E:\prayer-partners\directory.xlsx"

In current form, this sets up a task to email the random partners in 1 minute.

For the #prayer-request function: verified 2/13/2026 2255

pyinstaller --onefile -w 'E:\prayer-partners\prayer_requester.py'
pyinstaller --onefile -w 'E:\prayer-partners\schedule_prayer_request_check.py'
.\dist\schedule_prayer_request_check.exe "E:\prayer-partners\dist\prayer_requester.exe" "E:\prayer-partners\directory.xlsx"


Creating/scheduling a task to regularly (hourly) look for new weekly reminders the authorized user sent to the email inbox. 
- Regularly (hourly) searches for #weekly-reminder
- Parse weekday from #Weekday
- Add weekly reminder to weekday.json

pyinstaller --onefile -w 'E:\prayer-partners\weekly_reminders.py' #verified 2/13/2026 2256
pyinstaller --onefile -w 'E:\prayer-partners\schedule_weekly_reminder_search.py'#verified 2/13/2026 2256
.\dist\schedule_weekly_reminder_search.exe "E:\prayer-partners\dist\weekly_reminders.exe" "E:\prayer-partners\directory.xlsx" ## verified 2/13/2026 2306

Send out weekly reminders, daily depending on the day

pyinstaller --onefile -w 'E:\prayer-partners\email_weekly_reminders.py'
pyinstaller --onefile -w 'E:\prayer-partners\schedule_weekly_reminder_sender.py'
.\dist\schedule_weekly_reminder_sender.exe "E:\prayer-partners\dist\email_weekly_reminders.exe" "E:\prayer-partners\directory.py"

To build locally run:
pyinstaller --onefile -w 'E:\prayer-partners\email_prayer_buddies.py'; pyinstaller --onefile -w 'E:\prayer-partners\schedule_prayer_buddies.py'; pyinstaller --onefile -w 'E:\prayer-partners\prayer_requester.py'; pyinstaller --onefile -w 'E:\prayer-partners\schedule_prayer_request_check.py'; pyinstaller --onefile -w 'E:\prayer-partners\weekly_reminders.py';pyinstaller --onefile -w 'E:\prayer-partners\schedule_weekly_reminder_search.py';pyinstaller --onefile -w 'E:\prayer-partners\email_weekly_reminders.py'; pyinstaller --onefile -w 'E:\prayer-partners\gui.py' 