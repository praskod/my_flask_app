from flask import render_template
from flask_login import login_required
import pandas as pd

@app.route('/dashboard')
@login_required
def dashboard():
    # Load Titanic dataset
    df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    summary = df.describe().to_html()
    return render_template('dashboard.html', summary=summary)