import pytest 
from django.test import RequestFactory 
from django.contrib.auth.models import AnonymousUser 
from mixer.backend.django import mixer 
pytestmark = pytest.mark.django_db 
from  app_blog import views 

 

class TestHomeView: 

    def test_anonymous(self):
        req= RequestFactory().get('/') 
        resp=views.HomeView.as_view()(req)
        assert resp.status_code==200, 'Should be callable by an anyone' 



class TestAdminView:
    def test_superuser(self): 
       user = mixer.blend('auth.User',is_superuser=True) 
       req = RequestFactory().get('/') 
       req.user= user 
       resp=views.AdminView.as_view()(req) 
       assert resp.status_code == 200, 'Authenticated user can access' 