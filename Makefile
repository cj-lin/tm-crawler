format:
	autoflake -ir --remove-all-unused-imports .
	isort .
	black .

lint:
	flake8
