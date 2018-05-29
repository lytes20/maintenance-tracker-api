"""
File that has the api core functionality
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

all_requests = []
number_of_requests = len(all_requests)

@app.route("/", methods=["POST"])
def create_request():
    new_request = [{"title":"Iphone fix"}, {"desc":"Fix the screen of my Iphone"}]
    all_requests.append(new_request)
    new_number_of_requests = len(all_requests)
    if(new_number_of_requests > number_of_requests):
        return jsonify({"message":"sucessfully created request", "user_request": all_requests})
    else:
        return jsonify({"message":"can not add request"})

if __name__ == "__main__":
    app.run(debug = True)
