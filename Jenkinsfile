pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building AI Parking System...'
                bat 'javac Main.java Test.java'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing AI Parking System...'
                bat 'java Test'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying AI Parking System...'
                bat 'java Main'
            }
        }

    }
}