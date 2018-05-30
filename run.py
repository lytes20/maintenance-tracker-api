"""
File that has the api core functionality
"""
from flask import Flask, jsonify, request
from models import MaintenanceRequest, User
import random, json

app = Flask(__name__)

all_requests = []


@app.route("/users/requests", methods=["POST"])
def create_request():
    """ Endpoint to get the request data entered by the user """
    #get entered data
    data = request.get_json()

    #picking the request attributes
    req_title = data.get("request_title")
    req_desc = data.get("request_description")
    requester_name = "Gideon"
    req_id = len(all_requests) +1  # + random.randint(1, 3000)

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

    return jsonify({
        "message":"sucessfully created request",
        'request_title':new_request.title,
        "request_description":new_request.description,
        "requester_name" : new_request.requester_name,
        "request_id" : new_request.request_id
        })

@app.route("/users/requests", methods=["GET"])
def fetch_requests():
    """ Endpoint to fetch saved user requests """

    number_of_requests = len(all_requests)
    #check if user has any requests
    if len(all_requests) < 1:
        return jsonify({
            "message":"You have not made any requests yet"
        })
    
    #if user has just one request
<<<<<<< HEAD
    if number_of_requests  == 1:
=======
    if len(all_requests) == 1:
>>>>>>> tests
        return jsonify({
            "message":"Successfully fetched request",
            "requests":[
                json.dumps(a_request.__dict__) for a_request in all_requests
            ]
        })

<<<<<<< HEAD
    # for i in range(len(all_requests)):
    #     all_requests[i]

    # if number_of_requests > 1:
    #     return jsonify({
    #         "message":"You have not made any requests yet",
    #         "requests":[
    #             {
    #                 'request_title':all_requests[0].title,
    #                 "request_description":all_requests[0].description,
    #                 "requester_name" : all_requests[0].requester_name,
    #                 "request_id" : all_requests[0].request_id
    #             }
    #         ]
    #     })

@app.route("/users/requests/<requestid>", methods=["GET"])
def fetch_a_request(requestid):
    """ Function to fetch a single user request"""

    number_of_requests = len(all_requests)    
    #check if user has any requests
    if number_of_requests < 1:
        return jsonify({
            "message":"You have not made any requests yet"
        })

    #if user has requests
    for a_request in all_requests:
        if a_request.request_id == requestid:
            return jsonify({
                "message":"You have not made any requests yet",
                "request":[
                    {
                        'request_title':a_request.title,
                        "request_description":a_request.description,
                        "requester_name" :a_request.requester_name,
                        "request_id" :a_request.request_id
                    }
                ]
            })
        return jsonify({"message":"Request not found"})
    
  

=======
>>>>>>> tests
if __name__ == "__main__":
    app.run(debug = True)
