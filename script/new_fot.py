import glob

class NewFot(object):

    def __init__(self):
        self.new_fot_file_name = "nm-new"
        self.new_fot_run_command = "run -C {}\n"
        self.new_fot_crash_directory = "/home/docker/test-nm-new-fot/out*/crash/*"

    def start(self):
        print(glob.glob(self.new_fot_crash_directory))