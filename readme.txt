2/5/2026
To se the Prayer Partner Weekly Emailer function:

pyinstaller --onefile -w 'E:\prayer-partners\email_prayer_buddies.py'
pyinstaller --onefile -w 'E:\prayer-partners\wins_scheduler.py'
.\dist\wins_scheduler.exe "E:\prayer-partners\dist\email_prayer_buddies.exe" "E:\prayer-partners\directory.xlsx"

In current form, this sets up a task to email the random partners in 1 minute. 
