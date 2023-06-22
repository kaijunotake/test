#import email.message

#msg = email.message.EmailMessage()
#msg["From"] = "bossofmails@gmail.com"
#msg["To"] = "bossofmails@gmail.com"
#msg["Subject"] = "貓貓真香對吧"

#msg.set_content("我好想要吸大貓貓")
#msg.add_alternative("<h3>這裡是大貓貓</h3>這裡是小貓貓~"subtype = "html")

#import smtplib
#search what gmail smtp server's port is
#server = smtplib.SMSTP_SSL("smtp.gmail.com", 465)
#server.login("bossofmails@gmail.com", "idjeonzpqaobdmmz")
#server.send_message(msg)
#server.close()


#imdaboss

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 你的 Gmail 帳戶資訊
gmail_user = 'bossofmails@gmail.com'
gmail_password = 'idjeonzpqaobdmmz'

# 寄件人和收件人設定
sender = 'bossofmails@gmail.com'
recipient = 'bossofmails@gmail.com'

# 建立郵件主題和內容
subject = '測試郵件'
message = '這是一封測試郵件的內容。'

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

try:
    # 建立 SMTP 連線
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)

    # 寄送郵件
    server.sendmail(sender, recipient, msg.as_string())
    server.close()

    print('郵件已成功寄出！')

except Exception as e:
    print('寄送郵件失敗:', str(e))