pipeline {
    agent any

    environment {
        VENV_NAME = 'venv'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    sh "python -m venv ${VENV_NAME}"
                    sh "source ${VENV_NAME}/bin/activate && pip install -r requirements.txt"
                }
            }
        }

        stage('Test') {
            steps {
                sh 'docker run my-flask-app python -m pytest app/tests/'
            }
        }

        stage('Deploy') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${DOCKER_REGISTRY_CREDS}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh "echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin docker.io"
                    sh 'docker push $DOCKER_BFLASK_IMAGE'
                }
            }
        }
      
        post {
            always {
                sh "deactivate" // Deactivate the virtual environment
                sh 'docker logout'
            }
        }
    }
}
