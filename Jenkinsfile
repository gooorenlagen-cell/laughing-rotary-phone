pipeline{
    agent any
    stages{
        stage("Initial"){
            steps{
                script{
                    sh'''
                    ls -l
                    '''
                }
            }
        }
    }
}
post{
    always{
        cleanWs()
    }
}