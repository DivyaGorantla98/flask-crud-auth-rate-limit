# Containerized Flask CRUD App

This is a simple Flask-based CRUD application, containerized with Docker. It includes JWT-based authentication, rate limiting, and instructions for local testing and deployment.

## Features

- **CRUD Operations** on in-memory items (for demonstration).
- **JWT Authentication** for protected endpoints.
- **Rate limiting** (100 requests/hour by default).

## Project Structure

├── .gitignore
├── Dockerfile
├── requirements.txt
├── README.md
├── src
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── auth_utils.py
│   ├── controllers.py
│   └── models.py
└── tests
    └── test_app.py


## How to Use ##

1. Clone the repo

git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Install dependencies
pip install -r requirements.txt

3. Run the app locally
python src/app.py
Then visit http://localhost:5000/ping in your browser or Postman to verify it's running.

4. Generate a JWT Token
In a Python shell:

>>> from src.auth_utils import generate_token
>>> generate_token(123)
'eyJhbGciOiJIUzI1...'
Use this token with Bearer <token> in the Authorization header when accessing protected routes.

5. Docker Build & Run

docker build -t flask-crud-app .
docker run -p 5000:5000 flask-crud-app
Again, check http://localhost:5000/ping.

6. Testing

python -m unittest discover -s tests

You should see:

.
----------------------------------------------------------------------
Ran 1 test in X.XXXs

OK

Deployment to the Cloud (AWS Example)

1. Push image to Amazon ECR:

docker build -t flask-crud-app .
docker tag flask-crud-app:latest <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/flask-crud-app:latest
docker push <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/flask-crud-app:latest
2. Create an ECS Fargate task definition referencing that image, and run a service with port 5000 exposed.
3. Access your service via the load balancer or public IP.

License
MIT or your preferred license.

</details>

---

## 2.4 `Dockerfile`

Instructions to build a Docker image running the Flask app.

<details>
<summary><strong>Dockerfile content</strong></summary>

```dockerfile
# Use Python 3.9 slim as a base
FROM python:3.9-slim

# Create a working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY src /app/src

# Expose port 5000
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application
CMD ["python", "-m", "flask", "run", "--port=5000"]
