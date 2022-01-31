import pytest 

pytestmark = pytest.mark.django_db 

from app_blog import forms 
 

class TestPostForm: 

   def test_form(self): 
        form = forms.blogForm(data={}) 
        assert form.is_valid() is False, ('Should be invalid if no data given' )
        
        
        form = forms.blogForm(data={'m_content':'Hello world...!!',' m_title': 'CSE-27','m_slug':'helloworld','m_createdAt':'1-31-2022','m_uploadTo':'1-31-2022'}) 
        assert form.is_valid() is True , 'Should be valid when data is given'



       