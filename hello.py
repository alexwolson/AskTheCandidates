from flask import Flask, render_template, request
import Trumpbate02, Trump12
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def hello_world(name=None):
	if request.method == 'POST':
		try:
			result = Trumpbate02.debate().decode('ascii','ignore')
		except:
			result = Trumpbate02.debate().decode('ascii','ignore')
		result = result.replace('\n', "<br>")
		return render_template("hello.html", name = result, query=request.form['nm'])
	return render_template('hello.html', nameT=None, nameC=None, query=None)

@app.route('/qa', methods = ['POST', 'GET'])
def hello_qa(name=None):
	if request.method == 'POST':
		resultT = Trump12.trump_respond(request.form['nm'])
		resultC = Trump12.clinton_respond(request.form['nm'])
		return render_template("helloqa.html", nameT=resultT, nameC=resultC, query=request.form['nm'])
	return render_template('helloqa.html', nameT=None, nameC=None, query=None)
