"""
File that has the api core functionality
"""
from flask import Flask, jsonify, request
from models import MaintenanceRequest, User
import random, json

app = Flask(__name__)

all_requests = []
Users = []
#---------------------------------------------------------------------------------------------------------
# Start of End points for user authentication

@app.route("/<v1>/user/register", methods=["POST"])
def register(v1):
    """End point to register a new user"""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    if not username:
        return jsonify({"message": "Missing username parameter"}), 400
    if not password:
        return jsonify({"message": "Missing password parameter"}), 400
    if not email:
        return jsonify({"message": "Missing email parameter"}), 400
   
    new_user = User(username, password, email)
    Users.append(new_user)
    return jsonify({'message':'sucessfully registered'}), 201


@app.route("<v1>/user/login", methods=["POST"])
def login(v1):
    post_data = request.get_json()
    email = post_data.get("email")
    password = post_data.get("password")
    

    if not email:
        return jsonify({"message": "Missing email parameter"}), 400
    if not password:
        return jsonify({"message": "Missing password parameter"}), 400

    return jsonify({"message": "sucessfully logged in"}), 200

#End of user authentication end points
#---------------------------------------------------------------------------------------------------------


#Start of the priority end points
@app.route("/<v1>/users/requests", methods=["POST"])
def create_request(v1):
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

@app.route("/<v1>/users/requests", methods=["GET"])
def fetch_requests(v1):
    """ Endpoint to fetch saved user requests """
    
    #check if user has any requests
    if len(all_requests) < 1:
        return jsonify({
            "message":"You have not made any requests yet"
        })
    
    #if user has more than one request
    if len(all_requests) > 1:
        return jsonify({
            "message":"Successfully fetched request",
            "requests":[
                json.dumps(a_request.__dict__) for a_request in all_requests
            ]
        })

@app.route("/<v1>/users/requests/<requestid>", methods=["GET"])
def fetch_a_request(v1, requestid):
    """ Endpoint to fetch a single user requests """

    #check if user has any requests
    if len(all_requests) < 1:
        return jsonify({
            "message":"You have not made any requests yet"
        })
    
    #if user has more than one request
    if len(all_requests) > 1:
        returned_request = [a_request for a_request in all_requests if a_request.request_id == requestid]
        return jsonify({
            "message":"Successfully fetched the request",
            "request": returned_request[0]
        })

@app.route("/<v1>/users/requests/<requestid>", methods=["PUT"])
def edit_a_request(v1, requestid):
    """ Endpoint to edit a user requests """

    #check if user has any requests
    if len(all_requests) < 1:
        return jsonify({
            "message":"You have not made any requests yet"
        })
    
    #if user has more than one request
    if len(all_requests) > 1:
        #get entered data
        data = request.get_json()

        #picking the request attributes
        req_title = data.get("request_title")
        req_desc = data.get("request_description")

        returned_request = [a_request for a_request in all_requests if a_request.request_id == requestid]
        returned_request[0].title = req_title
        returned_request[0].description = req_desc

        return jsonify({
            "message":"Successfully fetched the request",
            "request": returned_request[0]
        })

if __name__ == "__main__":
    app.run(debug = True)
