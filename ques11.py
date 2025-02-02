class Logger:
    def log(self, message, message_type=None):
        if message_type == 'error':
            self.log_error(message)
        elif message_type == 'warning':
            self.log_warning(message)
        elif message_type == 'info':
            self.log_info(message)
        else:
            print(f"Log: {message}")

    def log_error(self, message):
        print(f"Error: {message}")

    def log_warning(self, message):
        print(f"Warning: {message}")

    def log_info(self, message):
        print(f"Info: {message}")

# Example Usage
logger = Logger()
logger.log("This is a general log message")
logger.log("This is an error message", "error")
logger.log("This is a warning message", "warning")
logger.log("This is an info message", "info")
