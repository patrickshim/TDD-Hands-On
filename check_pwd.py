import re
#2/15/2021
#https://stackoverflow.com/questions/41117733/validation-of-a-password-python

def check_pwd(pwd):
  if len(pwd) < 8:
    return False
  elif len(pwd) > 20:
    return False
  #https://www.tutorialspoint.com/How-to-check-if-a-Python-string-contains-only-digits
  elif pwd.isdigit():
    return False
  elif re.search('[a-z]', pwd) is None:
    return False
  elif re.search('[A-Z]', pwd) is None:
    return False
    
  return True