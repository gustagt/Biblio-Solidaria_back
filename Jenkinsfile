pipeline {
    agent {
        label 'agent1'
    }
    stages {
        stage('Build Image') {
            steps {
                script{
                    dockerapp = docker.build('gustaug/biblioback:v1', '-f . .')
                }
            }
        }
    }
}
