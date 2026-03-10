# Deployment Learning Lab

This repository is a guided hands-on lab to learn:
- post-training artifact handoff
- CI/CD for model-serving systems
- containerization with Docker and Docker Compose
- cloud deployment of an inference API

## Start Here

1. Open and read the notebook: `learning_notebook.ipynb`
2. Implement code only inside markers in starter files:
	- `#start code here`
	- `#send code here`
3. Run your checks locally:
	- `pytest -q`
	- `docker build -t deploy-lab:local .`
	- `docker compose up --build`

## Starter Files You Will Complete

- `app/main.py`
- `app/model_loader.py`
- `tests/test_api.py`
- `requirements.txt`
- `Dockerfile`
- `docker-compose.yml`
- `.github/workflows/ci.yml`
- `.github/workflows/cd.yml`
- `cloud/deploy/cloudrun-service.yaml`
- `cloud/config/dev.env`
- `cloud/config/staging.env`
- `cloud/config/prod.env`

## Learning Flow

1. Reproducibility and post-training contracts
2. Inference API design and latency budgeting
3. Test strategy (unit + integration)
4. Container build and local parity
5. CI quality gates
6. CD artifact promotion and release strategy
7. Config/secrets management
8. Observability, health checks, and rollback

## Notes

- Keep image tags immutable for releases.
- Avoid committing secrets to git.
- Promote the same image digest across environments.
