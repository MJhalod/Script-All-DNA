from flask import Flask
from flask import request,jsonify
import os
app = Flask(__name__)

@app.route("/test",methods=["GET","POST"])
def test():
 if request.method == "GET":
     return jsonify({"Response": "Get Request Called"})
 elif request.method == "POST":
     req=request.json
     name=req["name"]
     return jsonify({"Response": "Hi " + name})
     
if(__name__ == "__main__"):
    app.run(debug=True)