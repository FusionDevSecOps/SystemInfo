
stage 'Access repository'
node {

    git branch: 'modify', 
    url: 'https://github.com/ColmCharlton/SystemInfo'
		
	}


//stage 'Check os'
//node{

  //  checkOs
//}


stage 'Run Script'
node{

    if (isUnix()) {
           return "Linux"
        }
    else {
        return "Windows"
    }

    //sh: 'python Oscheck.py'
    bat label: '', script: 'python Oscheck.py'
    }

stage 'Notify user'
node{
	notify 'Ran!'
	}

stage 'Run tests'
node{
       bat label: '', script: 'python unitTests.py'
       //sh 'python unitTests.py'

}


def notify(status){
    emailext (
      to: "columcharlton@gmail.com",
      subject: "${status}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
      body: """<p>${status}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
        <p>Check console output at <a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a></p>""",
    )
}

def checkOs(){
    if (isUnix()) {
           return "Linux"
        }
    else {
        return "Windows"
    }
}