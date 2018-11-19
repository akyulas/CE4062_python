import glob
from .gdb_wrapper import GDB_Wrapper

class Strings(object):

    def __init__(self):
        self.strings_file_name = "test-strings-fot/strings"
        self.strings_run_command = "run {}"
        self.strings_crash_directory = "/home/docker/test-strings-fot/out*/crash/*"
        self.strings_triage_directory = "/home/docker/test-strings-fot/triage/"

    def start(self):
        crash_files = glob.glob(self.strings_crash_directory)
        crash_files_iter = iter(crash_files)
        gdb_wrapper = GDB_Wrapper(self.strings_file_name,
                                  self.strings_run_command, crash_files_iter,
                                  self.strings_triage_directory)
        gdb_wrapper.start_running_gdb()