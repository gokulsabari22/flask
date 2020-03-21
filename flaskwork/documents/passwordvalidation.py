import re
def validation(register_password):
    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
   
    result1 = re.findall(pattern, register_password)
  

    if result1 :
       return True
    else:
        return False
    
    
        