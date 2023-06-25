##
# Setup
##

install:
	poetry install

##
# CLI
##

map_branch:
	poetry run python -m docs.cli.map_branch branch=$(branch)

##
# Testing
##

behave:
	poetry run behave

pytest:
	poetry run pytest ./tests/unit/

