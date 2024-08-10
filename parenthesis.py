def isValid(s):
        s = list(s)
        for character in s:
            if character == "(":
                try:
                    s.remove("(")
                    s.remove(")")
                except:
                    return False
            if character == "{":
                try:
                    s.remove("{")
                    s.remove("}")
                except:
                    return False
            if character == "[":
                try:
                    s.remove("[")
                    s.remove("]")
                except:
                    return False
        return s == []

isValid("()[]{}")