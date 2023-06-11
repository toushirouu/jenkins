import org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition
import org.jenkinsci.plugins.workflow.job.WorkflowJob


pipeline {
    agent any

    stages {
        stage('Generowanie Jobów') {
            steps {
                script {
                    // Read the content of IPv6_RUN and IPv6_TST
                    def job1Config = readFile('IPv6_RUN')
                    def job2Config = readFile('IPv6_TST')

                    // Delete IPv6_RUN if it already exists
                    def existingJob1 = Jenkins.instance.getItemByFullName("IPv6_RUN")
                    if (existingJob1) {
                        existingJob1.delete()
                    }

                    // Create IPv6_RUN
                    def job1 = Jenkins.instance.createProject(WorkflowJob.class, "IPv6_RUN")
                    job1.definition = new CpsFlowDefinition(job1Config, true)
                    job1.save()

                    // Delete IPv6_TST if it already exists
                    def existingJob2 = Jenkins.instance.getItemByFullName("IPv6_TST")
                    if (existingJob2) {
                        existingJob2.delete()
                    }

                    // Create IPv6_TST
                    def job2 = Jenkins.instance.createProject(WorkflowJob.class, "IPv6_TST")
                    job2.definition = new CpsFlowDefinition(job2Config, true)
                    job2.save()
                }
            }
        }
    }
}