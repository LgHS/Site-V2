from . import app
from datetime import datetime

# Note: We're not using strftime's weekday because it relies on local lang.
weekday_name = (
	'monday', 'tuesday', 'wednesday',
	'thursday', 'friday', 'saturday', 'sunday'
)

def hs_is_open(time:datetime=None, opening_hours:dict=None) -> bool:
	"""Indicate if the HS is opened at said time. Only relies on hours.
	
	Args:
		time =
			A date (as datetime.datetime object) you want to know if the HS is open or not.
			Defaults to: datetime.now()
			
		opening_hours = 
			eg: {'monday': (13, 18), 'friday': (5, 7)}  # Tuples are (opening_hour, closing_hour).
			Defaults to: app.config['OPENING_HOURS']
	
	
	If a day when the HS is actually open is provided:
	
	>>> hs_is_open(datetime(2016, 1, 6, 15, 0), {'wednesday': (13, 18)})
	True
	>>> hs_is_open(datetime(2016, 1, 6, 12, 30), {'wednesday': (13, 18)})
	False
	
	If a day when the HS doesn't open at all is provided:
	>>> hs_is_open(datetime.datetime(2016, 1, 7, 15, 30), {'wednesday': (13, 18)})
	False
	"""
	
	if time is None:
		time = datetime.now()
	
	if opening_hours is None:
		opening_hours = app.config['OPENING_HOURS']
	
	start_hour, end_hour = opening_hours.get(
		weekday_name[time.weekday()],  # Retrieve opening hours for said day
		(0, 0)  # will always invalidate if the HS doesn't open on said day
	)
	
	return start_hour <= time.hour < end_hour
