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
    while esp_offset <= 20:
        parameter = dbg.smart_deference(dbg.context.Esp + esp_offset)