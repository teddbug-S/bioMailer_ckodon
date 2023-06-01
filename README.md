# BIOMAILER - CKODON
A python program that distributes the revised bio to all
ckodonites through the e-mail.
It reads student data from a spreadsheet file provided via 
user input.

## Usage
First you need python installed on your system, a version of 3.5 going up.
i.e Python >= 3.5.
After installing python you need to install the third-party packages or 
dependencies of the program, this sets everything up for running of the 
program.

See below for instructions.

- Installing dependencies
  Change directory or `cd` into the `BioMailer_Ckodon` directory
  by executing `cd BioMailer_Ckodon` and execute the following command to 
  install the requirements `pip install -r requirements.txt`.

- Launching the program
  With everything in place, change directory into the `src` folder
  by `cd src`.
  Execute the program by running the command the following command:
  On Linux/MacOS `python3 main.py`
  On Windows `python main.py`
  this will launch the program.

### Understanding the program

#### Data Entry
  When you first launch the program, you will prompted to provide or enter
  the full or relative file path or location of your spreadsheet file e.g 
  `My documents/students_data.xlsx` and hit the `enter` key.

  In the `files` subfolder which is in the application directory contains
  two files (initially); they both have the same data but with different arrangements.
  `ckodon.xlsx` has the perfectly distributed arrangement whilst `ckodon_2.xlsx` has
  the one-column arrangement. So you can use these example files for test of the app,
  by entering `files/ckodon.xlsx` or `files/ckodon_2.xlsx`.

  Make sure you provide the correct location of the file otherwise there will
  be an error and you will have to launch the program again.

  Now you need to tell the program the style of arrangement of data in the
  spreadsheet, I don't know whether everything has been placed in one column
  or perfectly distributed spanning many columns and rows.

  The program will provide you with options, if it is the first arrangement (e.i 
  in one column) you enter `1` in the prompt else if it is the latter one, the
  perfectly distributed one, you enter `2` and also hit `enter`.


#### Email Client Authorization (Gmail - Sender)
  You will need to authorize the email account that will be used in sending
  the mails.
  The program will prompt you to enter the email address e.g `example@gmail.com`
  After entering you enter the password also.

  Now the problem is simple, Google has disabled a setting called `Less Secure Apps` which
  enables custom applications like this one to access an email account.
  This makes it impossible to use your current gmail login creds to authorize, leaving
  `Application Passwords` as the only secure way out.

  These work by creating special login creds for each application you want to use your mail
  with (in this case, this application so 1).
  To create one, log on to [My Google Account](!myaccount.google.com), select `Security` on 
  the left pane, navigate to the `How to sign in` section and click
  on the two-step verification option, continue to enable it.
  After enabling this, you need to be in the two-step verification menu if not click on
  two-step verification option again from the `How to sign in` page to get there.

  In the menu scroll down till you find `App Password`, click on it,
  enter `BioMailer Ckodon` as name of the application to generate the password.


Back to the application, use your email address and the generated password to authorize
the app.
With everything in place, hit `enter` to continue.
The first record of data from the spreadsheet will be displayed to you, if it is 
accurate, enter `y` or `Y` and hit `enter` to proceed.

The application will show progress when sending mails, but when an error message such as
`Connection failed`; you check your internet connection,
`Unable to authenticate`; you check the password you pasted whether it matches your generated
password.

Have a good day!



  