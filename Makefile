install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl --force

brain-games:
	uv run brain-games

lint:
	uv run ruff check brain_games
