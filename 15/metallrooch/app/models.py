from app import db

class Something(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    text = db.Column(db.String(1000))

    def __repr__(self):
        return 'Title {}'.format(self.title)