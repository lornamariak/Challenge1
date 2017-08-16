from flask import Flask ,render_template ,redirect ,url_for, request
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
	error=None
	if request.method =='POST':
		if request.form['username'] != 'admin'or request.form['password'] != 'admin':
			error ='Invalid Credentials,Try again'
		else:
			return redirect(url_for('shoppinglist'))
	return render_template("welcome.html",error=error)
@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/shoppinglist")
def shoppinglist():
    return render_template("shoppinglist.html")

if __name__ == "__main__":
    app.run(debug=True)
