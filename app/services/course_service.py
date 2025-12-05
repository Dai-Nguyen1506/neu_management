# app/services/course_service.py
from app.models.course_model import Course
# from app.utils.validators import validate_instructor_data

class CourseService:
    """Take Course"""

    @staticmethod
    def get_all_course():
        """Get all programs"""
        return Course.get_all()
    
    @staticmethod
    def get_course_by_program_id(program_id):
        """Get courses of a program"""
        return Course.get_by_program_id(program_id=program_id)
    
    @staticmethod
    def delete_course(course_id):
        """Delete a course"""

        Course.delete(course_id)
        return True, "Course deleted successfully"