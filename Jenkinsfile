
stage 'Access repository'
node {
    cleanWs()   //Clean the workspace
    git branch: 'modify',
            url: 'https://github.com/ColmCharlton/SystemInfo'

}


stage 'Run tests in virtual environment'
node{
// Creates the virtualenv before proceeding
    withPythonEnv('Python3') {

        if (isUnix()) {
            //return "Linux"
            sh 'pip install nose'
            sh 'nosetests'
        }
        else {
            //return "Windows"
            // Creates the virtualenv before proceeding
            bat label: '', script: 'pip install nose'
            bat label: '', script: 'nosetests'
        }

    }
}
stage 'Run Scripts in virtual environment'
node{
// Creates the virtualenv before proceeding
    withPythonEnv('Python3') {

        if (isUnix()) {
            //return "Linux"
            sh 'python3 LinuxCommands.py'
        }
        else {
            //return "Windows"
            bat label: '', script: 'python WindowsCommands.py'
        }

    }
}
stage 'Run code coverage in virtual environment'
node {
// Creates the virtualenv before proceeding
    withPythonEnv('Python3') {

        if (isUnix()) {
            //return "Linux"
            sh 'pip install coverage '
            sh 'coverage run LinuxCommands.py'
            //sh 'coverage run JsonEdit.py'
            // sh 'coverage run oScommands.py'
            sh 'coverage html'
        } else {
            //return "Windows"
            bat label: '', script: 'pip install coverage'
            bat label: '', script: 'coverage run WindowsCommands.py'
            //bat label: '', script: 'coverage run JsonEdit.py'
            //bat label: '', script: 'coverage run oScommands.py'
            bat label: '', script: 'coverage html'
        }
    }

    stage('Archival') {
        publishHTML([allowMissing         : true,
                     alwaysLinkToLastBuild: false,
                     keepAll              : true,
                     reportDir            : 'htmlcov',
                     reportFiles          : 'index.html',
                     reportName           : 'Code Coverage',
                     reportTitles         : ''])

        //archiveArtifacts 'target/*.?ar'
        archiveArtifacts allowEmptyArchive: true, artifacts: '*.json'
    }
}


stage 'Notify user'
node {
    notify 'Run successfully'
}


def notify(status) {
    //Notify method sends details to email
    emailext(
            to: "columcharlton@gmail.com",
            subject: "${status}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
            body: """<p>${status}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
        <p>Check console output at <a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a></p>""",
    )
}
