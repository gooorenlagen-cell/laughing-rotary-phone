pipeline {
  agent any

  environment {
    IMAGE_NAME = "my-flask-app"
    DEPLOY_DIR = "/home/deployer/deploy"
    REMOTE = "deployer@YOUR_SERVER_IP"    // замените
    TAR_NAME = "image-${env.GIT_COMMIT}.tar"
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Build image') {
      steps {
        sh """
          docker build -t ${IMAGE_NAME}:${GIT_COMMIT} .
          docker tag ${IMAGE_NAME}:${GIT_COMMIT} ${IMAGE_NAME}:latest
        """
      }
    }

    stage('Save image to tar') {
      steps {
        sh "docker save -o ${TAR_NAME} ${IMAGE_NAME}:${GIT_COMMIT} ${IMAGE_NAME}:latest"
      }
    }

    stage('Copy to server & load & deploy') {
      steps {
        sshagent (credentials: ['deploy-ssh']) {
          sh """
            scp -o StrictHostKeyChecking=no ${TAR_NAME} ${REMOTE}:${DEPLOY_DIR}/
            ssh -o StrictHostKeyChecking=no ${REMOTE} '
              set -e
              cd ${DEPLOY_DIR}
              docker load -i ${TAR_NAME}
              docker-compose up -d --remove-orphans
              rm -f ${TAR_NAME}
            '
          """
        }
      }
    }
  }

  post {
    always {
      sh "rm -f ${TAR_NAME} || true"
      cleanWs()
    }
  }
}
