from .nm_new import NM_New
from .cxxfilt import CXXFilt
from .objdump import ObjDump
from .xed import XED
from .mjs import MJS
from .readelf import ReadElf
from .strings import Strings

if __name__ == '__main__':
    print("Please choose a file number to triage")
    print("1. test-cxxfilt-fot")
    print("2. test-objdump-fot")
    print("3. test-xed-fot")
    print("4. test-mjs-fot")
    print("5. test-readelf-fot")
    print("6. test-nm-new-fot")
    print("7. test-strings-fot")
    file_number = input("What's the file number that you want to triage?")
    if file_number == '1':
        cxxfilt_obj = CXXFilt()
        cxxfilt_obj.start()
    elif file_number == '2':
        objdump_obj = ObjDump()
        objdump_obj.start()
    elif file_number == '3':
        xed_obj = XED()
        xed_obj.start()
    elif file_number == '4':
        mjs_obj = MJS()
        mjs_obj.start()
    elif file_number == '5':
        readelf_obj = ReadElf()
        readelf_obj.start()
    elif file_number == '6':
        nm_new_obj = NM_New()
        nm_new_obj.start()
    elif file_number == '7':
        strings_obj = Strings()
        strings.start()
    else:
        print("please run again and choose a valid number.")