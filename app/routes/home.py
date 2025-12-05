# app/routes/students.py
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from app.services.home_service import HomeService
from app.models.program_model import Program

home_bp = Blueprint('home', __name__, url_prefix='/home', template_folder='../templates')

@home_bp.route('/')
def describe():
    number_of_student = HomeService.number_of_student()
    return render_template('home.html', number_of_student=number_of_student)