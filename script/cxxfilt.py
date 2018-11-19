import glob
from .gdb_wrapper import GDB_Wrapper

class CXXFilt(object):

    def __init__(self):
        self.cxx_filt_file_name = "test-cxxfilt-fot/cxxfilt"
        self.cxx_filt_run_command = "run < {}"
        self.cxx_filt_crash_directory = "/home/docker/test-cxxfilt-fot/out*/crash/*"
        self.cxx_filt_triage_directory = "/home/docker/test-cxxfilt-fot/triage/"

    def start(self):
        crash_files = glob.glob(self.cxx_filt_crash_directory)
        crash_files_iter = iter(crash_files)
        gdb_wrapper = GDB_Wrapper(self.cxx_filt_file_name,
                                  self.cxx_filt_run_command, crash_files_iter,
                                  self.cxx_filt_triage_directory)
        gdb_wrapper.start_running_gdb()