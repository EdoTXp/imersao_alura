# This Dockerfile sets up a Python 3.13.4 environment based on Alpine Linux 3.22.
# It performs the following steps:
FROM python:3.13.4-alpine3.22

# 1. Sets the working directory to /app.
WORKDIR /app

# 2. Copies the requirements.txt file and installs Python dependencies without caching.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copies the rest of the application code into the container.
COPY . .

# 4. Exposes port 8000 for the application.
EXPOSE 8000

# 5. Sets the default command to run the app using Uvicorn on host 0.0.0.0 and port 8000.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]