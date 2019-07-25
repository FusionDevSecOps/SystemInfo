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

                    stage 'Install dependencies'
                    node {
                        sh 'pip install nose'
                        sh 'pip install coverage '
                    }
                    stage 'Run tests and code coverage'
                    node {

                        sh 'nosetests'
                        sh 'coverage run LinuxCommands.py'
                        //sh 'coverage run JsonEdit.py'
                        // sh 'coverage run oScommands.py'
                        sh 'coverage html'
                    }
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


                    stage 'Install dependencies'
                    node {
                        bat label: '', script: 'pip install nose'
                        bat label: '', script: 'pip install coverage'

                    }
                    stage 'Run tests and code coverage'
                    node {

                        bat label: '', script: 'nosetests'
                        bat label: '', script: 'coverage run WindowsCommands.py'
                        //bat label: '', script: 'coverage run JsonEdit.py'
                        //bat label: '', script: 'coverage run oScommands.py'
                        bat label: '', script: 'coverage html'
                    }
                    stage('Archival')
                    node {
                        publish 'windows.json'

                    }
                    stage 'Notify user'
                    node {
                        notify 'Run successfully'
                    }
                }
            }


        }
    }
}
