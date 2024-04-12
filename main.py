from download_file import Download
from login import Login
from send_mail import Mail

def main():
    token = Login().get_token()
    download_file_xls = Download().download_file_xls(token)
    download_file_xls = Download().download_file_pdf(token)
    send_mail = Mail().send_mail()

if __name__ == "__main__":
    main()