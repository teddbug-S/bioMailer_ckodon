import socket
import smtplib
from time import sleep

from rich.console import Console

c = Console(log_time=False, log_path=False)

def send_mail(user, password, messages):
    """Initiate an SMTP connection authenticated with credentials to send mail"""
    # try to initiate an SSL connection
    try:
        with c.status("  [hot_pink]Getting ready to send message!", spinner='runner') as status:
            sleep(2.5)
            c.log("\n  [purple bold]Initiating SMTP ⚡⚡[/purple bold]")
            sleep(1.5)
            with smtplib.SMTP_SSL('smtp.gmail.com') as google_smtp: # ssl smtp
                
                # update for authentication
                status.update(
                    status="[bold plum4] Authenticating account 🔑",
                    spinner='bouncingBall',
                    spinner_style="green")
                sleep(1.4)
                # try to authenticate
                google_smtp.login(user, password) # login
                c.log("  [cyan2 bold]Authentication successful 👊✅[/cyan2 bold]")

                # update after successful authentication
                count = len(messages)
                status.update(
                    status=f"[orange3] Sending ({count}) messages 💨. [/orange3]",
                    spinner="pong",
                    spinner_style="yellow"
                )
                sleep(2.50)
                # now send each message
                nc = 1
                for message in messages:
                    # update progress
                    status.update(
                        status=f"[orange3] Sending 💨 ({nc}) of ({count}) messages. [/orange3]"   
                    )
                    # send mail
                    google_smtp.send_message(message)
                    nc += 1
                c.log(f"[light_green blink bold] ({count}) messages sent succesfully.✅[/light_green blink bold]")

    # catch some potential exceptions
    except (socket.gaierror, smtplib.SMTPConnectError):
        c.print("[red bold]\n  Connection failed. Check your internet connection![/red bold]")
    except smtplib.SMTPAuthenticationError:
        c.print("[red bold]\n  Unable to authenticate, check your credentials.[/red bold]")
