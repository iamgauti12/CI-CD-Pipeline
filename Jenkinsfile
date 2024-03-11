def deployToRemoteInstance() {
  script {
    sh '''
      ssh -i ~/.ssh/id_rsa ubuntu@172.31.89.27 \
      "docker pull $DOCKER_BFLASK_IMAGE && \
      docker stop myfirstcontainer || true && \
      docker rm myfirstcontainer || true && \
      docker run -d -p 5000:5000 --name myfirstcontainer $DOCKER_BFLASK_IMAGE"
    '''
  }
}

pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        sh 'docker build -t my-flask-app .'
        sh 'docker tag my-flask-app $DOCKER_BFLASK_IMAGE'
      }
    }
    stage('Test') {
      steps {
        sh 'docker run my-flask-app python -m pytest app/tests/'
      }
    }
    stage('Deploy to Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${DOCKER_REGISTRY_CREDS}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
          sh "echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin docker.io"
          sh 'docker push $DOCKER_BFLASK_IMAGE'
        }
      }
    }
    stage('Deploy to Remote Instance') {
      steps {
        deployToRemoteInstance()
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}
