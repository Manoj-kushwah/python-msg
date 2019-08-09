import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders 


def SendMail():
	try:
		print "============Prepare mail=========\n"
		msgFrom = "jsistudentportal@gmail.com"
		msgTo = input("To: ") #"manojkushwah58@gmail.com"
		msg = MIMEMultipart()
		msg['From'] = msgFrom #'jsistudentportal@gmail.com'
		msg['To'] = msgTo #'manojkushwah58@gmail.com'
		msg['Subject'] = input("Subject: ") #'Test mail'
		body_data = MIMEText(input("Body: "))
		msg.attach(body_data)

		filepath = "E:/manoj/demo/python/test/demo.txt"
		print "filepath: %s\n" %(filepath)
		fileName = os.path.basename(filepath)
		print "fileName: %s\n" %(fileName)
		fileData = open(filepath, "rb").read()
		print "fileData: %s\n" %(fileData)
		base = MIMEBase("application", "octet-stream")
		print "base: %s\n" %(base)
		base.set_payload(fileData)
		print "base payload: %s\n" %(base)
		encoders.encode_base64(base)
		print "base encoders: %s\n" %(base)
		base.add_header("Content-Disposition", "attachment; filename=%s" % fileName)
		print "base header: %s\n" %(base)
		msg.attach(base)

		# text = MIMEText("test")
		# msg.attach(text)
		# image = MIMEImage(img_data, name=os.path.basename("C:/Users/SAURABH/Desktop/input/bt_sec.png"))
		# msg.attach(image)
		if not msgTo:
			raise NameError("To not found.")
		if not msg['Subject']:
			raise NameError("Subject not found.")
		if not body_data:
			raise NameError("Body not found.")

		print "\n============Details=========\n%s\n" %(msg.as_string())

		try:
			print "Connecting to server =>"
			print "Open: socket open...."
			s = smtplib.SMTP("smtp.gmail.com",587)
			s.ehlo()
			s.starttls()
			s.ehlo()
			s.login(msgFrom, "password")
			print "Email sending...."
			s.sendmail(msgFrom, msgTo, msg.as_string())
			s.quit()
		except Exception as e:
			print "Error: email not send."
		else:
			print "Done: email has been send."
		finally:
			print "Close: socket closed."
	except Exception as e:
		print e.message
		SendMail()


SendMail()