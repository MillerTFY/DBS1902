from flask import Flask
app = Flask(__name__)


from flask import request, render_template
import joblib
    
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBSReg")
        pred = model.predict([[float(rates)]])
        s1 = "predict DBS Share price base on Linear Regression model is  : " + str(pred) 
        model = joblib.load("DBSDT")
        pred = model.predict([[float(rates)]])
        s2 = "predict DBS Share price base on Decision Tree model is  : " + str(pred)
        model = joblib.load("DBSNN")
        pred = model.predict([[float(rates)]])
        s3 = "predict DBS Share price base on Neural Network model is  : " + str(pred)       
        return(render_template("index.html", result1=s1, result2=s2, result3=s3))
    else:
        return(render_template("index.html", result1=2, result2=2, result3=2))


if __name__=="__main__": 
    app.run()