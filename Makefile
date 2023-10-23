install:
	pip install --upgrade pip && \
		pip install -r requirements.txt
		
test:
	# python -m pytest -vv test_application.py

lint:
	pylint --disable=R,C application.py

deploy:
	echo "Deploying app"
	eb init -p python-3.11 flask-cd --region ap-northeast-2
	eb deploy flask-cd-env

all: install lint test
