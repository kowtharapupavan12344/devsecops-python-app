pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'dir'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run App Test') {
            steps {
                bat 'python app/pythonproj/app.py'
            }
        }
    }
}