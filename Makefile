run-server:
	poetry run python manage.py runserver

make-migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

setup-hooks:
	poetry run pre-commit install

lint:
	poetry run flake8

test:
	poetry run python manage.py test
