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