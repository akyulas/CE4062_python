import glob
from .gdb_wrapper import GDB_Wrapper

class XED(object):

    def __init__(self):
        self.xed_file_name = "test-xed-fot/xed-func"
        self.xed_run_command = "run -xv 0 -v 0 -i {}"
        self.xed_crash_directory = "/home/docker/test-xed-fot/out*/crash/*"
        self.xed_triage_directory = "/home/docker/test-xed-fot/triage/"

    def start(self):
        crash_files = glob.glob(self.xed_crash_directory)
        crash_files_iter = iter(crash_files)
        gdb_wrapper = GDB_Wrapper(self.xed_file_name,
                                  self.xed_run_command, crash_files_iter,
                                  self.xed_triage_directory)
        gdb_wrapper.start_running_gdb()