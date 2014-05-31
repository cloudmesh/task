
start:
#	sudo rabbitmq-server -detached
	celery worker --app=cloudmesh_task -l info

stop:
	sudo rabbitmqctl stop


kill:
	ps auxww | grep 'celery worker' | awk '{print $2}' | xargs kill -9

halt:
	ps auxww | grep 'celery worker' | awk '{print $2}' | xargs kill
