.PHONY: lint, test

lint:
	bandit -ilr src \
	&& black . \
	&& flake8 examples/ scripts/ src/ tests/ \
	&& mypy --install-types --non-interactive examples/ scripts/ src/ tests/

test:
	echo "done!"