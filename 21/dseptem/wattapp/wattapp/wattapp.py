import webbrowser
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, flash, request, redirect
from sqlalchemy import desc
from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField
from wtforms.validators import DataRequired
from datetime import datetime

"""
wattapp! A wattage consumption cost calculator
"""

__author__ = "Dante Septem"
__version__ = "0.4"
__license__ = "MIT"

app = Flask(__name__)
app.config.from_object('conf')
db = SQLAlchemy(app)


class WattageCostForm(FlaskForm):
    """The form for the calculator, with handy validators to avoid empty fields or invalid inputs"""
    consumption = FloatField('consumption', validators=[DataRequired()])
    hours = IntegerField('hours', validators=[DataRequired()], default=1)
    cost_per_kwh = FloatField('cost_per_kwh', validators=[DataRequired()])


class WattageCostQuery(db.Model):
    """Model of a query
    Pretty much self describing"""
    id = db.Column(db.Integer, primary_key=True)
    consumption = db.Column(db.Float())
    hours = db.Column(db.Integer())
    cost_per_kwh = db.Column(db.Float())
    total_cost = db.Column(db.Float())
    query_date = db.Column(db.DateTime())

    def __init__(self, consumption, hours, cost_per_kwh):
        self.consumption = consumption
        self.hours = hours
        self.cost_per_kwh = cost_per_kwh
        self.total_cost = wattage_cost(consumption, cost_per_kwh, hours)
        self.query_date = datetime.now().replace(microsecond=0)

    def __repr__(self):
        return 'Query Date: {} | Device consumption: {self.consumption}w | Hours used: {self.hours} | Cost per kW/h: ${self.cost_per_kwh} | Total cost: ${self.total_cost}'.format(datetime.strftime(self.query_date, "%H:%M:%S %d/%m/%Y"), self=self)


@app.route('/', methods=['GET', 'POST'])
def wtc_calculator():
    """Main page of the app
    Presents the WTForm for the consumption cost calculation
    When the user presses 'Calculate Cost', the query gets added to the DB and a message is displayed with the total
    cost, or the user is asked to fill all fields if some where empty or erroneous
    Also provides a button to check the history"""
    form = WattageCostForm()

    if form.validate_on_submit():
        query = WattageCostQuery(
            request.form['consumption'],
            request.form['hours'],
            request.form['cost_per_kwh'],
        )
        try:
            db.session.add(query)
            db.session.commit()
            flash('Total cost: ${}'.format(wattage_cost(
                request.form['consumption'],
                request.form['cost_per_kwh'],
                request.form['hours']
            )))
        except:
            db.session.rollback()
    if form.errors:
        flash('All fields must be completed, only with numbers')
    return render_template('wtc_calculator.html',
                           form=form)


@app.route('/history', methods=['GET'])
def wtc_history():
    """Renders the template for the user's calculation history
    The template provides buttons to:
        * Delete single records
        * Clear all history
        """
    history = db.session.query(WattageCostQuery).order_by(desc(WattageCostQuery.query_date))
    if not history.first():
        history = None
    return render_template('wtc_history.html',
                           history=history)


@app.route('/clearhistory', methods=['POST'])
def clear_wtc_history():
    """Clears all queries from the DB, then return to the main page"""
    try:
        WattageCostQuery.query.delete()
        db.session.commit()
        flash('History cleared')
    except:
        db.session.rollback()
    return redirect('/')


@app.route('/deleterecord/<id_num>', methods=['POST'])
def delete_wtc_record(id_num):
    """Gets the query ID number from the url, then deletes it from the database and goes back to history page"""
    try:
        WattageCostQuery.query.filter_by(id=id_num).delete()
        db.session.commit()
        flash('Record deleted')
    except:
        db.session.rollback()
    return redirect('history')


def wattage_cost(consumption, cost_per_kwh, hours=1):
    """Returns the total cost of using a device for hours specified, according to the cost per kW/h provided"""
    return round(float(consumption) * int(hours) / 1000 * float(cost_per_kwh), 2)


def main():
    """ Main entry point of the app
     Creates the database if it doesn't exist, then starts the app and opens it in the user's default browser """
    db.create_all()
    webbrowser.open('http://127.0.0.1:5000')
    app.run()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
