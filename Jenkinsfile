pipeline {

  agent any
  
  stages {
  
    stage("Build") {
    
      steps {
        echo 'building the application...'
        sh """
            docker build -t node-app:$BUILD_NUMBER .
        """
      }
    }
      
    stage("Publish") {
          
      steps {
        echo 'Publishing the aplication...'
      }
    }
      
    stage("Deploy") {
          
      steps {
        echo 'deploying the aplication...'
        sh """
            docker service update --image node-app:$BUILD_NUMBER welcomeTA 
        """
      }
    }
  }
}
