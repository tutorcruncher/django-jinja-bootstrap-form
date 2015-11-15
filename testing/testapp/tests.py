import os
from django.test import TestCase, Client
from django.conf import settings

GEN_HTML = bool(os.getenv('GEN_HTML', False))


class BootstrapJinjaTemplateTagTests(TestCase):
    maxDiff = None

    def _complare_html(self, r, file_name):
        html_file = os.path.join(settings.BASE_DIR, 'fixtures', file_name)
        if not os.path.exists(html_file) and GEN_HTML:
            print('WARNING: file "%s" missing, generating it' % file_name)
            with open(html_file, 'w') as f:
                f.write(r.content.encode())
            return
        with open(html_file) as f:
            content = f.read()

        self.assertHTMLEqual(content, r.content.decode())

    def test_simple_form(self):
        client = Client()
        r = client.get('/simple_bs_form/')
        self.assertContains(r, '<div class="form-group">')

        self._complare_html(r, 'basic.html')

    def test_horizontal_form(self):
        client = Client()
        r = client.get('/horizontal_bs_form/')
        self.assertContains(r, '<div class="form-group">')

        self._complare_html(r, 'horizontal.html')

    def test_partial_form(self):
        client = Client()
        r = client.get('/partial_bs_form/')
        self.assertContains(r, '<div class="form-group">')

        self._complare_html(r, 'partial.html')

