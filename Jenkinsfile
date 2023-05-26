pipeline {
    agent any
    
    stages {
        stage('Generowanie Jobów') {
            steps {
                script {
                    // Read the content of IPv6_RUN and IPv6_TST
                    def job1Config = readFile('IPv6_RUN')
                    def job2Config = readFile('IPv6_TST')
                    
                    // Generate IPv6_RUN
                    def job1 = Jenkins.instance.createProject(WorkflowJobFactory, "IPv6_RUN")
                    job1.definitionText = job1Config
                    job1.save()
                    
                    // Generate IPv6_TST
                    def job2 = Jenkins.instance.createProject(WorkflowJobFactory, "IPv6_TST")
                    job2.definitionText = job2Config
                    job2.save()
                }
            }
        }
    }
}