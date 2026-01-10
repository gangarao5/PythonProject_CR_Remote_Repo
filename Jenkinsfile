pipeline {
    agent any

    stages {

        stage('Run API Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat 'python -m pytest tests/api -v'
                }
            }
        }

        stage('Run UI Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat 'python -m pytest tests/ui -v'
                }
            }
        }

        stage('Run Other Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat 'python -m pytest tests/other -v'
                }
            }
        }
    }

    post {
        always {
            echo "All test suites executed"
        }
    }
}




//
//
// pipeline {
//     agent any
//
//     environment {
//         VENV_DIR = "venv"
//         REPORT_DIR = "reports"
//     }
//
//     stages {
//
//         stage('Checkout Code') {
//             steps {
//                 checkout scm
//             }
//         }
//
//         stage('Setup Python Virtual Environment') {
//             steps {
//                 bat '''
//                 python --version
//
//                 if not exist %VENV_DIR% (
//                     python -m venv %VENV_DIR%
//                 )
//
//                 call %VENV_DIR%\\Scripts\\activate
//                 python -m pip install --upgrade pip
//                 pip install -r requirements.txt
//                 '''
//             }
//         }
//
//         stage('Run API Tests') {
//             steps {
//                 bat '''
//                 call %VENV_DIR%\\Scripts\\activate
//                 pytest tests/api -v --disable-warnings
//                 '''
//             }
//         }
//
//         stage('Run UI Tests') {
//             steps {
//                 bat '''
//                 call %VENV_DIR%\\Scripts\\activate
//                 pytest tests/ui -v --disable-warnings
//                 '''
//             }
//         }
//     }
//
//     post {
//
//         always {
//             echo "Archiving test artifacts..."
//
//             archiveArtifacts artifacts: 'reports/**/*.png', allowEmptyArchive: true
//             archiveArtifacts artifacts: '.pytest_cache/**', allowEmptyArchive: true
//         }
//
//         success {
//             echo "✅ Pipeline completed successfully"
//         }
//
//         failure {
//             echo "❌ Pipeline failed – check test results & screenshots"
//         }
//
//         cleanup {
//             echo "Cleaning up workspace"
//         }
//     }
// }
