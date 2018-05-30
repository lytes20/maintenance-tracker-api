"""
File that has the api core functionality
"""
from flask import Flask, jsonify, request
from models import MaintenanceRequest, User
import random

app = Flask(__name__)

all_requests = []
number_of_requests = len(all_requests)

@app.route("/users/requests", methods=["POST"])
def create_request():
    """ Function to get the request data entered by the user """
    #get entered data
    data = request.get_json()

    #picking the request attributes
    req_title = data.get("request_title")
    req_desc = data.get("request_description")
    requester_name = "Gideon"
    req_id = random.randint(1, 3000)

    #validation
    if not req_title:
        return jsonify({"message": "Request has no title"}), 400
    if not req_desc:
        return jsonify({"message": "Request has no description"}), 400
    if not requester_name:
        return jsonify({"message": "Request must be issued by a user"}), 400
    if not req_id:
        return jsonify({"message": "Request has no id"}), 400

    #storing entered request
    new_request = MaintenanceRequest(req_title, req_desc, requester_name, req_id)
    all_requests.append(new_request)
    # new_number_of_requests = len(all_requests)

    return jsonify({"message":"sucessfully created request", "user_request": all_requests})

@app.route("/users/requests", methods=["GET"])
def fetch_requests():
    return jsonify({"message":"success"})

if __name__ == "__main__":
    app.run(debug = True)
