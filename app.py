#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)

# @ is a function decorator
# must run the app.route first before running any function below


# In[3]:



from flask import request, render_template
import joblib
    
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        Signal = request.form.get("Signal")
        print(Signal)
        model = joblib.load("DBSReg")
        pred = model.predict([[float(Signal)]])
        s1 = "predict DBS Share price base on Linear Regression model is  : " + str(pred) 
        model = joblib.load("DBSDT")
        pred = model.predict([[float(Signal)]])
        s2 = "predict DBS Share price base on Decision Tree model is  : " + str(pred)
        model = joblib.load("DBSNN")
        pred = model.predict([[float(Signal)]])
        s3 = "predict DBS Share price base on Neural Network model is  : " + str(pred)       
        return(render_template("index.html", result1=s1, result2=s2, result3=s3))
    else:
        return(render_template("index.html", result1=2, result2=2, result3=2))


# In[ ]:


if __name__=="__main__": 
    app.run()


# In[ ]:




