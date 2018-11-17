import glob
from .gdb_wrapper import GDB_Wrapper

class NewFot(object):

    def __init__(self):
        self.new_fot_file_name = "test-nm-new-fot/nm-new"
        self.new_fot_run_command = "run -C {}\n"
        self.new_fot_crash_directory = "/home/docker/test-nm-new-fot/out*/crash/*"
        self.new_fot_triage_directory = "/home/docker/test-nm-new-fot/triage/"

    def start(self):
        crash_files = glob.glob(self.new_fot_crash_directory)
        print(len(crash_files))
        crash_files_iter = iter(crash_files)
        gdb_wrapper = GDB_Wrapper(self.new_fot_file_name,
                                  self.new_fot_run_command, crash_files_iter,
                                  self.new_fot_triage_directory)
        gdb_wrapper.start_running