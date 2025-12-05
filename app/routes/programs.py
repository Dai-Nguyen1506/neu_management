# app/routes/programs.py
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from app.services.program_service import ProgramService
from app.services.course_service import CourseService
from app.models.program_model import Program

programs_bp = Blueprint('programs', __name__, url_prefix='/programs', template_folder='../templates')


@programs_bp.route('/')
def list():
    """Display list of programs"""
    programs = ProgramService.get_all_programs()
    return render_template('programs/list.html', programs=programs)

@programs_bp.route('/search', methods=['GET', 'POST'])
def search():
    """Search programs"""
    if request.method == 'POST':
        program_id = request.form.get('program_id')
        name = request.form.get('name')

        programs = ProgramService.search_programs(
            program_id=program_id,
            name=name
        )
        return render_template('programs/list.html', programs=programs)
    
    return redirect(url_for('programs.list'))

@programs_bp.route('/InformationProgram/<int:program_id>')
def get_by_id(program_id):
    """Get program by id"""
    program = ProgramService.get_program_by_id(program_id)
    course = CourseService.get_course_by_program_id(program_id)
    return render_template('programs/detail.html',program=program, course=course)

@programs_bp.route('/create', methods=['GET', 'POST'])
def create():
    """Create a new program"""
    if request.method == 'GET':
        return render_template('programs/form.html')

    # Handle POST request
    data = {
        'program_name': request.form.get('program_name'),
        'department': request.form.get('department'),
        'duration_year': request.form.get('duration_year'),
        'degree_type': request.form.get('degree_type')
    }

    success, message = ProgramService.create_program(data)
    if success:
        flash(message, 'success')
        return redirect(url_for('programs.list'))
    else:
        flash(message if isinstance(message, str) else ', '.join(message), 'danger')
        return redirect(url_for('programs.list'))


@programs_bp.route('/update/<int:program_id>', methods=['GET', 'POST'])
def update(program_id):
    """Update Program"""
    program = ProgramService.get_program_by_id(program_id)
    if not program:
        flash('Program not found', 'danger')
        return redirect(url_for('programs.list'))

    if request.method == 'GET':
        return render_template('programs/form.html', program=program)

    # Handle POST request
    data = {}
    if request.form.get('program_name'):
        data['program_name'] = request.form.get('program_name')
    if request.form.get('department'):
        data['department'] = request.form.get('department')
    if request.form.get('duration_year'):
        data['duration_years'] = request.form.get('duration_years')
    if request.form.get('degree_type'):
        data['degree_type'] = request.form.get('degree_type')

    success, message = ProgramService.update_program(program_id, data)
    if success:
        flash(message, 'success')
        return redirect(url_for('programs.get_by_id', program_id=program_id))
    else:
        flash(message if isinstance(message, str) else ', '.join(message), 'danger')
        return redirect(url_for('programs.get_by_id', program_id=program_id))

@programs_bp.route('/delete/<int:program_id>', methods=['POST'])
def delete(program_id):
    """Delete program"""
    success, message = ProgramService.delete_program(program_id)
    if success:
        return jsonify({'success': True, 'message': message})
    return jsonify({'success': False, 'message': message}), 400

@programs_bp.route('/deletecourse/<int:course_id>', methods=['POST'])
def deletecourse(course_id):
    """Delete program"""
    success, message = CourseService.delete_course(course_id)
    if success:
        return jsonify({'success': True, 'message': message})
    return jsonify({'success': False, 'message': message}), 400
