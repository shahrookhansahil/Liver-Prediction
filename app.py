# import numpy as np
# from flask import Flask, request, jsonify, render_template
# import pickle

# # Create flask app
# flask_app = Flask(__name__)
# model = pickle.load(open("classifier.pkl", "rb"))

# @flask_app.route("/")
# def Home():
#     return render_template("index.html")

# @flask_app.route("/predict", methods = ["POST"])
# def predict():
#     float_features = [float(x) for x in request.form.values()]
#     features = [np.array(float_features)]
#     prediction = model.predict(features)
#     return render_template("index.html", prediction_text = "The Result of Liver disease Is".format(prediction))

# if __name__ == "__main__":
#     flask_app.run(debug=True)

from flask import Flask,render_template,request
import pickle
import numpy as np
app = Flask(__name__)

model = pickle.load(open('class.pkl','rb'))
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route("/predict",methods = ["POST"])
def predict():
    features = request.form.values()
    float_features = []


    for i in features:
        float_features.append(float(i))


    features = [np.array(float_features)]
    pred = model.predict(features)

    if pred == 1:
        vr = "The patient has Liver disease"
    else:
        vr = "The patient do not have Liver disease"

    return render_template('index.html',prediction_text = "Output:  {}".format(vr))


if __name__ == '__main__':
    app.run()