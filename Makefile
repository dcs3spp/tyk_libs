##
# Setup
##

install:
	poetry install

##
# CLI
##

map_branch:
	$(if $(branch),,$(error usage: make branch=<branch_name>))
	@poetry run python -m docs.cli.map_branch branch=$(branch)

find_missing_links:
	@poetry run python -m docs.cli.check_menu_yaml_links || { \
		status=$$?; \
		exit $$status; \
	}

##
# Testing
##

behave:
	poetry run behave

pytest:
	poetry run pytest ./tests/unit/

