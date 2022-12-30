from flask import Flask, render_template, request, flash, url_for, redirect
from forms import SignUpForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///authors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "secret"
db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), default="")

    def __init__(self, name, title, content):
        self.name = name
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Author %r' % self.id


db.create_all()
db.session.commit()

characters = [
    {
        "character": "Arthurius",
        "power": "Telepathy",
        "weapon": "Sword",
        "description": "Really smart but grades are pretty low, which is surprising because he should be able to read "
                       "his professors' minds during a test. Maybe he chooses not to. He's also super-friendly and "
                       "kind."
    },
    {
        "character": "Fantasia",
        "power": "Telekinesis",
        "weapon": "Crossbow",
        "description": "Shy and likes to play with talking raccoons."
    },
    {
        "character": "Obsidian",
        "power": "Invisibility",
        "weapon": "Spear",
        "description": "No one knows for sure who Obsidian really is. This boy just popped out of nowhere one day. "
                       "Many people suspect that he's always been around, silently staring at everyone."
    }
]


@app.route('/', methods=['GET'])
def list_authors():
    authors = Author.query.all()
    return render_template('list_authors.html', authors=authors, title="Fun Animal Facts")


@app.route('/add_authors', methods=['GET'])
def add_authors():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['title'] or not request.form['content']:
            flash('Please enter all the fields', 'error')
        else:
            author = Author(request.form['name'], request.form['title'], request.form['content'])

            db.session.add(author)
            db.session.commit()
            flash('Thanks for the awesome info!')
            return redirect(url_for('list_authors'))
        return render_template('add.html', title='Add New Author')


@app.route('/character')
def character():
    return render_template('character.html', title="Characters", characters=characters)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template("userdata.html", result=result)
    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run()
