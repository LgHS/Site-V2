from datetime import datetime
from flask import Flask, render_template
from .views import general

app = Flask(__name__)
app.config.from_object('lghs_website.default_config')
app.config.from_envvar('LGHS_WEBSITE_CONFIG', silent=True)


@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404


@app.context_processor
def is_open():
	open_hours = (
        # day_of_week, start_hour, end_hour
		(2, 19, 23),
		(6, 13, 18),
	)
	now = datetime.now()
	for day, start_hour, end_hour in open_hours:
		if day == now.weekday() and start_hour <= now.hour < end_hour:
			return {"is_open" : True}
	return {"is_open": False}


app.register_blueprint(general.mod)