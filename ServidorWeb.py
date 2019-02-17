#!usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, send_from_directory, make_response
from optparse import OptionParser
from sys import exit
import re

app = Flask(__name__)
dir_raiz = ''
#addOptions: Muestra todas las opciones disponibles dentro del programa 
def addOptions():
	parser = OptionParser()
	parser.add_option('-d', '--directory',
		dest='dir', default='.',
		help='Directorio que será utilizado como directorio raíz por el servidor 
	)

	options, args = parser.parse_args()
	return options


def ob_directirio():
	print(dir_raiz, file_name)
	file_name = request.args.get('file')
	res = make_response(send_from_directory(abs_dir,file_name))
	res.headers['directory'] = dir_raiz
	return 1

@app.route('/becarios')
def muestra_imagen:
	#render_template nos permite pasarle la variable de la página HTML 
    return render_template('index.html')

if __name__ =="__main__":
    app.run(debug=True,port=8080)