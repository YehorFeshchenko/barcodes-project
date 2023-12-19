"""
Flask blueprint - Components View
"""

from flask import Blueprint, redirect, request, abort, render_template, url_for, flash
from flask.json import jsonify
from .repository.componentRepository import ComponentRepository

components_blueprint = Blueprint("components", __name__)


@components_blueprint.route("/components", methods=["GET"])
def list_components():
    """
    List all components with details from related tables
    """
    components = ComponentRepository.get_all_components()
    return jsonify(components)
