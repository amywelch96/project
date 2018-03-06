from flask import Flask , render_template,request

app = Flask("MyApp")

@app.route("/")
def hello():
	return "Hello World!"
@app.route("/<name>")
def hello_someone(name):
	return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form
	print form_data["email"]
	return "All OK"
@app.route("/signup", methods=["GET"])
def sign_up():
	return render_template
app.run(debug=True)