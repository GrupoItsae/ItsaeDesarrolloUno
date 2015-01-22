# -*- coding: utf-8 -*-
 
from flask import Flask
import os
app=Flask(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
APP_DIR = os.path.join(BASE_DIR, 'app')
STATIC_DIR = os.path.join(APP_DIR, 'static')
MEDIA_ROOT = os.path.join(STATIC_DIR, 'media')
UPLOAD_FOLDER = MEDIA_ROOT
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import mainIndex
from app import personaMain