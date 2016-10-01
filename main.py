import htmlPy
import os
from Handler import backend

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = htmlPy.AppGUI(title=u"Sample application", developer_mode=True)
app.maximized = False

app.static_path = os.path.join(BASE_DIR, "UI/static/")
app.template_path = os.path.join(BASE_DIR, "UI/template/")

app.bind(backend.BackEnd())

app.template = ("index.html", {})

if __name__ == "__main__":
    app.start()