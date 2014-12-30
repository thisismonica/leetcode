def isNumber( s):
        try:
            int(s)
            if s.strip()[0] != '+':
                return True
            elif not isdigit( s.strip()[1] ): return False
        except ValueError:
            try:
                float(s)
                return True
            except ValueError:
                return False
print isNumber("+53")
