pipeline{
    agent any
    stages{
        stage('Checkout Code'){
            steps{
                checkout scm

            }
        }

        stage('Extract Data'){
            steps{
                bat "C:\\Users\\adity\\AppData\\Local\\Programs\\Python\\Python312\\python.exe extract.py"

            }
        }
        }
}