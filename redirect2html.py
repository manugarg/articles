from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class RedirectToHtml(webapp.RequestHandler):
  def get(self, url):
    self.redirect('%s.html' % url)

application = webapp.WSGIApplication([('(.*)', RedirectToHtml),
                                     ], debug=True
                                    )


def main():
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
