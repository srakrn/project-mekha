class Logger:
    def __init__(self, name):
        self.name = name

    def log(self, message):
        print(f"{self.name}: {message}")


class FileLogger(Logger):
    def __init__(self, file):
        self.file = file

    def log(self, message):
        with open(self.file, "a", encoding="utf-8") as f:
            f.write(f"{message}\n")
