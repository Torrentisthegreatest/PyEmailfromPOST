# <PyEmailfromPOST is to run a website so a form from another website can be summitted here so an email can be sent. Developed so a website hosted such that only html, css, and javascript work, not allowing for emails to be sent directly.>
# Copyright (C) 2019  Simon Weizman

# This file is a part of PyEmailfromPOST

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import smtplib, ssl, os
from config import config
from flask import Flask, request
app = Flask(__name__)

def sendemail(submittedemail, submittedsubject, submittedmsg, submittedname):
	port = 465
	sitename = config.emailconfig["sitename"]
	smtp_server = config.emailconfig["smtpserver"]
	sender_email = config.emailconfig["senderemail"]
	receiver_email = config.emailconfig["receiveremail"]
	password = config.emailconfig["password"]
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
