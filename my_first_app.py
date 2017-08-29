import webapp2

class HomePage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<h3>Hello World!</h3><br/><p>This is a test page</p>
		


app = webapp2.WSGIApplication([
	('/'. HomePage)],debug=True)
