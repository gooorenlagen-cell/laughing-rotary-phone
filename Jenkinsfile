pipeline{
    agent any
    stages{
        stage("Initial"){
            steps{
                script{
                    sh'''
                    ls -l
                    echo Lol
                    '''
                }
            }
        }
    }
    post{
    always{
        cleanWs()
    }
}
}