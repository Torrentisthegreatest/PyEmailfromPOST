import smtplib, ssl, os
from flask import Flask, request
app = Flask(__name__)

def sendemail(submittedemail, submittedsubject, submittedmsg, submittedname):
	port = 465
	sitename = str(os.environ.get("sitename"))
	smtp_server = str(os.environ.get("smtpserver"))
	sender_email = str(os.environ.get("senderemail"))
	receiver_email = str(os.environ.get("receiveremail"))
	password = str(os.environ.get("password"))
	message = """From: %s
To: %s
Reply-To: %s
Subject: %s
\n
You have received an email from your site %s

Sent by: %s
Message:
%s
""" % (sender_email, receiver_email, submittedemail, submittedsubject, sitename, submittedname, submittedmsg)
	print(message)
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)


	return """"
			<meta charset="UTF-8">
			<meta http-equiv="refresh" content="0; url=/">
			<script type="text/javascript">
				window.location.href = "https://simon.weizman.us#Contact"
			</script>"""

@app.route('/')
def home():
	return "I'm alive"

@app.route('/submit', methods=["POST"])
def mainpage():
	if request.method == "POST":
		submittedname = str(request.form['name'])
		submittedemail = str(request.form['email'])
		submittedsubject = str(request.form['subject'])
		submittedmsg = str(request.form['message'])
		return sendemail(submittedemail, submittedsubject, submittedmsg, submittedname)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080,debug = True)
