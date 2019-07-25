stage 'Clear workspace and Access repository'
node {
    cleanWs()   //Clean the workspace
    git branch: 'modify',
            url: 'https://github.com/ColmCharlton/SystemInfo'


    stage 'Parallel agents'
    parallel Archival: {
        node('Linux') {
            node {

                git branch: 'modify',
                        url: 'https://github.com/ColmCharlton/SystemInfo'
                // Creates the virtualenv before proceeding
                withPythonEnv('Python3') {

                    //"Linux"
                        sh 'pip install nose'
                        sh 'pip install coverage'

                        stage 'Run tests and code coverage'

                        sh 'nosetests'
                        sh 'coverage run LinuxCommands.py'
                        //sh 'coverage run JsonEdit.py'
                        // sh 'coverage run oScommands.py'
                        sh 'coverage html'
                    }
                }
        }
    }, Notify: {
        node('master') {
            node {
                git branch: 'modify',
                        url: 'https://github.com/ColmCharlton/SystemInfo'

                // Creates the virtualenv before proceeding
                withPythonEnv('Python3') {


                    bat label: '', script: 'pip install nose'
                    bat label: '', script: 'pip install coverage'

                    bat label: '', script: 'nosetests'
                    bat label: '', script: 'coverage run WindowsCommands.py'
                    //bat label: '', script: 'coverage run JsonEdit.py'
                    //bat label: '', script: 'coverage run oScommands.py'
                    bat label: '', script: 'coverage html'
                }
            }


        }
    }
}