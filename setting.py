import smtplib

with smtplib.SMTP(host = "smtp.gmail.com", port = "587") as smtp:   #setting SMTP server
    try:
        smtp.ehlo() #verify SMTP server
        smtp.starttls() #Create encrypted transmission
        smtp.login("jennifer910103@gmail.com")  #login sender's gmail
        smtp.send_message(content)  #sending mail
        print("Complete!")
    except Exception as e:
        print("Error message: ", e)