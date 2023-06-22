from email.mime.multipart import MIMEMutipart
from email.mime.text import MIMEText

content = MIMEMutipart()  #建立MIMEMutipart物件
content["subject"] = "Mail Title"  #郵件標題
content["from"] = "jennifer910103@gms.tku.ecd du.tw"  #sender
content["to"] = "409630307@gmail.com"  #recipient
content.attach(MIMEText("Write some content here to your reciptient."))
