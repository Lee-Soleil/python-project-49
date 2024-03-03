install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games/engine.py
	poetry run flake8 brain_games/scripts/brain_even.py
	poetry run flake8 brain_games/scripts/brain_calc.py
	poetry run flake8 brain_games/scripts/brain_gcd.py
	poetry run flake8 brain_games/scripts/brain_progression.py
	poetry run flake8 brain_games/scripts/brain_prime.py
	poetry run flake8 brain_games/games/even.py
	poetry run flake8 brain_games/games/calc.py
	poetry run flake8 brain_games/games/gcd.py
	poetry run flake8 brain_games/games/progression.py
	poetry run flake8 brain_games/games/prime.py





