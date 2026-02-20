pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/kowtharapupavan12344/devsecops-python-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run App Test') {
            steps {
                bat 'python app/app.py'
            }
        }
    }
}