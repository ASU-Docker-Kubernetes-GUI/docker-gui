"""
app.py serves as the root of the Docker/Kubernetes GUI application.
This file imports create_application and calls it in main.
"""
from app import create_application
import logging
app = create_application()

if __name__ == "__main__":
    logging.info('App running on localhost')
    app.run(debug=True, host='0.0.0.0')
