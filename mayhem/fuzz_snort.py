#!/usr/bin/env python3
import struct

import atheris
import sys


import fuzz_helpers

with atheris.instrument_imports():
    from idstools import unified2

from idstools.unified2 import UnknownRecordType
import struct

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        with fdp.ConsumeMemoryFile(all_data=True, as_bytes=True) as log:
            reader = unified2.RecordReader(log)
            for record in reader:
                pass
    except (EOFError, UnknownRecordType, struct.error):
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
