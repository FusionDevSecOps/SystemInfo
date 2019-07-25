stage 'Clear workspace and Access repository'
node {
    cleanWs()   //Clean the workspace
    git branch: 'modify',
            url: 'https://github.com/ColmCharlton/SystemInfo'


    stage 'Parallel agents'
    parallel Linux: {
        node('Linux') {
            node('Linux') {

                git branch: 'modify',
                    url: 'https://github.com/ColmCharlton/SystemInfo'

                // Creates the virtualenv before proceeding
                withPythonEnv('Python3') {

                    //"Linux"

                    node('Linux') {
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
        }
    }, Windows: {
        node('win') {
            node('win') {
                git branch: 'modify',
                        url: 'https://github.com/ColmCharlton/SystemInfo'

                // Creates the virtualenv before proceeding
                withPythonEnv('Python3') {


                    //"Windows"
                    stage 'Install dependencies'
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