from main import *

# Models in models are not initialized if they are not imported, because they are not imported into the main program
from main.model.db_models import *

from main.api import blueprint

app = SingletonApp()  # Get app via singleton to ensure this app is unique in this project.
app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
