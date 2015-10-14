from app import db


class Visit(db.Model):
    __tablename__ = 'Visits'
    visit_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    referer = db.Column(db.String)
    ip = db.Column(db.String)
    time = db.Column(db.TIMESTAMP)
    browser = db.Column(db.String)

    def __repr__(self):
        return '<visit %r>' % (self.ip)
