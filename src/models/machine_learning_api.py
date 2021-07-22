from flask import Flask, request
import pandas as pd
import numpy as np
import json
import pickle
import os

app = Flask(__name__)

# Load Model and Scaler Files
model_path = os.path.join(os.path.pardir,os.path.pardir,'models')

model_filepath = os.path.join(model_path, 'lr_model.pkl')
scaler_filepath = os.path.join(model_path, 'lr_scaler.pkl')

scaler = pickle.load(open(scaler_filepath,'rb'))
model = pickle.load(open(model_filepath,'rb'))

# columns
columns = [ u'unnamed', u'diagnosed', u'age', \
       u'sex', u'trestbps', u'chol', u'fbs', u'restecg', u'thalach', \
       u'exang', u'oldpeak', u'slope', u'ca', u'thal', u'num', \
       u'trestbps_Bin_very_low', u'trestbps_Bin_low', u'trestbps_Bin_high', u'trestbps_Bin_very_high', u'AgeState_MiddleAdult', \
       u'AgeState_OldAdult ', u'cp_1.0', u'cp_2.0', u'cp_3.0', \
       u'cp_4.0', u'cat_A', u'cat_B', u'cat_C', \
       u'cat_D', u'cat_E', u'cat_F', u'cat_G', u'cat_Z'] 

@app.route('/api', methods=['POST'])
def make_prediction():
    # read json object and convert to json string
    data = json.dumps(request.get_json(force=True))
    # create pandas dataframe using json string
    df = pd.read_json(data)
    # extract passengerIds
    ##patient_ids = df['unnamed'].ravel()
    # actual survived values
    actuals = df['diagnosed'].ravel()
    # extract required columns based and convert to matrix
    X = model#df[columns].to_numpy().astype('float')
    # transform the input
    X_scaled = scaler#.transform(X)
    # make predictions
    predictions = model.predict(X)
    # create response dataframe
    #df_response = pd.DataFrame({'Patient': patient_ids, 'Predicted' : predictions, 'Actual' : actuals})
    df_response = pd.DataFrame({ 'Predicted' : predictions, 'Actual' : actuals})

    # return json 
    return df_response.to_json()

 

if __name__ == '__main__':
    # host flask app at port 10001
    app.run(port=10001, debug=True)
