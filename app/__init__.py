from flask import Flask
from app import views, models

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='views')
app.config.from_object('config')
db = SQLAlchemy(app)

print("db loaded")


import datetime
from flask import request, make_response, render_template


from app.models.User import User
from app.models.Visit import Visit



@app.route('/')
def main_function():

    user_id = request.cookies.get('user_id')

    templ = render_template('index.html')
    resp = make_response(templ)

    if user_id is None:
        user = User()

        db.session.add(user)
        db.session.commit()

        app.logger.debug(user.id)
        user_id = user.id
        resp.set_cookie('user_id', str(user_id))
    else:
        print(user_id)


    visit = Visit(user_id = user_id, referer = request.referrer, ip = request.remote_addr, time = datetime.datetime.now(), browser = request.user_agent.string)
    db.session.add(visit)
    db.session.commit()
    return resp



