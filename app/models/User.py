from app import db


class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        return '<user %r>' % (self.id)
