from flask import Flask, render_template

app = Flask(__name__)

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


@app.route('/')
def hello_world():
    return render_template('home.html', word="World", title="Home")


@app.route('/character')
def character():
    return render_template('character.html', title="Characters", characters=characters)


if __name__ == '__main__':
    app.run()
