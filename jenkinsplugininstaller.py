import os

JENKINS_ADMIN = "admin"
JENKINS_PASS = os.popen("cat secrets/initialAdminPassword").read().strip("\n")

os.system('curl -o jenkins-cli.jar -L "http://localhost:8080/jnlpJars/jenkins-cli.jar"')

PLUGINS = ["configuration-as-code", "bootstrap5-api", "caffeine-api", "scm-api", "workflow-step-api", "font-awesome-api"]

for plugin in PLUGINS:
    os.system(f"java -jar jenkins-cli.jar -s http://localhost:8080/ -auth {JENKINS_ADMIN}:{JENKINS_PASS} install-plugin {plugin}")

os.system("systemctl restart jenkins.service")
