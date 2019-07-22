
stage 'Access repository'
node {

    git branch: 'modify', 
    url: 'https://github.com/ColmCharlton/SystemInfo'
		
	}

stage 'Run Script'
node{
	bat label: '', script: 'python Oscheck.py'

	stage 'Notify user'
	node{
	notify 'Ran!'
	}
}
//stage 'Run tests'
//node{
//       sh 'python test.py'
 //     }


def notify(status){
    emailext (
      to: "columcharlton@gmail.com",
      subject: "${status}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
      body: """<p>${status}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
        <p>Check console output at <a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a></p>""",
    )
}