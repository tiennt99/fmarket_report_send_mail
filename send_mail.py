import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd


def send_email_(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach body to email
    message.attach(MIMEText(body, "html"))
    try:
        # Open the file to be sent
        with open(attachment_path, "rb") as attachment:
            # Read Excel file
            df = pd.read_excel(attachment)

            # Convert DataFrame to HTML table
            html_table = df.to_html(index=False)

        # Add HTML table as MIMEText
        attachment_html = MIMEText(html_table, "html")
    except Exception as ex:
        attachment_html = f"<p>Đã xảy ra lỗi khi đọc tệp: {ex}</p>"
        
    message.attach(attachment_html)
    # Attach Excel file
    with open(attachment_path, "rb") as file:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(file.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_path}",
    )

    # Attach the attachment to the message
    message.attach(part)

    # Log in to SMTP server and send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())


class Mail:
    def send_mail(self):
        # Example usage
        sender_email = "tiennhshopee@gmail.com"
        sender_password = "yaxn yrwa bkbq rlvh"
        receiver_email = "openupmta99@gmail.com"
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
        # Chuyển subject thành "Báo cáo" theo ngày giờ hiện tại
        subject = f"Báo cáo {current_datetime}"
        body = ""
        attachment_path = "/home/tiennguyen/Desktop/research/ck/tool/bao_cao.xlsx"

        send_email_(sender_email, sender_password, receiver_email, subject, body, attachment_path)
