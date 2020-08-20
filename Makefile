black = black -S -l 120 --target-version py38

.PHONY: install
install:
	pip install --progress-bar off -r requirements.txt

.PHONY: black
black:
	$(black) bootstrapform_jinja/ testing/

.PHONY: lint
lint:
	flake8 bootstrapform_jinja/ testing/
	$(black) --check bootstrapform_jinja/ testing/

.PHONY: test
test:
	coverage run --source=bootstrapform_jinja testing/manage.py test

.PHONY: codecov
codecov:
	bash <(curl -s https://codecov.io/bash)

