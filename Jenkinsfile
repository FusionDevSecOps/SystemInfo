    stage Linux: {
        node('Linux') {

            git branch: 'modify',
                    url: 'https://github.com/ColmCharlton/SystemInfo'
            // Creates the virtualenv before proceeding
            withPythonEnv('Python3') {

                stage 'Install dependencies'
                node('Linux') {
                    sh 'pip install nose'
                    sh 'pip install coverage '
                }
                stage 'Run tests and code coverage'
                node('Linux') {

                    sh 'nosetests'
                    sh 'coverage run LinuxCommands.py'
                    //sh 'coverage run JsonEdit.py'
                    // sh 'coverage run oScommands.py'
                    sh 'coverage html'
                }
            }
        }
    }
