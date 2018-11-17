import subprocess
from shutil import copyfile
from .parse_gdb import GDB_Parser
import os
from time import sleep

class GDB_Wrapper(object):

    def __init__(self, test_file_name, run_command, crash_files_iter, crash_files_triage_dir):
        self.test_file_name = test_file_name
        self.run_command = run_command
        self.crash_files_iter = crash_files_iter
        self.crash_files_triage_dir = crash_files_triage_dir

    def start_running_gdb(self):
        start_command = "gdb"
        gdb = subprocess.Popen([start_command, self.test_file_name], stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.get_and_log_bt(gdb)

    def get_and_log_bt(self, gdb):
        for crash_file in self.crash_files_iter:
            temp_run_command = self.run_command.replace("{}", crash_file)
            gdb.stdin.write(b"set logging overwrite on\n")
            gdb.stdin.flush()
            gdb.stdin.write(b"set logging file mylog.txt\n")
            gdb.stdin.flush()
            gdb.stdin.write(b"set logging on\n")
            gdb.stdin.flush()
            gdb.stdin.write(temp_run_command.encode('utf-8'))
            gdb.stdin.flush()
            gdb.stdin.write(b"bt\n")
            gdb.stdin.flush()
            gdb.stdin.write(b"set logging off\n")
            gdb.stdin.flush()
            type_of_bug = self.get_type_of_bug()
            crash_file_name = self.get_name_of_crash_file(crash_file)
            dest_dir = self.create_dir_if_no_exist(type_of_bug, crash_file_name)
            self.copy_log_file(dest_dir, "mylog.txt")
            self.copy_crash_input(dest_dir, crash_file, crash_file_name)


    def get_type_of_bug(self):
        gdb_parser = GDB_Parser("mylog.txt", "Program received signal ")
        return gdb_parser.parse_and_get_type_of_bug()

    def create_dir_if_no_exist(self, type_of_bug, crash_file_name):
        destination_directory = self.crash_files_triage_dir + type_of_bug + \
                                "/" + crash_file_name + "/"
        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
        except:
            raise OSError("directory creation failed")
        return destination_directory

    def copy_log_file(self, destination_directory, log_file):
        back_trace_file = destination_directory + "bt.txt"
        copyfile(log_file, back_trace_file)

    def copy_crash_input(self, destination_directory, crash_file, crash_file_name):
        destination_file = destination_directory + crash_file_name
        copyfile(crash_file, destination_file)

    def get_name_of_crash_file(self, crash_file_dir):
        elements_of_dir = crash_file_dir.split("/")
        return elements_of_dir[-1]

