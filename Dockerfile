# Container recipe for inference API

#start code here
# TODO: choose a secure, slim Python base image
FROM python:3.12-slim

# TODO: set workdir
WORKDIR /app

# TODO: copy and install requirements with cache-friendly order
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# TODO: copy application code
COPY app/ ./app/
COPY artifacts/ ./artifacts/
COPY tests/ ./tests/

# TODO: expose service port
EXPOSE 8000

# TODO: define startup command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
#send code here
