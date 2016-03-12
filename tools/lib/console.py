class Console():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def colorize(self, color, text):
        return color + text + self.ENDC

    def ok(self, text):
        return self.colorize(self.OKGREEN, text)

    def err(self, text):
        return self.colorize(self.FAIL, text)

    def bold(self, text):
        return self.colorize(self.BOLD, text)

    def title(self, text):
        return self.colorize(self.HEADER, text)

    def working(self, text):
        return self.colorize(self.WARNING, text)