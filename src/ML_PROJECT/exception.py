import sys
from src.ML_PROJECT.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message
#it extracts the exact filename and line number where a bug occurred so you can find it instantly.

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details)

    def __str__(self):
        return self.error_message


#It takes the filename, line number, and the error message (like "Access Denied") and builds one clean, readable sentence
#super().__init__(error_message): This tells the original Python Exception class, "Hey, I'm taking over now, but keep the basic error message
#self.error_message = ...: It calls your "Detective" function and stores that detailed sentence (File + Line + Message) inside the object
# end "Whenever someone tries to print this error or show it in the terminal, show them my detailed custom message instead of the default one."


# when error occurs somehwere try catch send two things   the error itself (ex) and the entire Python system state (sys).
#e is the Error Object

'''Imagine your MySQL password is wrong.

What e contains: The specific error code and message from the database.

The actual value of e in this case: (1045, "Access denied for user 'root'@'localhost' (using password: YES)")'''

#