from login_verifier import verify_login_re

login1 = "asdf_123.asd1-1"
login2 = "AsAf-F"
login3 = "12asdas"

print(verify_login_re(login1))
print(verify_login_re(login2))
print(verify_login_re(login3))