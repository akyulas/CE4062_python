import glob
from .gdb_wrapper import GDB_Wrapper

class ObjDump(object):

    def __init__(self):
        self.objdump_file_name = "test-objdump-fot/objdump"
        self.objdump_run_command = "run -x {}"
        self.objdump_crash_directory = "/home/docker/test-objdump-fot/out*/crash/*"
        self.objdump_triage_directory = "/home/docker/test-objdump-fot/triage/"

    def start(self):
        crash_files = glob.glob(self.objdump_crash_directory)
        crash_files_iter = iter(crash_files)
        gdb_wrapper = GDB_Wrapper(self.objdump_file_name,
                                  self.objdump_run_command, crash_files_iter,
                                  self.objdump_triage_directory)
        gdb_wrapper.start_running_gdb()