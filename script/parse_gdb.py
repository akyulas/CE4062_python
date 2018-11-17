class GDB_Parser(object):

    def __init__(self, log_file_name, error_signal):
        self.log_file_name = log_file_name
        self.error_signal = error_signal

    def parse_and_get_type_of_bug(self):
        error_type = "Default Error"
        with open(self.log_file_name, 'r') as log_file:
            for line in log_file:
                if self.error_signal in line:
                    error_type = line.replace(self.error_signal, "")
                    break
        return error_type