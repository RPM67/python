print("Welcome to email validation program\nhere you can check weather your email is valid or not")
user_email = input("Enter your e-mail : ").strip().lower()
def emailValidation(mail):
    if not (mail.endswith(".com") or mail.endswith(".in")):
        return "Invalid Email.\nWrong domain name entered"
    elif mail.count("@")>1 or mail.count(".")>1:
        return "Invalid Email.\nWrong domain name entered"
    elif not mail.split("@")[0].isalnum():
        return "Invalid Email.\nemail address should not contain special or any other character except for alphabet and numbers"
    elif not mail.split("@")[0][0].isalpha(): # it will pick the first letter of first string splitted by @
        return "Invalid Email.\nemail address should not starts with numeric value"
    else:
        return "Correct Email"
   
print(emailValidation(user_email))