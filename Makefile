build:
	docker build -t birthbot_image .

run:
	docker run -d --name birthbot --volume /home/BirthBot/birthbot_database:/app/database birthbot_image -e "OPENAI_API_KEY=${OPENAI_API_KEY}"

run_debug: stop build
	docker run -d --name birthbot --volume ./db_debug:/app/db_debug birthbot_image

stop:
	docker rm -f birthbot

logs:
	docker logs birthbot

lint:
	isort --only-modified --diff .
	black --diff --color .

format:
	isort --only-modified .
	black .