import subprocess
from .parse_gdb import GDB_Parser

class GDB_Wrapper(object):

    def __init__(self, test_file_name, run_command, crash_files_iter, crash_files_triage_dir):
        self.test_file_name = test_file_name
        self.run_command = run_command
        self.crash_files_iter = crash_files_iter
        self.crash_files_triage_dir = crash_files_triage_dir

    def start_running_gdb(self):
        start_command = "gdb %s" % self.test_file_name
        gdb = subprocess.Popen([start_command], stdin=subprocess.PIPE)
        self.get_and_log_bt(gdb)

    def get_and_log_bt(self, gdb):
        for crash_file in self.crash_files_iter:
            temp_run_command = self.run_command.replace("{}", crash_file)
            gdb.stdin.write("set logging overwrite on\n")
            gdb.stdin.write("set logging file mylog.txt\n")
            gdb.stdin.write("set logging on\n")
            gdb.stdin.write(temp_run_command)
            gdb.stdin.write("bt\n")
            gdb.stdin.write("set logging off\n")
            type_of_bug = self.get_type_of_bug()


    def get_type_of_bug(self):
        gdb_parser = GDB_Parser()
        return gdb_parser.parse_and_get_error()


