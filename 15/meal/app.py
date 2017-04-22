#!python3
import sqlite3

from flask import Flask, render_template, request

with sqlite3.connect("meal.db") as connection:
	c = connection.cursor()
	try:
		c.execute("""CREATE TABLE meals
				(names TEXT, foods TEXT, drinks TEXT)
				""")		
	except:
		pass

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	info = []
	if request.method == 'POST' and 'name' in request.form:
		name = request.form.get('name')
		food = request.form.get('food')
		drink = request.form.get('drink')
		for i in (name, food, drink):
			info.append(i)
		with sqlite3.connect("meal.db") as connection:
			c = connection.cursor()
			c.execute("INSERT INTO meals VALUES(?, ?, ?)", info)
	return render_template('last_meal.html',
							info=info)
							
@app.route('/meal_history')
def meal_history():
	with sqlite3.connect("meal.db") as connection:
			c = connection.cursor()
	return render_template('meal_history.html',
							c=c)

app.run()
