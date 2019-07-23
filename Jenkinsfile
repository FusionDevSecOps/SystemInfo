
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
           //return "Linux"
           sh: 'python3 Oscheck.py'
        }
    else {
        return "Windows"
        bat label: '', script: 'python Oscheck.py'
    }
}

stage 'Run tests'
node{
if (isUnix()) {
           //return "Linux"
       sh 'python3 unitTests.py'
    }
    else {
        //return "Windows"
       bat label: '', script: 'python unitTests.py'
    }
       //bat label: '', script: 'python unitTests.py'
       //sh 'python unitTests.py'

}
stage 'Notify user'
node{
	notify 'Run successfully'
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
