from django.test import RequestFactory
from .. import views

class TestHomeView:
    def test_anonymous(self):
        req=RequestFactory.get('/')
        resp=views.HomeView.as_view(req)
        assert resp.status_code==200,'should be callable by anyone'


class CommentView:
    def test_anonymous(self):
        req=RequestFactory.get('/')
        resp=views.comment_page(req)
        assert resp.status_code==200,'should be callable by anyone'