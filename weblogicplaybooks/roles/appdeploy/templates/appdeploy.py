connect("weblogic", "weblogic", "t3://localhost:7002")
deploy('SamplePOC','/opt/SamplePOC.war', targets='AdminServer')
startApplication('SamplePOC')
exit()
