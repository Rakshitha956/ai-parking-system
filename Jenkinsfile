pipeline {
    agent any

    stages {

        stage('Check Files') {
            steps {
                bat 'dir'
            }
        }

        stage('Build') {
            steps {
                bat 'javac Main.java Test.java'
            }
        }

        stage('Test') {
            steps {
                bat 'java Test'
            }
        }

        stage('Run') {
            steps {
                bat 'java Main'
            }
        }

    }
}