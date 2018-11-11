#!groovy
 
import jenkins.model.*
import hudson.security.*
import jenkins.security.s2m.AdminWhitelistRule
 
def instance = Jenkins.getInstance()
 
def hudsonRealm = new HudsonPrivateSecurityRealm(false)

// only usefull when using docker swarm
//def user = new File("/run/secrets/jenkins-user").text.trim()
//def password = new File("/run/secrets/jenkins-pass").text.trim()

def user = "admin"
def password = "admin"

hudsonRealm.createAccount(user, password)
instance.setSecurityRealm(hudsonRealm)
 
def strategy = new FullControlOnceLoggedInAuthorizationStrategy()
instance.setAuthorizationStrategy(strategy)
instance.save()
 
Jenkins.instance.getInjector().getInstance(AdminWhitelistRule.class).setMasterKillSwitch(false)