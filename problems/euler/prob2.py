def main():
        """
        The Fibonacci Sequence has a pattern of even and odd numbers:
        o,o,e,o,o,e,o,o...
        """
        a, b = 1, 1
        s = 0
        i = 2

        try:
                while b < 4*10**6:
                        c = a + b
                        a = b
                        b = c
                        print(c,i)
                        if i == 2:
                                s += c
                                i = 0
                        else:
                                i += 1
                        
                return s
        except KeyboardInterrupt:
                print(n)
                print('yyy')
                return [s]
