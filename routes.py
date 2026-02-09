from flask import Blueprint, jsonify
from models import db, User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return 'funciona todo correcto'