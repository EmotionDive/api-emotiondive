from pathlib import Path
from datetime import datetime
import json

def write_activity_info(username, successes, failures, overwrite=True):
    """
    Creates/Updates an user special activity info
    """
    try:
        # Checking if the parent directory and file exists
        activity_file = Path("user_activities/" + username + ".json")
        activity_file.parent.mkdir(exist_ok=True, parents=True)

        # Checking overwrite flag
        if not overwrite:
            # Reading the json file and loading it as a dict to get previous data
            file = open(activity_file)
            data = json.load(file)
            successes = data["exitos"] + successes
            failures = data["fracasos"] + failures
            file.close()

        # Creating activity serialized object
        activity_dict = {
            "username": username,
            "last_update": str(datetime.today()),
            "exitos": successes,
            "fracasos": failures
        }
        activity_obj = json.dumps(activity_dict, indent=4)

        # Writing to json
        with open(activity_file, 'w') as file:
            file.write(activity_obj)

        response_obj = {
            "status": "success",
            "message": "User activity info was written successfully."
        }
        return response_obj, 200
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": str(e)
        }
        return response_obj, 400

def read_activity_info(username):
    """
    Reads and returns an user special activity info
    """
    try:
        # Checking if the parent directory and file exists
        activity_file = Path("user_activities/" + username + ".json")
        activity_file.parent.mkdir(exist_ok=True, parents=True)

        # Reading the json file and loading it as a dict
        file = open(activity_file)
        data = json.load(file)
        file.close()

        response_obj = {
            "status": "success",
            "message": "User activity info was read successfully.",
            "data": data,
        }
        return response_obj, 200
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": str(e)
        }
        return response_obj, 400

def write_activity_info_specific(username, index, success, failure):
    """
    Creates/Updates an user specific special activity info given an index
    """
    try:
        # Checking if the parent directory and file exists
        activity_file = Path("user_activities/" + username + ".json")
        activity_file.parent.mkdir(exist_ok=True, parents=True)

        # Reading the json file and loading it as a dict to get previous data
        file = open(activity_file)
        data = json.load(file)

        if index < len(data["exitos"]):
            data["exitos"][index] = success
            data["fracasos"][index] = failure
        else:
            data["exitos"].append(success)
            data["fracasos"].append(failure)

        file.close()

        # Creating activity serialized object
        activity_dict = {
            "username": username,
            "last_update": str(datetime.today()),
            "exitos": data["exitos"],
            "fracasos": data["fracasos"]
        }
        activity_obj = json.dumps(activity_dict, indent=4)

        # Writing to json
        with open(activity_file, 'w') as file:
            file.write(activity_obj)

        response_obj = {
            "status": "success",
            "message": "User activity info was written successfully."
        }
        return response_obj, 200
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": str(e)
        }
        return response_obj, 400

def read_activity_info_specific(username, index):
    """
    Reads and returns an user specific special activity info given an index
    """
    try:
        # Checking if the parent directory and file exists
        activity_file = Path("user_activities/" + username + ".json")
        activity_file.parent.mkdir(exist_ok=True, parents=True)

        # Reading the json file and loading it as a dict
        file = open(activity_file)
        data = json.load(file)
        file.close()

        specific_activity_obj = {
            "username": data["username"],
            "last_update": data["last_update"],
            "info_index": index,
            "exito": data["exitos"][index] if index < len(data["exitos"]) else "",
            "fracasos": data["fracasos"][index] if index < len(data["fracasos"]) else ""
        }

        response_obj = {
            "status": "success",
            "message": "User activity info was read successfully.",
            "data": specific_activity_obj,
        }
        return response_obj, 200
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": str(e)
        }
        return response_obj, 400