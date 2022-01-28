def teamSlug = ''

pipeline {
    agent {
        node {
            label 'master'
        }
    }

    options {
        disableConcurrentBuilds()
    }

    parameters {
        string(name: 'USERNAME', description: 'Github username')
        string(name: 'TOTAL_PRS', description: 'No of pull request in integer')
        string(name: 'APP_TEMPLATE_BRANCH', defaultValue: 'main', description: 'Branch for github.com/motain/paas-go-service-template')
    }

    stages {
        stage('Set username of github user') {
            steps {
                script {
                    currentBuild.displayName = "#${shamimhussain87}: ${APPNAME}"
                }
            }
        }

        stage("Create github repository") {
            environment {
                GITHUB_AUTH_TOKEN = credentials('paas-onefootball-paas-admin-github-token')
            }
            steps {
                script {
                    teamSlug = sh(
                        returnStdout: true,
                        script: './jenkins/paas-create-application-jobs/create-github-repository.py'
                    ).trim()
                }
            }
        }

        stage("Initialize github repository") {
            steps {
                sh "TEAM_SLUG=${teamSlug} ./jenkins/paas-create-application-jobs/initialize-github-repository.sh"
            }
        }
    }

    post {
        cleanup {
            cleanWs()
        }
    }
}
