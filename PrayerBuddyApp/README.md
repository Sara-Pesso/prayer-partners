## Basic Functionality

Welcome to the Prayer Buddy App!

This app has 3 main functions:
1. Randomly assigns prayer buddy partners each Sunday (in the case of an odd number of participants there is one group of 3 made) and emails to inform the groups
2. Checks for new weekly reminders and then sends those reminders out weekly on their specified day (examples: send out a reminder for Friday meeting on Thursdays, send out practice notice on Sundays, etc.)
3. Allows users to send anonymous (or not!) prayer requests to everyone on the email distribution. 

## User set up

1. Download this repo to your own computer: [Prayer Buddy App Repo](https://github.com/Sara-Pesso/prayer-partners/tree/Prayer-App-Distro)
2. Determine what G-Mail address (referred to as the 'authorized user')you want to control the app from
    - a. Set up an app password for this G-Mail-- make sure to write it down!
    - b. Update the config.toml (in \path\to\your\repo\dist\config.toml) using your information
    - c. In G-Mail, make 2 new Labels, named exactly: ```Prayer Requests``` and ```Weekly Reminders```.
3. Update the directory.xlsx (located in \path\to\your\repo\directory.xslx) to include emails for everyone in your club

## Setting up the Windows Scheduler Functions

This app uses the G-Mail API and the Windows Task Scheduler to send emails from your authorized email address. The app is set up to make this process as simple as possible. 
The GUI (the actual app you, the user, interface with-- which can be opened by double-clicking on \path\to\your\repo\gui.exe).

Here's what each of those buttons do:

1. Recommended: Open the Windows Task Scheduler, so you can see the apps tasks get scheduled for execution by your computer! 
2. The first 5 textboxes are pulled directly from your config.toml. Make sure these values are correct!
 - If these values are *not* correct, update the relevant textboxes. 
 - Note: Probably the "Email Username" and "Authorized User" boxes will be the same.
 - Once the values are correct, click the **Update** button. This updates the config.toml to the correct values so the app is using the correct information.
 - Alternative method: you can close the app, change the config.toml manually, save it, and then reopen the app.

**WHEN INITIALLY SETTING UP YOUR APP, PRESS ALL THIS BUTTONS!** This adds the automation tasks to you Windows Task Scheduler, so it will happen automatically every week after!
3. **Redraw Weekly Prayer Buddies**: This button will redraw and send out new prayer buddies for the week whenever you press it. If not pressed, it will send out on Sunday afternoons. 
4. **Send Today's Reminders**: This will first check the G-Mail inbox for new reminders, then add the messages to the list of reminders to be sent out for the specified day of the week. Then, it immediately sends out the reminders cached for the current day of the week. To set a reminder there are 2 options:
 - a. Email the authorized G-Mail account an email exactly how you want your email to appear. Then, use the hashtag ```#weekly-reminder``` and ```#Thursday``` to, for example, send that reminder email out each Thursday. These hashtags are case sensitive!
 - b. (Not recommended). You can manually add the email in the corresponding \path\to\your\repo\dist\week_reminder_json\DAY_OF_THE_WEEK.json
 - c. The repo and files above are also how you can delete a message so it stops being sent, if desired. 

Once the emails are cached to be sent out, they are moved to the Weekly Reminder Label in the G-Mail account. Once this button is pressed, a daily email search for new reminders and a daily task to send each weekday's reminders are sent out that day are created. This will automate the process for subsequent weeks.

5. **Check for Prayer Requests**: Works similarly to the previous button. Anyone whose email is in your directory.xlsx can email the authorized account with a prayer request. They simply write the email as they wish for it to appear, then add the hashtag ```#prayer-request``` (case sensitive!). The message will be anonymous unless they add their name to the email. These will be automatically sent out each hour and the original email moved to the G-Mail Prayer Request Label. Each prayer request is only sent once (not weekly). The will be a Windows Task Scheduler task created that checks the G-Mail inbox and does this hourly. 

## Check set up
Go to the Windows Task Scheduler. On the lefthand panel, select Task Scheduler Library. You should see (among others) the tasks you just created:

- PrayerBuddyEmailer
- CheckEmailForNewReminders
- SendWeeklyReminders
- PrayerRequestCheck

You can also see the intervals at which they are scheduled!
