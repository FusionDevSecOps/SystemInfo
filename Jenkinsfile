
stage 'Access repository'
node {

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
            sh 'python3 test.py'
        }
        else {
            //return "Windows"
            bat label: '', script: 'python test.py'
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
            sh 'coverage run Oscheck.py'
            sh 'coverage html'
        } else {
            //return "Windows"
            bat label: '', script: 'pip install coverage'
            bat label: '', script: 'coverage run Oscheck.py'
            bat label: '', script: 'coverage html'
        }
    }

    stage 'Notify user'
    node {
        notify 'Run successfully'
    }

}
    def notify(status) {
        emailext(
                to: "columcharlton@gmail.com",
                subject: "${status}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>${status}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
        <p>Check console output at <a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a></p>""",
        )
    }
