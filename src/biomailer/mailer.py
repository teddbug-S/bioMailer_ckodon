from email.message import EmailMessage


html = """
<!DOCTYPE html>
<html lang="en">
<body>
  <header>
    <div>
      <h1>Revised Bio - CKODON</h1>
    </div>
  </header>
  <section>
    <div>
      <h2>{name}</h2>
      <p>{major} - Major</p>
    </div>
    <div>
      <h2>Bio</h2>
      <div>
        <p>{bio}</p>
      </div>
    </div>
  </section>
  <footer>
    <p>CKODON 2023 &copy; All Rights Reserved</p>
  </footer>
</body>
</html>"""


def construct_message_body(name, major, bio):
    """Construct an HTML message body"""
    text_content = f"""
    Revised Bio  -  CKODON
    ======================
            {name}
            {major} - Major

    Bio
    ===
    {bio}
    """
    
    return html.format(name=name, major=major, bio=bio), text_content


def build_email_message(from_, to_, html, text):
    """Build an EmailMessage object"""

    message = EmailMessage()
    message["Subject"] = "Your Revised Bio"
    message["To"] = to_
    message["From"] = from_
    
    # set body content
    message.set_content(text)
    message.add_alternative(html, subtype="html")

    return message


def generate_mail(record, from_):
    """Generate an email message for each record ready for sending"""
    data = {
                'name': record[0], 'to_': record[1],
                'major': record[2], 'bio': record[3],
                'from_': from_
            }
    # get body content and build an email message
    content_body = construct_message_body(data.get('name'), data.get('major'), data.get('bio'))
    mail = build_email_message(data.get('from_'), data.get('to_'), *content_body)
    
    return mail
