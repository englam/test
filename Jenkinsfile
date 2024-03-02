pipeline {
  agent any
  stages {
    stage('Check Network') {
      parallel {
        stage('Check Network') {
          steps {
            sh 'ifconfig'
          }
        }

        stage('Check Network2') {
          steps {
            sh 'ifconfig'
          }
        }

      }
    }

    stage('Test') {
      steps {
        echo 'Test Finish'
      }
    }

  }
  environment {
    englam1 = '123'
    engalm2 = '456'
  }
}