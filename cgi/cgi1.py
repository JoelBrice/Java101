import cgi
import cgitb; cgitb.enable()

print("Content-Type: text/html \n\n")

Form = cgi.FieldStorage()

print(Form['greeting'].value, Form['user'].value)
