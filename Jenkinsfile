#!groovy

node {

    try {
        stage 'Checkout'
            checkout scm

            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES')

        stage 'Test'
            //sh 'virtualenv env'
            //sh '. env/bin/activate'
            //sh 'env/bin/pip install -r requirements.txt'
            sh 'python manage.py test'

        stage 'Deploy'
            //sh './deploy_prod.sh'

        stage 'Publish results'
    }

    catch (err) {
        throw err
    }

}
