class Strings:
    def getString(self):
        self.str=input("Enter string :")
    def printString(self):
        print(self.str.upper())
s=Strings()
Strings.getString(s)
s.printString()