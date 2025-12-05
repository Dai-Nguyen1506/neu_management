# app/models/course_model.py
from app.connection import get_connection

class Course:
    """Course model for database operations"""

    @staticmethod
    def get_all():
        """Get all courses"""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM course")
        courses = cursor.fetchall()
        conn.close()
        return courses
    
    @staticmethod
    def get_by_program_id(program_id):
        """Get Courrse By ID Program"""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM course WHERE program_id = %s"

        cursor.execute(query, (program_id,))
        courses = cursor.fetchall()
        conn.close()
        return courses
    
    @staticmethod
    def delete(course_id):
        """Delete Course"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM course WHERE course_id = %s", (course_id,))
        conn.commit()
        conn.close()
