import doctest
import sys

import lghs_website

HOST = '127.0.0.1'
PORT = 6001

if '--test' in sys.argv:
	doctest.testmod(lghs_website, verbose=True)
else:
	lghs_website.app.run(host=HOST, port=PORT)
