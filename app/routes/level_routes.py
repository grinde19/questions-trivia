from flask import Blueprint
from app.controllers.level_controller import *

bp = Blueprint("levels", __name__)
bp.route("/api/levels/", methods=["GET"])(get_levels)
bp.route("/api/levels/<int:id>/", methods=["GET"])(get_level)
bp.route("/api/levels/", methods=["POST"])(create_level)
bp.route("/api/levels/<int:id>/", methods=["PUT"])(update_level)
bp.route("/api/levels/<int:id>/", methods=["DELETE"])(delete_level)
