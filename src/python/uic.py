import re
import sys

from utils import is_installed

if __name__ == '__main__':
    if is_installed('PySide6'):
        from PySide6.scripts.pyside_tool import uic as main
    elif is_installed('PyQt6'):
        from PyQt6.uic.pyuic import main
    elif is_installed('PyQt5'):
        from PyQt5.uic.pyuic import main
    else:
        raise ModuleNotFoundError(
            'No Qt for Python module with uic tool is installed.'
        )
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
