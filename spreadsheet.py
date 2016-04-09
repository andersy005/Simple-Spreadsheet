import cherrypy
import os.path

current_dir = os.path.dirname(os.path.abspath(__file__))


class Root(object):
    spreadsheet = '''<!DOCTYPE html>
<html>
<head>
	<title></title>
	<link rel="stylesheet" type="text/css" href="static/css/redmond/jquery-ui-1.8.1.custom.css" media="screen, projection">
	<script type="text/javascript" src="static/jquery-1.4.2.js" ></script>
    <script type="text/javascript" src="static/jquery-ui-1.8.1.custom.min.js" ></script>
    <script type="text/javascript" src="static/jeditable.min.js"></script>
    <script type="text/javascript" src="spreadsheet.js"></script>
</head>

<body id="spreadsheet_example">
<div id="example">
<p id = "logging"> hello
</p>
<script type="text/javascript">
    $("example").sheet({cols:8, rows:10});
</script>
</div>

</body>
</html>'''

    @cherrypy.expose
    def index(self):
        return Root.spreadsheet

if __name__ == "__main__":

    cherrypy.quickstart(Root(),config={
        '/static':
            {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': os.path.join(current_dir, "static")
            },
        '/spreadsheet.js':
            {
                'tools.staticfile.on': True,
                'tools.staticfile.filename': os.path.join(current_dir, "spreadsheet.js")

            }
    })