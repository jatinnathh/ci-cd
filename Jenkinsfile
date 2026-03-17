pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "jatinnath2023bcd0014/2023bcd0014_2023bcd0014"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'hhttps://github.com/jatinnathh/ci-cd'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }
    }
}