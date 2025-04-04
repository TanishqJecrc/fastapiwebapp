pipeline {
    agent any
    environment {
        AZURE_CREDENTIALS_ID = 'azure-service-principal'
        RESOURCE_GROUP = 'rg-jenkins'
        APP_SERVICE_NAME = 'linapptanishq'
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/TanishqJecrc/fastapiwebapp.git'
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                bat "pip install -r requirements.txt"
            }
        }

        stage('Package FastAPI App') {
            steps {
                bat "powershell Compress-Archive -Path ./app.py, ./venv, ./requirements.txt -DestinationPath ./deploy.zip -Force"
            }
        }

        stage('Deploy') {
            steps {
                withCredentials([azureServicePrincipal(credentialsId: AZURE_CREDENTIALS_ID)]) {
                    bat "az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID"
                    bat "az webapp deploy --resource-group $RESOURCE_GROUP --name $APP_SERVICE_NAME --src-path ./deploy.zip --type zip"
                }
            }
        }
    }
     post {
        success {
            echo 'Deployment Successful!'
        }
        failure {
            echo 'Deployment Failed!'
        }
    }
}
