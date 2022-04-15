from flask.cli import FlaskGroup
import sys
from project import app

cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()