# from datetime import datetime
# from . import app, db

# db.Model.metadata.reflect(db.engine)

# class User(db.Model):
#   __table_args__ = {'extend_existing': True}
#   userid = db.Column(db.Integer, primary_key=True)
#   fname = db.Column(db.String(20), nullable=False)
#   lname = db.Column(db.String(20), nullable=False)
#   password = db.Column(db.String(60), nullable=False)
#   email = db.Column(db.String(120), nullable=False)
#   phone = db.Column(db.String(20), nullable=False)

#   def __repr__(self):
#     return  f"User('{self.fname}', '{self.lname}')," \
#             f"'{self.password}', '{self.email}','{self.phone}')"
