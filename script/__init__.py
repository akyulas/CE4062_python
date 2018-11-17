from .new_fot import NewFot

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
    print(file_number)
    if file_number == '6':
        new_fot_obj = NewFot()
        new_fot_obj.start()