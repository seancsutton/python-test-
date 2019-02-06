pipeline {
    agent any
     stages {
        stage ('installing py test') {
             steps {
                bash ''' pip install pytest 
                         pip install pytest-cov 
                         pip install pytest-xdist 
                         pip install pytest-bdd
                         pytest --junitxml=$(Build.StagingDirectory)/010.xml
                         
   '''
                }
            }
        }
     
    }