try:
    from werkzeug import cached_property
except:
    import werkzeug, importlib
    f = open(werkzeug.__file__, 'a')
    f.write("from .utils import cached_property\n")
    f.close()
    importlib.reload(werkzeug)

try:
    from flask.helpers import _endpoint_from_view_func
except:
    import flask.scaffold
    flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func    
    
from main import *

# Models in models are not initialized if they are not imported, because they are not imported into the main program
from main.model.db_models import *

from main.api import blueprint

app = SingletonApp()  # Get app via singleton to ensure this app is unique in this project.
app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    
