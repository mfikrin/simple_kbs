import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from flask import request,Flask,jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
env_config=os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    _json = request.json
    SAT = _json['SAT']
    SATSP = _json['SATSP']
    OAT = _json['OAT']
    MAT = _json['MAT']
    RAT = _json['RAT']
    SAFS = _json['SAFS']
    RAFS = _json['RAFS']
    SAFSCS = _json['SAFSCS']
    RAFSCS = _json['RAFSCS']
    OADCS = _json['OADCS']
    RADCS = _json['RADCS']
    CCVCS = _json['CCVCS']
    HCVCS = _json['HCVCS']
    SADSPSP = _json['SADSPSP']
    SADSP = _json['SADSP']
    OMI = _json['OMI']
    classifier = joblib.load('classifier.pkl')
    prediction = classifier.predict([[SAT,SATSP,OAT,MAT,RAT,SAFS,RAFS,SAFSCS,RAFSCS,OADCS,RADCS,CCVCS,HCVCS,SADSPSP,SADSP,OMI]])
    # return jsonify(_json)
    return jsonify({'Fault Detection Ground Truth': str(prediction[0])})
    


if __name__ == '__main__':
     app.run()