Name: Dee Wu
ID: 185825860
Email: wuxx2586@mylaurier.ca
WorkID: cp610-project

1. Statement: I claim that the enclosed submission is my individual work.

2. Server Information:
You are using Jupyter Notebook.

The version of the notebook server is: 6.3.0
The server is running on this version of Python:
Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)]

Current Kernel Information:
Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.23.1 -- An enhanced Interactive Python. Type '?' for help.

3. Folder PATH listing for volume Windows
Volume serial number is BC66-004A
C:.
|   .gitattributes
|   DatasetComparison.xlsx
|   Data_Mining_Approach_to_Detect_Heart_Dis.pdf
|   folderStructure.doc
|   How to Setup a New Flask App on a Mac.docx
|   Screen Recording 2021-07-21 at 4.58.26 PM.mov
|   wuxx2586_critique_0720.pdf
|   wuxx2586_presentation_0720.pdf
|   wuxx2586_project_0720.pdf
|   wuxx2586_proposal_0630.pdf
|   
+---.ipynb_checkpoints
|       Diagnosis of Heart Disease - 01 Data -checkpoint.ipynb
|       Diagnosis of Heart Disease - 02 Model-checkpoint.ipynb
|       Diagnosis of Heart Disease - 03 API-checkpoint.ipynb
|       Diagnosis of Heart Disease Proposal-checkpoint.ipynb
|       Doing Data Science with Python - 02 Exploring Processing Data -checkpoint.ipynb
|       Doing Data Science with Python - 03 Building and Evaluating Models-checkpoint.ipynb
|       Doing Data Science with Python - 04 API-checkpoint.ipynb
|       hello_world_api-checkpoint.ipynb
|       Q2 Naive Bayers Classifier Prediction-checkpoint.ipynb
|       Reference-checkpoint.ipynb
|       Untitled-checkpoint.ipynb
|       
+---code
|   |   $api_file
|   |   app.py
|   |   Diagnosis of Heart Disease - 01 Data .ipynb
|   |   Diagnosis of Heart Disease - 02 Model.ipynb
|   |   Diagnosis of Heart Disease - 03 API.ipynb
|   |   get_processed_data.py
|   |   
|   \---.ipynb_checkpoints
|           Diagnosis of Heart Disease - 01 Data -checkpoint.ipynb
|           Diagnosis of Heart Disease - 02 Model-checkpoint.ipynb
|           Diagnosis of Heart Disease - 03 API-checkpoint.ipynb
|           
+---data
|   +---processed
|   |       test.csv
|   |       train.csv
|   |       
|   \---raw
|           cleveland.data
|           cleveland.processed.data
|           hungarian.data
|           hungarian.processed.data
|           long-beach-va.data
|           long-beach-va.processed.va.data
|           switzerland.data
|           switzerland.processed.data
|           
+---models
|       api.py
|       final_prediction.pickle
|       lr_model.pkl
|       lr_scaler.pkl
|       machine_learning_api.py
|       
\---src
    +---data
    |       get_processed_data.py
    |       
    \---models
            hello_world_api.py
            machine_learning_api.py
            
4. Heart Disease Diagnosis API
Step 1: Setup Environment
In order let models folder be current folder, $python3 api.py, follow the step in mac terminal:

DeematoMacBook-Pro:project user$ pwd
/Users/user/desktop/cp-610/project
DeematoMacBook-Pro:project user$ mkdir MyNewFlaskApp
DeematoMacBook-Pro:project user$ cd MyNewFlaskApp
DeematoMacBook-Pro:MyNewFlaskApp user$ python3 -m venv venv
DeematoMacBook-Pro:MyNewFlaskApp user$ source venv/bin/activate
(venv) DeematoMacBook-Pro:MyNewFlaskApp user$ pip3 install Flask
Collecting Flask
  Using cached Flask-2.0.1-py3-none-any.whl (94 kB)
Collecting itsdangerous>=2.0
  Using cached itsdangerous-2.0.1-py3-none-any.whl (18 kB)
Collecting Jinja2>=3.0
  Using cached Jinja2-3.0.1-py3-none-any.whl (133 kB)
Collecting Werkzeug>=2.0
  Using cached Werkzeug-2.0.1-py3-none-any.whl (288 kB)
Collecting click>=7.1.2
  Using cached click-8.0.1-py3-none-any.whl (97 kB)
Collecting MarkupSafe>=2.0
  Using cached MarkupSafe-2.0.1-cp39-cp39-macosx_10_9_x86_64.whl (13 kB)
Installing collected packages: MarkupSafe, Werkzeug, Jinja2, itsdangerous, click, Flask
Successfully installed Flask-2.0.1 Jinja2-3.0.1 MarkupSafe-2.0.1 Werkzeug-2.0.1 click-8.0.1 itsdangerous-2.0.1
(venv) DeematoMacBook-Pro:MyNewFlaskApp user$ pwd
/Users/user/desktop/cp-610/project/MyNewFlaskApp
(venv) DeematoMacBook-Pro:MyNewFlaskApp user$ cd ..
(venv) DeematoMacBook-Pro:project user$ cd models
(venv) DeematoMacBook-Pro:models user$ ls
api.py			lr_model.pkl		machine_learning_api.py
final_prediction.pickle	lr_scaler.pkl
(venv) DeematoMacBook-Pro:models user$ python3 api.py
Traceback (most recent call last):
  File "/Users/user/Desktop/cp-610/project/models/api.py", line 3, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
(venv) DeematoMacBook-Pro:models user$ pip install numpy
Collecting numpy
  Using cached numpy-1.21.1-cp39-cp39-macosx_10_9_x86_64.whl (17.0 MB)
Installing collected packages: numpy
Successfully installed numpy-1.21.1
(venv) DeematoMacBook-Pro:models user$ python3 api.py
Traceback (most recent call last):
  File "/Users/user/Desktop/cp-610/project/models/api.py", line 24, in <module>
    model = p.load(open(modelfile, 'rb'))
ModuleNotFoundError: No module named 'sklearn'
(venv) DeematoMacBook-Pro:models user$ pip install sklearn
Collecting sklearn
  Using cached sklearn-0.0-py2.py3-none-any.whl
Collecting scikit-learn
  Using cached scikit_learn-0.24.2-cp39-cp39-macosx_10_13_x86_64.whl (7.3 MB)
Collecting threadpoolctl>=2.0.0
  Using cached threadpoolctl-2.2.0-py3-none-any.whl (12 kB)
Requirement already satisfied: numpy>=1.13.3 in /Users/user/Desktop/cp-610/project/MyNewFlaskApp/venv/lib/python3.9/site-packages (from scikit-learn->sklearn) (1.21.1)
Collecting scipy>=0.19.1
  Using cached scipy-1.7.0-cp39-cp39-macosx_10_9_x86_64.whl (32.1 MB)
Collecting joblib>=0.11
  Using cached joblib-1.0.1-py3-none-any.whl (303 kB)
Installing collected packages: threadpoolctl, scipy, joblib, scikit-learn, sklearn
Successfully installed joblib-1.0.1 scikit-learn-0.24.2 scipy-1.7.0 sklearn-0.0 threadpoolctl-2.2.0
(venv) DeematoMacBook-Pro:models user$ python3 api.py
 * Serving Flask app 'api' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 275-582-264




Step 2: In Jupyter Notebook
Execute Diagnosis of Heart Disease - 03 API-checkpoint.ipynb.

5. github repository
https://deewu123@github.com/deewu123/project

6. Google Drive Project Link
https://drive.google.com/file/d/1AH9wQMIzHr9EsvDF-lzXoAf2I2gn1dJC/view?usp=sharing
