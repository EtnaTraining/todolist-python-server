from flask import Flask, request, send_from_directory
import json, os
from werkzeug import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = '/tmp'

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/todos/<udid>", methods=['GET', 'POST'])
def todos(udid):
	print udid
        print request.form
	if request.method == 'POST':
		if todos.has_key(udid):
			todos[udid].append({'title' : request.form['title'], 'location' : request.form['location'], 'alarm' : request.form['alarm'], 'dueDate' : request.form['dueDate'], 'filename': request.form['filename'], 'hasChild' : True})
			return json.dumps(len(todos[udid]))
		else:	
			todos[udid] = [{'title' : request.form['title'], 'location' : request.form['location'], 'alarm' : request.form['alarm'], 'dueDate' : request.form['dueDate'], 'filename' : request.form['filename'], 'hasChild' : True}] 		
			return json.dumps(len(todos[udid]))
	if request.method == 'GET':
		print todos
		if todos.has_key(udid):
			return json.dumps(todos[udid]) 
		else: 
			return json.dumps([])


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
	filename = request.form['filename']
        if file: # and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            #return redirect(url_for('uploaded_file', filename=filename))
            return filename
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/upload/<filename>')
def uploaded_file(filename):
    print filename
    return send_from_directory(UPLOAD_FOLDER,
                               filename)


if __name__ == "__main__":
	todos = {}
    	app.run(host='0.0.0.0', debug = True)
