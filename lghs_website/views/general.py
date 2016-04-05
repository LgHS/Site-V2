from flask import Blueprint, render_template

mod = Blueprint('general', __name__)

@mod.route('/')
def index():
	# if request_wants_json():
	#	 return jsonify(releases=[r.to_json() for r in releases])

	return render_template('general/index.html', section='home')


@mod.route('/contact/')
def contact():
	return render_template('general/contact.html', section='contact')


@mod.route('/members/')
def members():
	return render_template('general/members.html', section='members')
