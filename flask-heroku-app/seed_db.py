import pandas as pd
from app import db, models

df = pd.read_csv('titanic.csv')
for index, row in df.iterrows():
    user = models.User(username=row['Name'], password='default_password')
    db.session.add(user)
db.session.commit()
