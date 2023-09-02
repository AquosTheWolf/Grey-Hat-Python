#Please see the books for the previous iterations of this file, as this file will only contain the final version included in the src file from the books website
import my_debugger
from my_debugger_defines import *

debugger = my_debugger.debugger()

pid = input("Enter the PID of the process to attach to: ")

debugger.attach(int(pid))

printf = debugger.func_resolve(b"msvcrt.dll","printf")
print("[*] Address of printf: 0x%08x" % printf)
debugger.bp_set_mem(printf,10)

debugger.run()