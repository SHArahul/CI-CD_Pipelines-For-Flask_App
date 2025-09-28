## CI/CD Pipelines for Flask Application

This repository demonstrates the implementation of Continuous Integration and Continuous Deployment (CI/CD) pipelines for a Flask application using both GitHub Actions and Jenkins. The pipelines automate the deployment process to an Ubuntu EC2 instance, ensuring efficient and reliable application delivery.

# Table of Contents

# Project Overview

# Repository Structure

# Prerequisites

# GitHub Actions CI/CD Pipeline

# Jenkins CI/CD Pipeline

# Deployment Details

# Usage

# Logs & Monitoring

# Contributing

---

# Project Overview

This project showcases a Flask web application with automated CI/CD pipelines:

GitHub Actions: Automates testing and deployment processes.

Jenkins: Provides an alternative CI/CD pipeline for deployment.

EC2 Deployment: Deploys the application to an Ubuntu EC2 instance.

Virtual Environment: Utilizes Python virtual environments to manage dependencies.

Process Management: Runs the Flask application in detached screen sessions for continuous operation.

# Repository Structure

CI-CD_Pipelines-For-Flask_App/
│
├── Myapp/                     # Flask application code
│   ├── app.py                 # Main Flask application
│   ├── requirements.txt       # Python dependencies
│   └── ...                    # Additional application files
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions CI/CD pipeline
│
├── Jenkinsfile                # Jenkins CI/CD pipeline script
├── README.md                  # Project documentation


# Prerequisites

Ensure the following are set up on your EC2 Ubuntu instance:

System Packages
# Update package lists
sudo apt update

# Install essential packages
sudo apt install -y python3 python3-pip python3-venv git screen

# Optional: Upgrade pip
python3 -m pip install --upgrade pip

SSH Access

GitHub Actions:

Set the following secrets in your GitHub repository:

EC2_HOST: EC2 instance public IP or hostname

EC2_USERNAME: EC2 SSH username (e.g., ubuntu)

EC2_SSH_KEY: Private SSH key for EC2 access

Jenkins:

Configure Jenkins credentials for SSH access to the EC2 instance.

GitHub Actions CI/CD Pipeline

The GitHub Actions workflow is defined in .github/workflows/ci-cd.yml. It includes:

Triggers:

On push to main and staging branches

On release creation

Steps:

Checkout code

Set up Python environment

Install dependencies

Run tests using pytest

Deploy to EC2:

Staging: Port 5000

Production: Port 8000

Clean up old Flask processes and logs

Start Flask application in detached screen session

Example deployment step:

screen -dmS flask_staging bash -c "source $HOME/flask_venv/bin/activate && PORT=5000 ENV=dev python Myapp/app.py"

Jenkins CI/CD Pipeline

The Jenkins pipeline is defined in the Jenkinsfile. It includes:

Stages:

Checkout code

Set up Python environment

Install dependencies

Run tests using pytest

Deploy to EC2:

Staging: Port 5000

Production: Port 8000

Clean up old Flask processes and logs

Start Flask application in detached screen session

Example deployment stage:

stage('Deploy to Staging') {
    steps {
        sshagent(['ec2-ssh-key']) {
            sh """
                ssh ubuntu@${EC2_HOST} '
                cd ~/CI-CD_Pipelines-For-Flask_App
                git pull origin staging
                source ~/flask_venv/bin/activate
                pip install -r Myapp/requirements.txt
                pkill -f "python Myapp/app.py" || true
                screen -dmS flask_staging bash -c "source ~/flask_venv/bin/activate && PORT=5000 ENV=dev python Myapp/app.py"
                '
            """
        }
    }
}

Deployment Details
Environment	Branch	Port	Notes
Staging	staging	5000	For testing and development purposes
Production	main	8000	For live application deployment
Usage
Start Flask Locally
cd Myapp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

Run Flask in Detached screen Session on EC2
screen -dmS flask_app bash -c "source ~/flask_venv/bin/activate && PORT=5000 ENV=dev python Myapp/app.py"

Attach to screen Session
screen -r flask_app

Logs & Monitoring

Staging Logs: ~/flask-staging.log

Production Logs: ~/flask-production.log

To view logs:

tail -f ~/flask-staging.log


To stop running Flask sessions:

screen -ls

screen -S flask_app -X quit

---
Screenshots:

triggering the github actions deploy and main branch and deployment of staging and main branch in ec2 server. 

<img width="1912" height="887" alt="triggering main branch and build test" src="https://github.com/user-attachments/assets/9bae564b-a6a5-4ac8-8225-32608cc8ccb4" />

<img width="1918" height="872" alt="prod deploy" src="https://github.com/user-attachments/assets/6b1a44f8-3f5f-4d27-91aa-2d5b457842a3" />

<img width="1917" height="1015" alt="changes reflected on main ec2 machine" src="https://github.com/user-attachments/assets/5b0f196d-2de7-43f1-b5ce-2d487748a4c5" />

<img width="1907" height="877" alt="github action staging and build-test " src="https://github.com/user-attachments/assets/6d28373d-acc0-4347-bbaf-c58f526d5e89" />

<img width="1918" height="995" alt="changes on server ec2" src="https://github.com/user-attachments/assets/719a9ba4-ef98-4b34-b202-ac185472e802" />

<img width="1452" height="193" alt="running flask on ec2 machine port 5000" src="https://github.com/user-attachments/assets/cc37e1dc-0fba-49eb-bce3-6c15e6618e2b" />

<img width="1892" height="340" alt="running flask on port 8000 deploy main" src="https://github.com/user-attachments/assets/b0b7b80b-e25e-401d-8818-eba12fba9024" />

---
Author: Rahul Sharma
