sudo crontab -l
sudo crontab -e
0 20 * * * /home/tiennguyen/anaconda3/envs/Python37/bin/python /home/tiennguyen/Desktop/research/tool/fmarket_report_send_mail/main.py >> /home/tiennguyen/Desktop/research/tool/fmarket_report_send_mail/file.log 2>&1