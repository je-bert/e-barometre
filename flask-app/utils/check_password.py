import re

regex = "^[A-Za-z\d]{3,50}$"
# Minimum eight characters, at least one letter and one number:

# "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
 
def check_password(password):
  return password != None and re.fullmatch(regex, password)