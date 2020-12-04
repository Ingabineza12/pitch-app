from app import create_app,db
from flask_script import Manager, Server
from app.models import User, Role
from flask_migrate import Migrate, MigrateCommand

#Creating app instance
# app = create_app('development')
app = create_app('production')



manager = Manager(app, db)
manager.add_command('server', Server)
manager.add_command('db',MigrateCommand)
migrate = Migrate(app,db)
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Role = Role )

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
