from ctypes import *
from my_debugger_defines import *

import sys
import time
kernel32 = windll.kernel32

class debugger():

    def __init__(self):
        self.h_process = None
        self.pid = None
        self.debugger_active = None
        self.h_thread = None
        self.context = None
        self.breakpoints = {}
        self.first_breakpoint = True
        self.hardware_breakpoints = {}

        system_info = SYSTEM_INFO()
        kernel32.GetSystemInfo(byref(system_info))
        self.page_size = system_info.dwPageSize

        self.guarded_pages = []
        self.memory_breakpoints = {}

    def load(self, path_to_exe):
        creation_flags = DEBUG_PROCESS
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0

        startupinfo.cb = sizeof(startupinfo)

        if kernel32.CreateProcessA(path_to_exe, None, None, None, None, creation_flags, None, None, byref(startupinfo), byref(process_information)):
            print("[*] We have successfully launched the process!")
            print("[*] The Process ID I have is %d" % \
                  process_information.dwProcessId
            self.pid = process_information.dwProcessId)
            self.h_process = self.open_process(self, process_information.dwProcessId)
            self.debugger_active = True
        else:
            print("[*] Error with error code %d." % kernel32.GetLastError())
    
    def open_process(self,pid):
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,pid)

        return h_process
    
    def attatch(self,pid):

        self.h_process = self.open_process(pid)

        if kernel32.DebugActiveProcess(pid):
            self.debugger_active = True
            self.pid = int(pid)
        else:
            print("[*] Uable to attach to the process.")

    def run(self):
        while self.debugger_active == True:
            self.get_debug_event()

    def get_deug_event(self):
        debug_event = DEBUG_EVENT()
        continue_status = DBG_CONTINUE

        if Kernel32.WaitForDebugEvent(byref(debug_event), 100):
            self.h_thread = self.open_thread(debug_event.dwThreadId)
            self.context = self.get_thread_context(h_thread = self.h_thread)
            self.debug_event = debug_event

            print("Event CodeL %d ThreadID: %d" % \
                  (debug_event.dwDebugEventCode,debug_event.dwThreadId))
            

    