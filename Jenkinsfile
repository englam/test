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

        stage('print test') {
          steps {
            echo '123'
          }
        }

      }
    }

    stage('Test') {
      steps {
        echo 'Test Finish haha'
      }
    }

  }
  environment {
    englam1 = '123'
    engalm2 = '456'
  }
}