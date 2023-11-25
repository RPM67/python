import smtplib as smtp

ob = smtp.SMTP('smtp.gmail.com',
               587)  # SMTP() class will send connection request to 'gmail' server and 587 is port number of gmail server that need to be provided here
ob.ehlo()  # this funtion will help in connecting this python program to the connection received from gmail server from stored in ob object
ob.starttls()
sender_mail = 'dragonaklevel7@gmail.com'
sender_mail_app_password = 'wpyn snux iawo hmaf'  # since this python script is not authorised to access the gmail account. so, we generated this app password to give access of sender gmail to this python script
try:
    ob.login(sender_mail, sender_mail_app_password)
except smtp.SMTPAuthenticationError:
    exit("Invalid UserName or Password Entered")
except Exception as e:
    exit(e)

subject = "testing python program"
body = "this mail is automatically sent to you by Rahul Prakash Mishra with purpose of testing a gmail automate python program.\nso please ignore it."

message = f"subject:{subject}\n\n{body}"  # here you are formatting your mail by providing the subject here by using 'subject:'

receiver_mail = ['kumarsumanprakash8519@gmail.com', 'riyamishrarkm@gmail.com', 'nishasharma150203@gmail.com', 'amanak52141@gmail.com']

ob.sendmail('dragonaklevel7@gmail.com', receiver_mail, message)
print("mail sent successfully")

ob.quit()
