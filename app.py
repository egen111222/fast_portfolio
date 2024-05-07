from flask import Flask,render_template
from models import db
from dotenv import load_dotenv
import os
from flask_admin import Admin
from models import Note
from flask_admin.contrib.sqla import ModelView

load_dotenv()

app = Flask(__name__,
            static_url_path="")
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB"]
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(Note, db.session))

if __name__ == "__main__":
    app.run()
