import yate
import os
os.chdir('/Users/esteban/Repos/learn-python/hfpython/chapter07/webapp')

# The CGI Standard States that every web response must start with a header line
# that indictes the type of data included in the request

print(yate.start_response())
# Content-type: text/html

print(yate.start_response('text/plain'))
# Content-type: text/plain

print(yate.start_response('application/json'))
# Content-type: application/json

print(yate.include_header('Welcome to the home'))
# <html>
# <head>
# <title>Welcome to the home</title>
# <link type="text/css" rel="stylesheet" href="/coach.css" />
# </head>
# <body>
# <h1>Welcome to the home</h1>

print(yate.include_footer({ 'Home': '/index.html', 'Select': '/cgi-bin/select.py' }))
# <p>
# <a href="/index.html">Home</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/cgi-bin/select.py">Select</a>&nbsp;&nbsp;&nbsp;&nbsp;
# </p>
# </body>
# </html>

print(yate.start_form('/cgi-bin/process-athlete.py'))
# <form action="/cgi-bin/process-athlete.py" method="POST">

print(yate.end_form())
# <p></p><input type=submit value="Submit"></form>

print(yate.end_form('Click to Confirm your order'))
# <p></p><input type=submit value="Click to Confirm your order"></form>

for fab in ['John', 'Paul', 'George', 'Ringo']:
	print(yate.radio_button(fab, fab))
# <input type="radio" name="John" value="John"> John<br />
# <input type="radio" name="Paul" value="Paul"> Paul<br />
# <input type="radio" name="George" value="George"> George<br />
# <input type="radio" name="Ringo" value="Ringo"> Ringo<br />

print(yate.u_list(['Life of Brian', 'Holy Grail']))
# <ul><li>Life of Brian</li><li>Holy Grail</li></ul>

print(yate.header('Welcome to the home'))
# <h2>Welcome to the home</h2>

print(yate.header('Generates 5 level header', 5))
# <h5>Generates 5 level header</h5>

print(yate.para('Chunk of text in here...'))
# <p>Chunk of text in here...</p>
