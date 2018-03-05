import requests 
def send_simple_message():
	print 'sending mail'
	print 'result_simple_message()'
	result = requests.post ("https://api.mailgun.net/v3/sandbox2564db18e3a0458ea7b33908f5d08ef9.mailgun.org/messages",
        auth=("api", "key-08a2e354572978f71130c24d1be38443"),
        data={"from": "Excited User <mailgun@sandbox2564db18e3a0458ea7b33908f5d08ef9.mailgun.org>",
              "to": ["zccaawe@ucl.ac.uk", "zccaawe@ucl.ac.uk"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
	print result
    return result 

send_simple_message()