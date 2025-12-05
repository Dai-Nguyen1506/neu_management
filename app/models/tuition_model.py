# app/models/tuition_model.py
from app.connection import get_connection

class Tuition:
    """Student model for database operations"""

    @staticmethod
    def get_all():
        """Get all students with program information"""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT
                s.*,
                p.full_name
            FROM tuition_fee s
            LEFT JOIN student p ON s.student_id = p.student_id
        """
        cursor.execute(query)
        students = cursor.fetchall()
        conn.close()
        return students

    @staticmethod
    def get_payments(fee_id):
        """Get payment by ID"""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT *
            FROM payment
            WHERE fee_id = %s
            """
        
        cursor.execute(query,(fee_id,))
        payments = cursor.fetchall()
        conn.close()
        return payments

    @staticmethod
    def search(fee_id, name, semester, status):
        """Search tuition"""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT s.*, p.full_name
            FROM tuition_fee s
            LEFT JOIN student p ON s.student_id = p.student_id
            WHERE 1=1
        """
        values = []

        if fee_id:
            query += " AND s.fee_id = %s"
            values.append(fee_id)
        if name:
            query += " AND s.full_name LIKE %s"
            values.append("%" + name + "%")
        if semester:
            query += " AND s.semester = %s"
            values.append(semester)
        if status:
            query += " AND s.payment_status = %s"
            values.append(status)

        cursor.execute(query, tuple(values))
        tuitions = cursor.fetchall()
        conn.close()
        return tuitions 
    
    @staticmethod
    def delete(fee_id):
        """Delete a tuition"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tuition_fee WHERE fee_id = %s", (fee_id,))
        conn.commit()
        conn.close()
