from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title> revenue</title>
</head>
<body>
<h1 align="center">Top Software Companies in Revenue</h1>
<h3>
<table border="5" cellspacing="5" cellpadding="5" width="1000" height="500" align="center">

<tr>

<th><h2>Rank</h2></th>
<th><h2>IT Services Company name</h2></th>
<th><h2>Revenue in 2022(₹ Cr)</h2></th>	
	
</tr>

<tr>
<td>1</td>
<td>Tata Consultancy Services</td>
<td>195,772</td>
</tr>
<tr>
<td>2</td>
<td>Infosys</td>
<td>123,936	</td>
</tr>
<tr>
<td>3</td>
<td>HCL Technologies		</td>
<td>85,651</td>
</tr>
<tr>
<td>4</td>
<td>Wipro		</td>
<td>79,093</td>
</tr>
<tr>
<td>5</td>
<td>Tech Mahindra	</td>
<td>38,642</td>
</tr>
</table>
</h3>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
