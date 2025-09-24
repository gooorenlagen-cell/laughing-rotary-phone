pipeline{
    agent any
    stages{
        stage{
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