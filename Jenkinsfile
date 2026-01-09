// pipeline {
//     agent any
//
//     stages {
//
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }
//
//         stage('Create & Activate Venv') {
//             steps {
//                 bat '''
//                 python --version
//                 python -m venv venv
//                 call venv\\Scripts\\activate
//                 pip install --upgrade pip
//                 pip install -r requirements.txt
//                 '''
//             }
//         }
//
//         stage('Run Tests') {
//             steps {
//                 bat '''
//                 call venv\\Scripts\\activate
//                 pytest -v
//                 '''
//             }
//         }
//     }
//
//     post {
//         always {
//             echo "Pipeline finished"
//         }
//     }
// }







pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
        REPORT_DIR = "reports"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                bat '''
                python --version

                if not exist %VENV_DIR% (
                    python -m venv %VENV_DIR%
                )

                call %VENV_DIR%\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                pytest tests/api -v --disable-warnings
                '''
            }
        }

        stage('Run UI Tests') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                pytest tests/ui -v --disable-warnings
                '''
            }
        }
    }

    post {

        always {
            echo "Archiving test artifacts..."

            archiveArtifacts artifacts: 'reports/**/*.png', allowEmptyArchive: true
            archiveArtifacts artifacts: '.pytest_cache/**', allowEmptyArchive: true
        }

        success {
            echo "✅ Pipeline completed successfully"
        }

        failure {
            echo "❌ Pipeline failed – check test results & screenshots"
        }

        cleanup {
            echo "Cleaning up workspace"
        }
    }
}
