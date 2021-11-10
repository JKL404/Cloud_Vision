import os
from app import app
import urllib.request
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for, render_template

#Google API Library
from google.cloud import vision
from google.cloud.vision import types

#Authenticating service account
client = vision.ImageAnnotatorClient()
client = vision.ImageAnnotatorClient.from_service_account_file('apikey.json')




ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
	return render_template('index.html')
	

@app.route('/textdetect/')
def upload_form():
	return render_template('upload.html')

@app.route('/textdetect/', methods=['POST'])
def upload_image():
	if 'files[]' not in request.files:
		flash('No file part')
		return redirect(request.url)
	files = request.files.getlist('files[]')
	file_names = []
	for file in files:
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file_names.append(filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#else:
		#	flash('Allowed image types are -> png, jpg, jpeg, gif')
		#	return redirect(request.url)

	return render_template('upload.html', filenames=file_names)

@app.route('/facedetect/')
def upload_form1():
	return render_template('detect.html')

@app.route('/facedetect/', methods=['POST'])
def upload_image1():
	if 'files[]' not in request.files:
		flash('No file part')
		return redirect(request.url)
	files = request.files.getlist('files[]')
	file_names = []
	for file in files:
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file_names.append(filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#else:
		#	flash('Allowed image types are -> png, jpg, jpeg, gif')
		#	return redirect(request.url)

	return render_template('detect.html', filenames=file_names)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)


@app.route('/imgtotext/<filename>')
def display_text(filename):
	#Opening Images
	image_to_open = 'static/uploads/'+filename
	with open(image_to_open, 'rb') as image_file:
	    content = image_file.read()
	image = vision.types.Image(content=content)
	#image to text
	text_response = client.text_detection(image=image)
	texts = [text.description for text in text_response.text_annotations]
	return render_template('message.html',name=texts[0],title="Image To Text")  

@app.route('/imgtolabel/<filename>')
def display_label(filename):
	#Opening Images
	image_to_open = 'static/uploads/'+filename
	with open(image_to_open, 'rb') as image_file:
	    content = image_file.read()
	image = vision.types.Image(content=content)
	#img to label
	web_response = client.web_detection(image=image)
	web_content = web_response.web_detection
	web_content.best_guess_labels
	predictions = [(entity.description, '{:.2%}'.format(entity.score)) for entity in web_content.web_entities]
	web_content.full_matching_images
	web_content.visually_similar_images[:3]
	return render_template('message.html',name=predictions[0],title="Image To Label")

@app.route('/facedetect/<filename>')
def display_face(filename):
	#Opening Images
	image_to_open = 'static/uploads/'+filename
	with open(image_to_open, 'rb') as image_file:
	    content = image_file.read()
	image = vision.types.Image(content=content)
	#Face Prediction
	face_response = client.face_detection(image=image)
	face_content = face_response.face_annotations
	#face_content[0].detection_confidence
	likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
	detectface=[]
	for face in face_content:
		detectface.append('anger: {}'.format(likelihood_name[face.anger_likelihood]))
		detectface.append('joy: {}'.format(likelihood_name[face.joy_likelihood]))
		detectface.append('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
	return render_template('message.html',name=face_content[0].detection_confidence,title="Face Prediction",facee=detectface) 

if __name__ == "__main__":
    app.run()
