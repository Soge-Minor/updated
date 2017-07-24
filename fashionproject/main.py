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
    loader= jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

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
    ('/choose_outfit' ChooseOutfitHandler),
    ('/styles_colors', StylesColorsHandler)

], debug=True)
