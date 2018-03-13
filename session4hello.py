from flask import Flask , render_template,request

app = Flask("MyApp")

@app.route("/")
def home():
	return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def sign_up_post():
	form_data = request.form
	save_email(request.form['email'])
	print form_data["email"]
	return render_template("signup.html")

import requests
def send_simple_message():
 return requests.post(
    "https://api.mailgun.net/v3/sandbox2564db18e3a0458ea7b33908f5d08ef9.mailgun.org/messages",
    auth=("api", "key-08a2e354572978f71130c24d1be38443"),
    data={"from": "Excited User <mailgun@sandbox2564db18e3a0458ea7b33908f5d08ef9.mailgun.org>",
              "to": ["zccaawe@ucl.ac.uk", "zccaawe@ucl.ac.uk"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

send_simple_message()

def save_email(email_address):
    with open('emails_file.txt', 'a') as file_handle:
        file_handle.write(email_address + '\n')



app.run(debug=True)