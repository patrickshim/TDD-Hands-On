#2/15/2021
#https://stackoverflow.com/questions/41117733/validation-of-a-password-python

def check_pwd(pwd):
  if len(pwd) < 8:
    return False

  return True