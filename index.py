import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# set up the SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "kanijsworna29@gmail.com"
sender_password = "hognhzidgcrbxbmo"
recipient_email = "niweha1478@rockdian.com"

# set up the email message
msg = MIMEMultipart('alternative')
msg['Subject'] = "Test Email with HTML Table"
msg['From'] = sender_email
msg['To'] = recipient_email

# create the HTML table
table_data = [['Name', 'Age', 'Gender'], ['John', '25', 'Male'], ['Jane', '30', 'Female'], ['Bob', '40', 'Male']]
table_html = "<table><tr>{}</tr>{}</table>".format(
    "".join(["<th>{}</th>".format(header) for header in table_data[0]]),
    "".join(["<tr>{}</tr>".format("".join(["<td>{}</td>".format(cell) for cell in row])) for row in table_data[1:]])
)

# attach the HTML table to the email message
html = MIMEText(table_html, 'html')
msg.attach(html)

# send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())

print('Email successfully sent!')