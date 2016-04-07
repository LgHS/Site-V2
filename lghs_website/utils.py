# Note: Better than relying on strftime which relies on local lang
weekday_int = {
	'monday': 0, 'tuesday': 1, 'wednesday': 2,
	'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6
}
weekday_name = {v:k for k,v in weekday_int}