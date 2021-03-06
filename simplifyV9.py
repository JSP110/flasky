import os
from app import create_app, db

if __name__ == '__main__':
	app = create_app(os.getenv('FLASK_CONFIG') or 'default')  # For testing in PC
	app.run(host='0.0.0.0', port = 80)