from app.models.student_model import Student
from app.models.instructor_model import Instructor
from app.models.instructor_model import Instructor
from app.models.instructor_model import Instructor
from app.models.instructor_model import Instructor

class HomeService:
    @staticmethod
    def number_of_student():
        student = Student.get_all()
        number_of_student = len(student)
        return number_of_student
    
    @staticmethod
    def number_of_program():
        None
    
    @staticmethod
    def number_of_course():
        None

    @staticmethod
    def nummber_of_instructor():
        None
    
    @staticmethod
    def x():
        None
    
