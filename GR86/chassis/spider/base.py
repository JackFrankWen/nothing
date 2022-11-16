class spider:
    def transform(self, code):
        if code[0] == '6':
            return code + '.SH'
        elif code[0] == "8" or code[0] == "4":
            return code + '.BJ'
        else:
            return code + '.SZ'
