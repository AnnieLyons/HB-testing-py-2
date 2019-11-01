from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///testdb"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # FIXME: write a function that creates a game and adds it to the database.
    
    game = Game(name="Ticket", description="a cross-country train adventure")

    db.session.add(game)
    db.session.commit()

if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")



# Ticket to Ride| a cross-country train adventure
# Power Grid| supply the most cities with power
# Amazing Labyrinth| move around the shifting paths of the labyrinth in a race to collect various treasures
# Princes of Florence| attract artists and scholars trying to become the most prestigious family in Florence
# Agricola | farmers sow, plow the fields, collect wood, and feed their families