#!/usr/bin/python3.7.6

import os
import uuid
import sqlite3
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin

import zipfile

# py from scipoc
from scipoc.data_conversions.prepare_s3dis_label import prepare_s3dis_label
from scipoc.data_conversions.prepare_s3dis_data import prepare_s3dis_data
from scipoc.data_conversions.prepare_s3dis_filelists import prepare_s3dis_filelists


#prepare_s3dis_label("data/5581a3019/Stanford3dDataset_v1.2_Aligned_Version","data/5581a3019/S3DIS/prepare_label_rgb")
app = Flask(__name__)
CORS(app)

app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['UPLOAD_UNZIP_FOLDER'] = 'data'


conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

# Warning: Flask in debug mode runs the init code here two times
try:
    c.execute('SELECT COUNT(id) FROM files')
    print(c.fetchone()[0], 'uploads in database')
except:
    c.execute("""
					CREATE TABLE `files` (
						`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
						`uploadUUID`	TEXT NOT NULL,
						`folderPath`	TEXT NOT NULL,
						`fileName`	TEXT NOT NULL
					);
				 """)
    print('Initialized database')
conn.commit()
conn.close()


@app.route('/upload', methods=['POST'])
def upload_file():
    print(request)
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'Bad request', 400
        file = request.files['file']
        if file.filename == '':
            return 'Bad request', 400
        if file:
            conn = sqlite3.connect('db.sqlite')
            c = conn.cursor()
            filename = secure_filename(file.filename)
            uploadID = uuid.uuid4().hex[0:9]
            folderPath = app.config['UPLOAD_FOLDER']+'/' + uploadID
            os.makedirs(folderPath)

            file.save(os.path.join(
                app.config['UPLOAD_FOLDER'], uploadID, filename))
            c.execute("""
						 INSERT INTO `files` (`uploadUUID`, `folderPath`, `fileName`) VALUES (
							?,?,?) 
						 """, (uploadID, folderPath, filename,))
            conn.commit()
            conn.close()
            response = jsonify({'uploadUUID': uploadID,'filename':filename})

            return response

# FIXME: Flask as production server to serve files? :thinking:


@app.route('/file/<fileID>', methods=['GET'])
def serve_file(fileID):
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    try:
        c.execute("""
					 SELECT folderPath, fileName FROM files WHERE uploadUUID = ? 
					 """, (fileID,))
        uploadDetails = c.fetchone()
        folderPath = uploadDetails[0]
        name = uploadDetails[1]
        conn.commit()
        conn.close()
        return send_from_directory(folderPath, name, as_attachment=True)
    except:
        conn.commit()
        conn.close()
        return 'File not found', 404

#####  REQUST FOR SEGMENTATION   #####
@app.route('/seg/datapre/<fileID>', methods=['GET'])
def data_preparation(fileID):
    return fileID


# unzip
@app.route('/seg/datapre/unzip/<uploadID>', methods=['GET'])
def data_preparation_unzip(uploadID):

    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    try:
        c.execute("""
					 SELECT fileName FROM files WHERE uploadUUID = ? 
					 """, (uploadID,))
        uploadDetails = c.fetchone()
        name = uploadDetails[0]
        # unzip the file for scipoc
        folderPath_data_from = app.config['UPLOAD_FOLDER']+'/' + uploadID +'/' + name; 
        folderPath_data_to = app.config['UPLOAD_UNZIP_FOLDER']+'/' + uploadID
        os.makedirs(folderPath_data_to)
        with zipfile.ZipFile(folderPath_data_from, 'r') as zip_ref:
            zip_ref.extractall(folderPath_data_to)
        conn.commit()
        conn.close()
        response = jsonify({'path': folderPath_data_to})

        return response
    except:
        conn.commit()
        conn.close()
        return 'File not found', 404

# label
@app.route('/seg/datapre/labelling/<fileID>', methods=['GET'])
def data_preparation_labelling(fileID):
    DEFAULT_DATA_DIR = 'data/'+fileID+'/Stanford3dDataset_v1.2_Aligned_Version'
    DEFAULT_OUTPUT_DIR = 'data/'+fileID+'/S3DIS/prepare_label_rgb'

    prepare_s3dis_label(DEFAULT_DATA_DIR,DEFAULT_OUTPUT_DIR)
    response = jsonify({'path': DEFAULT_OUTPUT_DIR})

    return response
    

# format
@app.route('/seg/datapre/format/<fileID>', methods=['GET'])
def data_preparation_formatting(fileID):
    # TODO: make these paths to be global
    DEFAULT_DATA_DIR = 'data/'+fileID+'/S3DIS/prepare_label_rgb/'
    DEFAULT_PLY_OUTPUT_DIR = 'data/'+fileID+'/S3DIS/'

    prepare_s3dis_data(DEFAULT_DATA_DIR,DEFAULT_PLY_OUTPUT_DIR)
    response = jsonify({'root': DEFAULT_DATA_DIR,'ply_path': DEFAULT_PLY_OUTPUT_DIR})

    return response

# filelist
@app.route('/seg/datapre/filelist/<fileID>', methods=['GET'])
def data_preparation_filelisting(fileID):
    # TODO: make these paths to be global
    DEFAULT_DATA_DIR = 'data/'+fileID+'/S3DIS/prepare_label_rgb/'

    prepare_s3dis_filelists(DEFAULT_DATA_DIR)
    response = jsonify({'root': DEFAULT_DATA_DIR})

    return response

if __name__ == "__main__":
    app.run(debug=True, host='192.168.3.14')
