import json

from yapy.compare.output.formatter import OutputFormatter


class JSONFormatter(OutputFormatter):

    def __init__(self, plagiarism_compare):
        super().__init__(plagiarism_compare)

    def __row_result(self, row_id):
        result = []

        length = len(self.plagiarism_compare.result)

        for i in range(0, length):
            id = self.headers[i]

            result.append({
                'id': id,
                'score': self.plagiarism_compare.result[row_id][i] or self.plagiarism_compare.result[i][row_id]
            })

        return result

    def format(self):
        result = []

        for i, id in enumerate(self.headers):
            result.append({
                'id': id,
                'results': self.__row_result(i)
            })

        return json.dumps(result, indent=4)
