from flask import Flask, render_template, url_for
import os
import json
import textwrap

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

#note that it is easier here in os.walk to define the directory, so we'll add an argument for 'user' here.
def get_static_file_map(usrFolder):
	file_map= {}
	for dirname, subdirs, files in os.walk('static/{}/'.format(usrFolder)):
		file_map[dirname] = []
		for name in files:
			file_map[dirname].append(os.path.join(dirname[7::], name))
	return file_map

@app.route("/inktober/<username>")
def userGallery(username):
	file_map = get_static_file_map(username)
	return render_template('gallery.html', file_map=file_map,)

if __name__ == '__main__':
	app.run(debug=true)

