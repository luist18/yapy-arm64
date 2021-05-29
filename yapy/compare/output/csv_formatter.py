from yapy.compare.output.formatter import OutputFormatter


class CSVFormatter(OutputFormatter):

    def __init__(self, plagiarism_compare):
        super().__init__(plagiarism_compare)

    def __draw_header(self):
        headers = self.headers

        header = ['Results']

        for element in headers:
            header.append(element)

        return ";".join(header) + "\n"

    def __draw_row(self, row_id):
        row_data = [self.plagiarism_compare.result[row_id][column]
                    for column in range(0, len(self.plagiarism_compare.result))]

        row = []

        for element in row_data:
            if element is None:
                row.append("None")
            else:
                row.append(str(element))

        return f'{self.headers[row_id]};' + ";".join(row) + "\n"

    def format(self):
        table = self.__draw_header()

        for row in range(0, len(self.plagiarism_compare.result)):
            table += self.__draw_row(row)

        return table
    
    def format_suspicious(self):
        # todo
        return ""
