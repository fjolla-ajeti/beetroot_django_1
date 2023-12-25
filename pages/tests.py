from django.test import SimpleTestCase
from django.urls import reverse

class HomePageViewTest(SimpleTestCase):

    def test_url_exists_at_correct_loaction(self):
        response=self.client.get("/home/")
        self.assertEqual(response.status_code,200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
    
    def test_template_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response,'<h1>This is home html</h1>')
        

class AboutPageViewTest(SimpleTestCase):
    def test_url_exists_at_correct_loaction(self):
        response=self.client.get("/about/")
        self.assertEqual(response.status_code,200)

        
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code,200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
    
    def test_template_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response,'<h1>This is about html</h1>')