#!d:\lenovo\desktop\client-python\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'aioconsole==0.3.1','console_scripts','apython'
__requires__ = 'aioconsole==0.3.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('aioconsole==0.3.1', 'console_scripts', 'apython')()
    )
