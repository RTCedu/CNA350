import virtualbox
import time
vbox = virtualbox.VirtualBox()
#print("VM(s):\n + %s" % "\n + ".join([vm.name for vm in vbox.machines]))
vm = vbox.find_machine('UbuntuMini')
vm.launch_vm_process()
session = vm.create_session()
time.sleep(30)
session.console.keyboard.put_keys('zak')
session.console.keyboard.put_keys(['ENTER'])
time.sleep(0.5)
session.console.keyboard.put_keys('zak')
session.console.keyboard.put_keys(['ENTER'])

time.sleep(30)

session.console.power_down()