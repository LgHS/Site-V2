from flask import Flask, render_template
from .views import general

app = Flask(__name__)
app.config.from_object('lghs_website.default_config')
app.config.from_envvar('LGHS_WEBSITE_CONFIG', silent=True)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

app.register_blueprint(general.mod)