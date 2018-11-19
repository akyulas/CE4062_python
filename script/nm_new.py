import glob
from .gdb_wrapper import GDB_Wrapper

class NM_New(object):

    def __init__(self):
        self.nm_new_file_name = "test-nm-new-fot/nm-new"
        self.nm_new_run_command = "run -C {}"
        self.nm_new_crash_directory = "/home/docker/test-nm-new-fot/out*/crash/*"
        self.nm_new_triage_directory = "/home/docker/test-nm-new-fot/triage/"

    def start(self):
        crash_files = glob.glob(self.nm_new_crash_directory)
        crash_files_iter = iter(crash_files)
        gdb_wrapper = GDB_Wrapper(self.nm_new_file_name,
                                  self.nm_new_run_command, crash_files_iter,
                                  self.nm_new_triage_directory)
        gdb_wrapper.start_running_gdb()