## PyBites Code Challenge 28 - Bokeh + Flask

OK I will admit: time was divided between a PyBites wordcount and doing funky visualizations on a movie data set.

Time allowed for former, latter to be done yet ...

1. I added some code in `get_data.py` to download our complete [PyBites repo](https://github.com/pybites/pybites.github.io-src).

2. I used [Herman's bootstrap code](https://github.com/realpython/flask-bokeh-example/blob/master/tutorial.md) to get started - very helpful.

3. I added labels which was a bit of a challenge (`from bokeh.models import ColumnDataSource, LabelSet`)

TODOs:

4. Add a GET parameter to the Flask route to refresh the GH clone of the repo.

5. Deploy to Heroku using [Julian's tutorial](https://pybit.es/deploy-flask-heroku.html).
