pipeline {
    agent any

    options {
        timestamps()                 // show timestamps in logs
        disableConcurrentBuilds()     // avoid parallel runs
        buildDiscarder(logRotator(
            numToKeepStr: '10',
            artifactNumToKeepStr: '10'
        ))
    }

    environment {
        VENV_DIR = "venv"
        PYTHON = "python"
        REPORT_DIR = "reports"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Cloning source code from Git"
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo "Creating virtual environment and installing dependencies"
                bat """
                %PYTHON% -m venv %VENV_DIR%
                %VENV_DIR%\\Scripts\\pip install --upgrade pip
                %VENV_DIR%\\Scripts\\pip install -r requirements.txt
                """
            }
        }

        stage('Static Code Check (Optional)') {
            steps {
                echo "Running flake8 / pylint"
                bat """
                %VENV_DIR%\\Scripts\\pip install flake8
                %VENV_DIR%\\Scripts\\flake8 .
                """
            }
        }

        stage('Run Unit / API Tests') {
            steps {
                echo "Executing API tests"
                bat """
                %VENV_DIR%\\Scripts\\pytest tests/api \
                -v \
                --junitxml=%REPORT_DIR%\\api_results.xml
                """
            }
        }

        stage('Run UI Automation Tests') {
            steps {
                echo "Executing Selenium UI tests"
                bat """
                %VENV_DIR%\\Scripts\\pytest tests/ui \
                -v \
                --html=%REPORT_DIR%\\ui_report.html \
                --self-contained-html
                """
            }
        }

        stage('Archive Reports') {
            steps {
                echo "Preparing reports for archiving"
                dir("${REPORT_DIR}") {
                    bat "dir"
                }
            }
        }
    }

    post {

        always {
            echo "Pipeline execution completed"

            // Archive all reports
            archiveArtifacts artifacts: 'reports/**/*', fingerprint: true

            // Publish JUnit results (for Jenkins Test Result Trend)
            junit allowEmptyResults: true, testResults: 'reports/**/*.xml'
        }

        success {
            echo "✅ Build SUCCESS"
            // Example: send mail / slack (optional)
        }

        failure {
            echo "❌ Build FAILED"
        }

        unstable {
            echo "⚠️ Build UNSTABLE"
        }

        cleanup {
            echo "Cleaning workspace"
            cleanWs()
        }
    }
}
