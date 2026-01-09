pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create & Activate Venv') {
            steps {
                bat '''
                python --version
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest -v
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
    }
}
