from flask import Flask, render_template, request , jsonify
import os
import yaml
import joblib
import numpy as np
import pandas as pd

params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root,"static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(
    __name__, 
    static_folder = static_dir,
    template_folder = template_dir
)

def read_params(config_path):
    with open(config_path) as yaml_f:
        config = yaml.safe_load(yaml_f)
    return config

#predict methods for prediction
def predict(data):
    config = read_params(params_path)
    model_dir = config["webapp_model_dir"]
    model = joblib.load(model_dir)
    y_pred = model.predict(data)
    print(y_pred)
    return y_pred[0]

def api_response(request):
    try:
        data = request.json if request.json else request.form
        data = [list(map(float, data.values()))]
        response = predict(data)
        response = {"response": response}
        return jsonify(response)
    except Exception as e:
        print(e)
        error = {"error": "Something went Wrong!"}
        return jsonify(error)



#creating index root
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if request.form:
                data = dict(request.form)   #reuquesting all the variables  and storing it in float format
                data = [list(map(float, data.values()))]
                response = predict(data)
                return render_template("index.html", response = response)  


            elif request.json: 
                #if we want to query it in API that will be stored in json format
                response= api_response(request)
                return jsonify(response)


        except Exception as e:
            print(e)
            error = {"error": "Something went Wrong!"}
            return render_template("404.html", error = error)
        pass
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True, port= 5000)