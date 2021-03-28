from .formatter import OutputFormatter


class HtmlFormatter(OutputFormatter):

    def __init__(self, content):
        self.content = content

    def format(self):
        return super().format()

    def export(self, path):
        return super().export(path)
