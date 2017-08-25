
'''

 @ Frist web demo 

 安装mongodb
 熟悉flask
'''


from flask import Flask,request, render_template, url_for
import datetime
import pymongo

app = Flask(__name__)

mongoClient = pymongo.MongoClient('localhost',27017)
db = mongoClient['msgboard']

@app.route('/', methods=['GET', 'POST'])
def index():
	#return '<h1>Hello world!</h1><p>what fuck the world!!!</p>'
	if request.method == 'GET':
		return render_template('index.html', msglist=db['msg'].find())
	else:
		msg_collection = db['msg']
		time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
		msg_collection.insert({
			'msg':request.form['msg'],
			'time':time
			})
		return render_template('index.html', msglist=db['msg'].find())


if __name__=='__main__':
	app.run(debug=True)

