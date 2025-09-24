pipeline{
    agent any
    stages{
        stage("build"){
            steps{
                script{
                    sh'''
                    docker compose up -d
                    docker compose down
                    '''
                }
            }
        }
    }
    post {
        always{
            cleanWs()
        }
    }
}