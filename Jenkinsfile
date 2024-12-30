pipeline{
    agent{
        node{
            lable 'Jenkins slave node'
        }
    }
    stages{
        stage("checkout code"){
            step{
                giturl:'https://github.com/yashvardhanpatil/my_repo.git', branch: 'main'
            }
        }
        stage("build docker image"){
            step{
                sh "docker build -t myimage ."
            }
        }
        stage("Add tag and push image"){
            step{
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', 
                usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]){
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    sh 'docker tag myimage $DOCKER_USERNAME/myimage'
                    sh 'docker push $DOCKER_USERNAME/myimage'
                }
            }
        }
    }


}
