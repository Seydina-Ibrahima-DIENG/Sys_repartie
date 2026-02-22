pipeline {
    agent any
    
    environment {
        // ICI : Mets ton identifiant Docker Hub
        DOCKER_USER = "ibrahima13" 
    }

    stages {
        stage('Nettoyage et Check') {
            steps {
                echo 'Préparation de l environnement...'
                sh 'pip install flake8 || true' 
            }
        }

        stage('Build des images Docker') {
            steps {
                echo 'Construction des images...'
                sh "docker build -t ${DOCKER_USER}/backend:latest ./backend"
                sh "docker build -t ${DOCKER_USER}/frontend:latest ./frontend"
            }
        }

        stage('Push vers Docker Hub') {
            steps {
                echo 'Envoi des images vers Docker Hub...'
                // On utilise l'ID 'docker-hub-creds' que tu as créé dans l'interface Jenkins
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_LOGIN')]) {
                    sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_LOGIN} --password-stdin"
                    sh "docker push ${DOCKER_USER}/backend:latest"
                    sh "docker push ${DOCKER_USER}/frontend:latest"
                }
            }
        }

        stage('Déploiement automatique') {
            steps {
                echo 'Mise à jour du cluster Kubernetes...'
                // On applique les fichiers YAML
                sh 'kubectl apply -f k8s/ --validate=false'
                
                // On force le redémarrage pour charger les nouvelles images poussées sur le Hub
                sh 'kubectl rollout restart deployment backend'
                sh 'kubectl rollout restart deployment frontend'
            }
        }
    }
}
