pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-creds'  
        IMAGE_NAME = 'hophopp/sentiment-api'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/amalsboui/Sentiment-Analysis-MLOps'
            }
        }

        stage('Check Changes') {
            steps {
                script {
                    if (sh(script: "git diff --name-only HEAD~1 HEAD | grep -E 'FastAPI/|train.py|requirements.txt'", returnStatus: true) != 0) {
                        echo "No relevant changes. Skipping build."
                        currentBuild.result = 'SUCCESS'
                        return
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    pip install --upgrade pip
                    pip install -r requirements.txt pytest httpx
                    export PYTHONPATH=$PWD
                    pytest tests/
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDENTIALS}", passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                        sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                    }
                }
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    sh "docker stop sentiment-api || true"
                    sh "docker rm sentiment-api || true"
                    sh "docker run -d -p 8088:8088 --name sentiment-api ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}