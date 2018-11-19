import glob
from .gdb_wrapper import GDB_Wrapper

class MJS(object):

    def __init__(self):
        self.mjs_file_name = "test-mjs-fot/mjs_main"
        self.mjs_run_command = "run {}"
        self.mjs_crash_directory = "/home/docker/test-mjs-fot/out*/crash/*"
        self.mjs_triage_directory = "/home/docker/test-mjs-fot/triage/"

    def start(self):
        crash_files = glob.glob(self.mjs_crash_directory)
        crash_files_iter = iter(crash_files)
        gdb_wrapper = GDB_Wrapper(self.mjs_file_name,
                                  self.mjs_run_command, crash_files_iter,
                                  self.mjs_triage_directory)
        gdb_wrapper.start_running_gdb()