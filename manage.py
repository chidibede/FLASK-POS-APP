from pointofsale import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from pointofsale import models

if __name__ == "__main__":
    manager.run()