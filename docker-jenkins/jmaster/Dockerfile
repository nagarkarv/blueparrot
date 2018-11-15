FROM jenkins/jenkins:lts
# Setup plugins that we want to install
COPY plugins-config/plugins.txt /usr/share/jenkins/ref/plugins.txt
# Disable setup wizard
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
# Setup security and admin user
COPY plugins-config/security.groovy /usr/share/jenkins/ref/init.groovy.d/security.groovy
# Setup docker plugin
COPY plugins-config/dockerplugin.groovy /usr/share/jenkins/ref/init.groovy.d/dockerplugin.groovy

# Install all plugins
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt