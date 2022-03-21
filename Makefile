POETRY = poetry run
PROJECT_FOLDER = backend
PYTEST_FLAGS = --ff -rfs
TEST_TARGET = tests


## @ Help
.PHONY: help
help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make [target]\033[36m\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "\033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)


## @ Application
.PHONY: run
run:  ## Start Program
	@echo "Rodando a aplicação!"

## @ Tests
.PHONY: test coverage
test:  ## Run tests with pytest
	@$(POETRY) pytest $(PYTEST_FLAGS) $(TEST_TARGET)

coverage:  ## Run tests, make report and open into browser
	@$(POETRY) pytest $(PYTEST_FLAGS) --cov=. --cov-report=html $(TEST_TARGET)
	@wslview ./htmlcov/index.html || xdg-open ./htmlcov/index.html || powershell.exe Invoke-Expression ./htmlcov/index.html

## @ Format
.PHONY: black isort format
black:  ## Format python files from project with black
	@$(POETRY) black $(PROJECT_FOLDER) $(TEST_TARGET) --color

isort:  ## Sort imports with isort
	@$(POETRY) isort $(PROJECT_FOLDER) $(TEST_TARGET)

format: black isort ## Format project files with tools: black, isort

## @ Lint
.PHONY: flake lint_black lint_isort lint
lint_black:  ## Run black in check mode
	@$(POETRY) black $(PROJECT_FOLDER) $(TEST_TARGET) --color --check

lint_isort:  ## Run isort in check mode
	@$(POETRY) isort $(PROJECT_FOLDER) $(TEST_TARGET) --check

flake:  ## Run flake8 on project
	@$(POETRY) flake8 $(PROJECT_FOLDER) $(TEST_TARGET)

lint: lint_black lint_isort flake  ## Run lint with tools: black, isort, flake8

## @ Clean
.PHONY: clean clean_python_cache clean_coverage_cache clean_pytest_cache
clean_coverage_cache: ## Remove coverage cache files
	@rm -rf htmlcov
	@rm -rf .coverage

clean_python_cache:  ## Remove python cache files
	@find . -name "__pycache__" -exec rm -rf {} +
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +

clean_pytest_cache:  ## Remove pytest cache files
	@ rm -rf .pytest_cache

clean: clean_python_cache clean_coverage_cache clean_pytest_cache ## Remove Cache files
