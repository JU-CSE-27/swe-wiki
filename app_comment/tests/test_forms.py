from django.test import SimpleTestCase
from app_comment.forms import commentForm

class TestForms(SimpleTestCase):
    def test_expense_form_valid_data(self):

        form=commentForm(data={'m_comments':'pizza is tasty'})

        """
        form = commentForm(data= {
            'user':'Ritu'
            'm_comments':'pizza is tasty'
            'm_comment_date':'Jan. 8, 2022, 8:44 a.m.'
             })"""

        

        self.assertTrue(form.is_valid())

    def test_expense_form_no_data(self):
        form=commentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)