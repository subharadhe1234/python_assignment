import os

class LogFileRotator:
    def __init__(self, log_file, max_size):
        """
        Initialize the log rotator.

        :param log_file: Path to the current log file.
        :param max_size: Maximum size of the log file in bytes.
        """
        self.log_file = log_file
        self.max_size = max_size

    def write_log(self, message):
        """
        Write a message to the log file and rotate if necessary.

        :param message: The message to be written.
        """
        # Check if the log file exceeds the size limit
        if os.path.exists(self.log_file) and os.path.getsize(self.log_file) >= self.max_size:
            self.rotate_log()

        with open(self.log_file, 'a') as log:
            log.write(message + '\n')

    def rotate_log(self):
        """
        Rotate the current log file by renaming it.
        """
        for i in range(5, 0, -1):  # Keep up to 5 rotated logs
            old_file = f"{self.log_file}.{i}"
            next_file = f"{self.log_file}.{i + 1}"

            if os.path.exists(old_file):
                os.rename(old_file, next_file)

        # Rename the current log file to .1
        rotated_file = f"{self.log_file}.1"
        os.rename(self.log_file, rotated_file)

# Example usage
if __name__ == "__main__":
    log_rotator = LogFileRotator("app.log", 1 * 1024 * 1024)  # 1MB size limit

    # Simulate log writes
    for i in range(100):
        log_rotator.write_log(f"Log message {i + 1}")

    print("Log rotation simulation complete.")
