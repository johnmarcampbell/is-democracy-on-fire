from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
import arrow

app = Flask(__name__)
bootstrap = Bootstrap(app)

def days_until_midterms(date=arrow.utcnow()):
    """Given a date, this function will tell you how many days
    it will be before the next midterm election."""
    election_day = arrow.get('2018-11-06', 'YYYY-MM-DD')
    delta = election_day - date
    return delta.days
    
@app.route('/')
def index():
    return render_template('index.html', midterm_days=days_until_midterms())

if __name__ == '__main__':
    app.run(debug=True)
