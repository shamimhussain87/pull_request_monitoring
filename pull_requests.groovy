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
        string(name: 'APPNAME', description: 'Application name')
        string(name: 'TEAM_NAME', description: 'Team name')
        string(name: 'APP_TEMPLATE_BRANCH', defaultValue: 'main', description: 'Branch for github.com/motain/paas-go-service-template')
    }

    stages {
        stage('Set build name') {
            steps {
                script {
                    currentBuild.displayName = "#${BUILD_NUMBER}: ${APPNAME}"
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
