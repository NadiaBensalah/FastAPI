# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 08:44:32 2022

@author: BENSALAH
"""




#hypercorn main:app --reload
#☺http://127.0.0.1:8000/docs
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


import pandas as pd
import joblib
import pickle

from pytube import YouTube



app=FastAPI(title='Nadia tna9al 3la wady',description='Nadia tna9al 3la wady')

db=[]

clf_filename='naive_bayes_classifier.pkl'
vec_filename='count_vectorizer.pkl'
vectorizer=pickle.load(open(vec_filename,'rb'))
nb_clf=pickle.load(open(clf_filename,'rb'))       
        
        
class youtubeURL(BaseModel):
    URL:str
    #Title:str
    #Category:str
    
    
@app.get('/')
def index():    
    return "Nadia"


@app.get('/infer')
def infer_Topic():
    results=[]
    for video in db:
        yt = YouTube(video['URL'])
        Title=yt.title
        prediction =nb_clf.predict(vectorizer.transform([Title]))[0]
        results.append({'URL':video['URL'],'Title':Title,'Category':prediction})
    return results

@app.post('/youtubeURL')
def Enter_url(url: youtubeURL):
    
    db.append(url.dict())
    return db[-1]

if __name__ == "__main__":
    uvicorn.run("main:app")
