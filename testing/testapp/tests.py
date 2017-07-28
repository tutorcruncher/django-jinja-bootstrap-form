import os
from django import VERSION as DJANGO_VERSION
from django.test import TestCase, Client
from django.conf import settings

GEN_HTML = bool(os.getenv('GEN_HTML', False))

if DJANGO_VERSION >= (1, 11):
    FIXTURES_DIR = 'fixtures_11'
elif DJANGO_VERSION >= (1, 10):
    FIXTURES_DIR = 'fixtures_10'
else:
    FIXTURES_DIR = 'fixtures'


class BootstrapJinjaTemplateTagTests(TestCase):
    maxDiff = None

    def assertHTMLEqualToFixture(self, response, file_name):
        html_file = os.path.join(settings.BASE_DIR, FIXTURES_DIR, file_name)
        content = response.content.decode()
        if not os.path.exists(html_file) and GEN_HTML:
            print('WARNING: file "%s" missing, generating it' % file_name)
            with open(html_file, 'w') as f:
                f.write(content)
            return
        with open(html_file) as f:
            model_content = f.read()

        self.assertHTMLEqual(content, model_content)

    def test_simple_form(self):
        client = Client()
        response = client.get('/simple_bs_form/')
        self.assertContains(response, '<div class="form-group">', status_code=200)
        self.assertHTMLEqualToFixture(response, 'basic.html')

    def test_horizontal_form(self):
        client = Client()
        response = client.get('/horizontal_bs_form/')
        self.assertContains(response, '<div class="form-group">', status_code=200)
        self.assertHTMLEqualToFixture(response, 'horizontal.html')

    def test_partial_form(self):
        client = Client()
        response = client.get('/partial_bs_form/')
        self.assertContains(response, '<div class="form-group">', status_code=200)
        self.assertHTMLEqualToFixture(response, 'partial.html')

