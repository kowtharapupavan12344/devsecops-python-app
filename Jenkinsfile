pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    bat """
                    sonar-scanner ^
                      -Dsonar.projectKey=devsecops-python-app ^
                      -Dsonar.sources=. ^
                      -Dsonar.host.url=http://localhost:9000 ^
                      -Dsonar.login=%SONAR_AUTH_TOKEN%
                    """
                }
            }
        }

        stage('Syntax Check') {
            steps {
                bat 'python -m py_compile app/pythonproj/app.py'
            }
        }
    }
}