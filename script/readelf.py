import glob
from .gdb_wrapper import GDB_Wrapper

class ReadElf(object):

    def __init__(self):
        self.readelf_file_name = "test-readelf-fot/readelf"
        self.readelf_run_command = "run -a {}"
        self.readelf_crash_directory = "/home/docker/test-readelf-fot/out*/crash/*"
        self.readelf_triage_directory = "/home/docker/test-readelf-fot/triage/"

    def start(self):
        crash_files = glob.glob(self.readelf_crash_directory)
        crash_files_iter = iter(crash_files)
        gdb_wrapper = GDB_Wrapper(self.readelf_file_name,
                                  self.readelf_run_command, crash_files_iter,
                                  self.readelf_triage_directory)
        gdb_wrapper.start_running_gdb()