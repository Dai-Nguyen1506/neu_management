# app/services/tuition_service.py
from app.models.tuition_model import Tuition
# from app.utils.validators import validate_student_data, validate_email


class TuitionService:
    """Business logic for tuition operations"""
    @staticmethod
    def get_all_tuition():
        tuitions = Tuition.get_all()
        return tuitions
    
    @staticmethod
    def get_payments_student(fee_id):
        return Tuition.get_payments(fee_id)
    
    @staticmethod
    def search_tuitions(fee_id=None,name=None,semester=None,status=None):
        return Tuition.search(fee_id, name, semester, status)
    
    @staticmethod
    def delete_tuition(fee_id):
        """Delete a tuition"""

        Tuition.delete(fee_id)
        return True, "Student deleted successfully"

