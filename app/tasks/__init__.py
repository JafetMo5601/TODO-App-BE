from flask import Blueprint
from flask_cors import CORS

tasks_bp = Blueprint("tasks", __name__)

from . import routes