pipeline {

    agent any

    environment {
        dockerhub_registry = '6419/attendance_app_bynet'
        dockerhub_credential = credentials('dockerhub')
        dockerImage = ''
        github_credential = 'a0bb4e47-f112-4b84-9e36-1fb1d2239d7e'
        github_url = 'https://github.com/linoyh/Attendance-project.git'
        test_cerdentials =
        prod_cerdentials =
    }

    stages {
        stage ('Git Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'master']],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [[$class: 'CleanCheckout']],
                    submoduleCfg: [],
                    userRemoteConfigs: [[url: github_url]]
                ])
            }
        }
        stage ('Build BE Image') {
            steps {
                script {
                    dockerImage = docker.build dockerhub_registry + ":latest"
                }
            }
        }
        stage ('push to dockerhub') {
            steps {
               script {
                    docker.withRegistry( '', dockerhub_credential) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage ('pull from dockerHub') {
            steps {
               script {
                    docker.withRegistry( '', dockerHubRegistryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage ('test') {
            steps {
               script {
                sshagent {
                    sh """ssh -o StrictHostKeyChecking=no -l ec2user test curl 127.0.0.1:5000""" )
                    }
                }
            }
        }
        stage ('prod') {
            steps {
               script {

                    }
                }
            }
        }
        stage ('Clean Memory') {
            steps {
                sh "docker rmi $dockerhub_registry:latest"
            }
        }
    }

    post {
        always {
            emailext to: "linoyhevron@gmail.com",
                     subject: "Jenkins build: ${currentBuild.currentResult}: ${env.JOB_NAME}",
                     body: "${currentBuild.currentResult}: Job ${env.JOB_NAME}\nMore Info can be found here: ${env.BUILD_URL}"
        }
    }
}