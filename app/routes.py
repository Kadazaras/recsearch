from flask import render_template, flash, redirect, url_for,request, jsonify,make_response
from app import app
from app import SessionLocal
from app.models import Event
import json
#from sklearn.cluster import DBSCAN
#import scipy.spatial as sp
import os
import pandas as pd


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    db = SessionLocal()
    return render_template('rp.html')

@app.route('/retrieve_data', methods=['POST'])
def retrieve_data():
    db = SessionLocal()
    variable = request
    bounds = json.loads(variable.form['bounds'])
    query = db.query(Event).filter(Event.long > bounds['_southWest']['lng'])\
        .filter(Event.long < bounds['_northEast']['lng']) \
        .filter(Event.lat > bounds['_southWest']['lat']) \
        .filter(Event.long < bounds['_northEast']['lat'])\
        .all()
    lista = []
    for i in range(len(query)):
        lista.append(query[i].to_dict())
    a = json.dumps(lista, indent=2)
    return make_response(a, 201)

@app.route('/retrieve_text', methods=['POST'])
def retrieve_text():
    db = SessionLocal()
    variable = request
    questions = variable.form.getlist('input[]')
    return '\n'.join(questions)


def cluster(data, epsilon,N): #DBSCAN, euclidean distance
    db     = DBSCAN(eps=epsilon, min_samples=N).fit(data)
    labels = db.labels_ #labels of the found clusters
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0) #number of clusters
    clusters   = [data[labels == i] for i in range(n_clusters)] #list of clusters
    return clusters, n_clusters
