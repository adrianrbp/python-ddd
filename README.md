# Python DDD Projects
- Domain Driven Design Iterations

## Starting new project
```bash
nix flake init --template "https://flakehub.com/f/the-nix-way/dev-templates/*#python"

nix-shell -p uv
cd snack-machine
uv init
uv venv

uv add ruff black isort --dev
uv add pytest --group test
```