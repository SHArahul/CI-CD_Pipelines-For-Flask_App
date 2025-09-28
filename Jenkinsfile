pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'which python3 || sudo apt-get update && sudo apt-get install -y python3 python3-pip'
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r Myapp/requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest Myapp/ --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Deploy') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo 'Deploying Flask App to Staging...'
                sh 'echo "Deployment step (replace with actual deployment commands)"'
            }
        }
    }


    post {
        success {
            mail(to: 'besegi4437@bitmens.com', 
                 subject: "Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The build was successful. Check the details at ${env.BUILD_URL}")
        }
        failure {
            mail(to: 'besegi4437@bitmens.com', 
                 subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The build failed. Check the details at ${env.BUILD_URL}")
        }
    }
}       