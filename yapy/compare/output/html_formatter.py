from yapy.compare.output.formatter import OutputFormatter


class HtmlFormatter(OutputFormatter):

    def __init__(self, plagiarism_compare):
        super().__init__(plagiarism_compare)

    def __draw_header(self):
        headers = self.headers

        header = '<th>Results</th>'

        for element in headers:
            header += f'<th>{element}</th>'

        return f'<tr>{header}</tr>'

    def __draw_row(self, row_id):
        row_data = [self.plagiarism_compare.result[row_id][column]
                    for column in range(0, len(self.plagiarism_compare.result))]

        row = ''

        for element in row_data:
            row += f'<td>{element}</td>'

        return f'<tr><th>{self.headers[row_id]}</th>{row}</tr>'

    def format(self):
        table = self.__draw_header()

        for row in range(0, len(self.plagiarism_compare.result)):
            table += self.__draw_row(row)

        return f'<table>{table}</table>'
