install:
	poetry install

run:
	poetry run uvicorn payment_platform.__main__:app --reload

db:
	docker exec -it payment-platform-postgres psql -U myuser -d mydatabase

lint:
	poetry run ruff check .

check:
	poetry run black --check .

diff:
	poetry run black --diff .

format:
	poetry run black .

typecheck:
	poetry run mypy .

test:
	poetry run pytest
