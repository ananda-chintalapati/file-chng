connect('weblogic','weblogic', 't3://localhost:7002')
print ''
print '======================================================'
print 'The script has been connected to the Admin Server'
print '======================================================'
print ''

edit()
startEdit()

# Machine-1 = the new WebLogic Machine
cmo.createUnixMachine('Machine-1')

cd('/Machines/Machine-1/NodeManager/Machine-1')
cmo.setListenAddress('localhost')


activate()
exit()

