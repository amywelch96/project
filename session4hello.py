from flask import Flask , render_template,request

app = Flask("MyApp")

@app.route("/")
def hello():
	return "Hello World!"
@app.route("/<name>")
def hello_someone(name):
	return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up_post():
	form_data = request.form
	print form_data["email"]
	return "All OK"

@app.route("/signup", methods=["GET"])
def sign_up_get():
	return render_template("signup.html")

app.run(debug=True)