pipeline {
    agent any

    stages {
        stage("Code") {
            steps {
                echo "Cloning the code"
                git url: "https://github.com/Nishika10/Django-ToDo-App", branch:"autodeploy"
                echo "Code cloned successfully"
            }
        }
        stage("Build") {
            steps {
                echo "Building the code"
                sh "whoami"
                sh "docker build -t todo-app:latest ."
            }
        }
         stage("Push to DockerHub") {
             steps {
                echo "Pushing the image to Docker Hub"
                withCredentials([usernamePassword(
                    credentialsId: "DockerHubCred",
                    usernameVariable:"dockerHubUser",
                    passwordVariable:"dockerHubPass")]){
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass} "
                sh "docker image tag todo-app:latest ${env.dockerHubUser}/todo-app:latest "
                sh "docker push ${env.dockerHubUser}/todo-app:latest"
                }
            }
        }
        stage("Deploy") {
            steps {
                echo "Deploying the code"
                sh "docker compose down && docker compose up -d --build"
                echo "Code deployed successfully"
            }
        }
    }
}
