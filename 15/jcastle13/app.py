from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rootpage():
    weight = 0.0
    height = 0.0
    bmi = 0.0
    if request.method == 'POST' and 'userweight' in request.form:
        weight = request.form.get('userweight')
        height = request.form.get('userheight')
        #print("Height:", height)
        '''Check if height is a valid number (i.e. floating value)'''
        if isfloat(height):
            if isfloat(weight):
                height = float(height) * float(height)
                weight = float(weight) / float(height)
                bmi = float(weight) * 703
            else:
                weight = "Not a valid weight value!!"
                #bmi = str(bmi)
                #bmi = "Cannot calculate BMI"
        else:
            height = "Not a valid height value!!"
            #bmi = str(bmi)
            #bmi = "Cannot calculate BMI"


        #print("Update height:", height)
    return render_template("index.html", weight = weight, height = height, bmi = bmi)

''' Function to detect if a string is a valid floating value'''
def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False


if __name__ == "__main__":
    app.run()


