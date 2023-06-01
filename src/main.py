from functools import partial
from getpass import getpass
from multiprocessing import Pool

from rich.console import Console
from rich.table import Table

from biomailer import WorkbookReader, generate_mail, send_mail

# initialize console
c = Console(log_time=False)
c.clear() # clear console screen

c.print("\n  [yellow bold]Welcome to the CKODON Bio Mailer[/ yellow bold]")
c.print("  " + "[yellow bold]_[/ yellow bold]" * 32)

# request name of spreadsheet file
ws_name = c.input("\n  Enter name of spreadsheet file (example.xlsx): ")

c.print("\n[green bold]  How is the data structured on the sheet?[/green bold]")

# show an example of structure
table1 = Table("Name", "Email", "Intended Major", "Bio")
table1.add_row("John Doe", "johndoe@gmail.com", "Aerospace Engineering", "Hello World")

table2 = Table(show_header=False)
table2.add_row("John Doe")
table2.add_row("johndoe@gmail.com")
table2.add_row("Aerospace Engineering")
table2.add_row("Hello world")

c.print("\nOPTION 1 (ONE)", table1)
c.print("\nOPTION 2 (TWO)", table2)

# ask how data is structured in order not to break the reader
data_structure = c.input("\n  Option One (1) or Two (2) 1/2: ")


# initialize reader to fetch data from sheet
try:
    reader = WorkbookReader(ws_name)
except FileNotFoundError:
    c.print("Incorrect file name or path, check your input.")
else:
    if data_structure == "2": # if data is in inappropriate structure
        reader.transpose() # we transpose
    
    # accept sender credentials
    SENDER = c.input("\n  Enter your email (sender): ")
    PASSWORD = getpass("  Enter password: ")

    # fetch data from worksheet
    ws_data = list(reader.fetch_data())
    f_ = ws_data[0]
    c.print("\n  [green bold]First item in spreadsheet is: [/green bold]")
    c.print(f"  Name: {f_[0]}, Email: {f_[1]}, Major: {f_[2]}")

    proceed = c.input("\n  Confirm Y/N_: ").lower()
    c.print() # print empty line
    if proceed == 'y':
        # use multiprocessing to generate mails
        with Pool(5) as pool:
            generated_mails = pool.map(partial(generate_mail, from_=SENDER), ws_data)
        
        # now let's send the mail messages
        send_mail(SENDER, PASSWORD, messages=generated_mails)
    else:
        c.print("\n  [red bold]Aborted![/red bold]")
