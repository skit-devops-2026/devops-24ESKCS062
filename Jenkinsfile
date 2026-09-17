pipeline {
    agent any

    stages {

        stage('Install') {
            steps {
                bat 'make install'
            }
        }

        stage('Test') {
            steps {
                bat 'make test'
            }
        }

        stage('Build') {
            steps {
                bat 'make build'
            }
        }
    }
}