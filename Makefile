build:
	docker build -t birthbot_image .

run:
	docker run -d --name birthbot --env OPENAI_API_KEY --volume /home/BirthBot/birthbot_database:/app/database birthbot_image
	docker exec -d birthbot /bin/sh -c "echo \"nameserver 8.8.8.8\" > /etc/resolv.conf"
	docker exec -d birthbot /bin/sh -c "python3 main.py"

run_debug: stop build
	docker run -d --name birthbot --volume ./db_debug:/app/database --device=/dev/net/tun --cap-add=NET_ADMIN birthbot_image
	docker exec -d birthbot /bin/sh -c "echo \"nameserver 8.8.8.8\" > /etc/resolv.conf"
	docker exec -d birthbot /bin/sh -c "python3 main.py"

open_container:
	docker exec -it birthbot /bin/sh

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