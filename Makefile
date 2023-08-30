.PHONY: clean

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

tests:
	coverage run -m pytest
	coverage report -m

migrate:
	cd logs && nohup python ../manage.py es_migrate -u -i requirement -s '2019-01-01' -e '2021-12-30'&
	cd logs && nohup python ../manage.py es_migrate -u -i requirement_detail -s '2021-01-01' -e '2021-12-30'&
	cd logs && nohup python ../manage.py es_migrate -u -i purchase_plan -s '2019-01-01' -e '2021-12-30'&
	cd logs && nohup python ../manage.py es_migrate -u -i purchase_plan_detail -s '2021-01-01' -e '2021-12-30'&
	cd logs && nohup python ../manage.py es_migrate -u -i transfer_plan -s '2019-01-01' -e '2021-12-30'&
	cd logs && nohup python ../manage.py es_migrate -u -i transfer_plan_detail -s '2021-01-01' -e '2021-12-30'&
	cd logs && nohup python ../manage.py es_migrate -u -i purchase_order -s '2019-01-01' -e '2021-12-30'&
	cd logs && nohup python ../manage.py es_migrate -u -i purchase_order_detail -s '2019-01-01' -e '2021-12-30'&
	cd logs && nohup python ../manage.py es_migrate -u -i purchase_order_receive -s '2019-01-01' -e '2021-12-30'&
	cd logs && nohup python ../manage.py es_migrate -u -i purchase_order_receive_detail -s '2021-01-01' -e '2021-12-30'&

all: clean tests run

init:
	python3 -m venv venv