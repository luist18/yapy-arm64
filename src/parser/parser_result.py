class ParserResult:
    def __init__(self, lark_result):
        self.lark_result = lark_result
        self.tokens = self.__tokens()
        self.tokens_table = self.__tokens_table()
        self.register_number = self.__register_number()

    def __tokens(self):
        tokens = []

        for token in self.lark_result.iter_subtrees():
            token_name = token.data
            if token_name != 'program' and token_name != 'ret' and token_name != 'header':
                tokens.append(token_name)

        return tokens

    def __tokens_table(self):
        tokens = {}

        for token in self.tokens:
            if token in tokens:
                tokens[token] += 1
            else:
                tokens[token] = 1

        return tokens

    def __register_number(self):
        number = 0

        # for tree in self.lark_result.iter_subtrees():
        #    print(tree)

        return number
