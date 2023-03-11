from rest_framework.exceptions import APIException


class UsernameFieldRequired(APIException):
    default_detail = "Username field is required"
    

class FirstNameFieldRequired(APIException):
    default_detail = "First Name field is required"
    
    
class LastNameFieldRequired(APIException):
    default_detail = "Last Name field is required"


class EmailFieldRequired(APIException):
    default_detail = "Email field is required"
    
