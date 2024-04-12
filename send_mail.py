import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd


def send_email_(sender_email, sender_password, receiver_email, subject, body, attachment_path_body,
                attachment_path_pdf):
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach body to email
    message.attach(MIMEText(body, "html"))
    try:
        # Open the file to be sent
        with open(attachment_path_body, "rb") as attachment:
            # Read Excel file
            df = pd.read_excel(attachment)

            # Convert DataFrame to HTML table
            html_table = df.to_html(index=False)

        # Add HTML table as MIMEText
        attachment_html = MIMEText(html_table, "html")
    except Exception as ex:
        attachment_html = f"<p>Đã xảy ra lỗi khi đọc tệp: {ex}</p>"

    message.attach(attachment_html)
    # Attach PDF file
    with open(attachment_path_pdf, "rb") as file:
        part = MIMEBase("application", "pdf")
        part.set_payload(file.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_path_pdf}",
    )

    # Attach the attachment to the message
    message.attach(part)

    # Log in to SMTP server and send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        res_login = server.login(sender_email, sender_password)
        print(res_login)
        res_send = server.sendmail(sender_email, receiver_email, message.as_string())
        print(res_send)


class Mail:
    def send_mail(self):
        # Example usage
        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")
        receiver_email = os.getenv("RECEIVER_EMAIL")
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
        # Chuyển subject thành "Báo cáo" theo ngày giờ hiện tại
        subject = f"Báo cáo {current_datetime}"
        body = ""
        attachment_path_body = "/home/tiennguyen/Desktop/research/tool/fmarket_report_send_mail/bao_cao.xlsx"
        attachment_path_pdf = "/home/tiennguyen/Desktop/research/tool/fmarket_report_send_mail/bao_cao.pdf"

        send_email_(sender_email, sender_password, receiver_email, subject, body, attachment_path_body,
                    attachment_path_pdf)
