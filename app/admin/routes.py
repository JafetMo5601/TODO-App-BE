from flask import request, jsonify
from flask_cors import cross_origin

from app.data import todoDB
from . import admin_bp


@admin_bp.route("/api/priority/add/", methods=["POST"])
@cross_origin()
def priorityAdd():
    response = todoDB.priorityAdd(request.get_json()["priorityName"])
    return jsonify(response)


@admin_bp.route("/api/priority/retrieve/", methods=["GET"])
@cross_origin()
def priorityRetrieve():
    response = todoDB.priorityRetrieve(request.get_json()["priorityId"])
    return jsonify(response)


@admin_bp.route("/api/status/add/", methods=["POST"])
@cross_origin()
def statusAdd():
    response = todoDB.statusAdd(request.get_json()["statusName"])
    return jsonify(response)


@admin_bp.route("/api/status/retrieve/", methods=["GET"])
@cross_origin()
def statusRetrieve():
    response = todoDB.statusRetrieve(request.get_json()["statusId"])
    return jsonify(response)


@admin_bp.route("/api/tag/add/", methods=["POST"])
@cross_origin()
def tagAdd():
    response = todoDB.tagAdd(request.get_json()["tagName"])
    return jsonify(response)


@admin_bp.route("/api/tag/retrieve/", methods=["GET"])
@cross_origin()
def tagRetrieve():
    response = todoDB.tagRetrieve(request.get_json()["tagId"])
    return jsonify(response)


@admin_bp.route("/api/tasktype/add/", methods=["POST"])
@cross_origin()
def taskTypeAdd():
    response = todoDB.taskTypeAdd(request.get_json()["taskTypeName"])
    return jsonify(response)


@admin_bp.route("/api/tasktype/retrieve/", methods=["GET"])
@cross_origin()
def taskTypeRetrieve():
    response = todoDB.taskTypeRetrieve(request.get_json()["taskTypeId"])
    return jsonify(response)
