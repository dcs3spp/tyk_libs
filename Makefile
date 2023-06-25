##
# Setup
##

install:
	poetry install

##
# CLI
##

map_branch:
	poetry run python -m docs.cli.map_branch branch=release-5-lts

##
# Testing
##

behave:
	poetry run behave

pytest:
	poetry run pytest ./tests/unit/

