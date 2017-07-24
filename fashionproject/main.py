import logging
import os
import jinja2
import json
import urllib
import urllib2
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader= jinja2.FileSystemLoader(
        os.path.dirname(__file__) + '/templates')
        )

class MainHandler(webapp2.RequestHandler):
    def get(self):
        cur_user = users.get_current_user()
        log_url = ''
        if cur_user:
            log_url = users.create_logout_url('/homepage')
        else:
            log_url = users.create_login_url('/')
        template = jinja_environment.get_template('main.html')
        var = {
            'user' :cur_user,
            'log_url': log_url
        }
        self.response.out.write(template.render(var))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class ChooseOutfitHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class StylesColorsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/homepage', HomePageHandler),
    ('/choose_outfit', ChooseOutfitHandler),
    ('/styles_colors', StylesColorsHandler)

], debug=True)
