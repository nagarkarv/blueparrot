// get list of jenkins plugin. Run this script in the jenkins console
// run this code in http://<jenkins-url>/script
// Save the output into plugins.txt

List<String> JenkinsPlugins = new ArrayList<String>(Jenkins.instance.pluginManager.plugins)

JenkinsPlugins.sort {it.getDisplayName()}
.each{
	plugin -> 
  println("${plugin.getShortName()}:${plugin.getVersion()}")
}
