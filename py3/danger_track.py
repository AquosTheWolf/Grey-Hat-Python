from pydbg import *
from pydbg.defines import *

import utils

MAX_INSTRUCTIONS = 10

dangerous_functions = {
    "strcpy": "msvcrt.dll",
    "strncpy": "msvcrt.dll",
    "sprintf": "msvcrt.dll",
    "vsprintf": "msvcrt.dll"
}

dangerous_functions_resolved = {}
crash_encountered = False
instruction_count = 0

def danger_handler(dbg):
    esp_offset = 0
    while esp_offset <= 20:
        parameter = dbg.smart_deference(dbg.context.Esp + esp_offset)
        print("[ESP + %d] => %s" % (esp_offset, parameter))
        esp_offset += 4

    dng.suspend_all_threads()
    dbg.process_snapshot()
    dbg.resume_all_threads()

    return DBG_CONTINUE
