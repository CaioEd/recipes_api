venv:
	venv/Scripts/activate


install:
	pip install -r requirements.txt


migrations:
	python manage.py makemigrations


migrate:
	python manage.py migrate


run:
	python manage.py runserver