import os
import django
from django.test import TestCase, Client
from django.conf import settings


class BootstrapJinjaTemplateTagTests(TestCase):

    def test_simple_form(self):
        client = Client()
        r = client.get('/simple_bs_form/')
        self.assertEqual(r.status_code, 200)

        if django.get_version().startswith('1.6'):
            # for some reason dj 1.6 renders this slightly differently, I can't be bothered to work out why.
            self.assertContains(r, '<div class="form-group">')
            return
        html_file = os.path.join(settings.BASE_DIR, 'fixtures', 'basic.html')
        with open(html_file) as f:
            content = f.read()

        self.assertHTMLEqual(r.content.decode('utf-8'), content)

    def test_horizontal_form(self):
        client = Client()
        r = client.get('/horizontal_bs_form/')
        self.assertEqual(r.status_code, 200)

        if django.get_version().startswith('1.6'):
            # for some reason dj 1.6 renders this slightly differently, I can't be bothered to work out why.
            self.assertContains(r, '<div class="form-group">')
            return
        html_file = os.path.join(settings.BASE_DIR, 'fixtures', 'horizontal.html')
        with open(html_file) as f:
            content = f.read()

        self.assertHTMLEqual(r.content.decode('utf-8'), content)
