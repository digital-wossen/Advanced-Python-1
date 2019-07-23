
#from mod_conversion import in2cm_table
#l = input()

#sta = int(input('Enter the start:'))
#en = int(input('Enter the end:'))
#ste = int(input('Enter the step size here:'))

#in2cm_table(sta, en, ste )

from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('in2cm.html')