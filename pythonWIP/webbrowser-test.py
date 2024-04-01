import webbrowser

# this script need to be run as sudo, but there is a security flag that needs to be disabled.

# Specify the path to the Firefox binary
firefox_path = '/usr/bin/firefox'

# Create a new browser controller
b = webbrowser.get(firefox_path + ' %s')

# Open a URL in the specified browser
b.open('http://www.python.org')