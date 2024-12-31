"""Parsing input data and generating formatted code output."""

class CodeProcessor:
    """
    A class for parsing input data and generating formatted code output.

    This class integrates parsing and code generation, using an internal
    scanner for processing input and providing methods to emit code to an
    output stream.
    You can specify output files by calling either `set_m68k_code_output_file`,
    `set_llvm_code_output_file`, or both, depending on which output formats you
    need.

    Parameters
    ----------
        scanner (Scanner): A scanner instance used for parsing input data.
    """

    def __init__(self, scanner):
        self.__scanner = scanner
        self.__table = dict()

    def close(self):
        """Close output files."""
        self.__close(self.__file_m68k)
        self.__close(self.__file_llvm)

    def factor(self):
        """Parse and Translate a Math Factor."""
        if self.__scanner.peek_char() == '(':
            self.__scanner.match('(')
            value = self.expression()
            self.__scanner.match(')')
        elif self.__scanner.is_peek_alpha():
            value = self.__table.get(self.__scanner.get_name(), 0)
        else:
            value = self.__scanner.get_num()
        return value

    def multiply(self, value):
        """Recognize and Translate a Multiply."""
        self.__scanner.match('*')
        return value * self.factor()

    def divide(self, value):
        """Recognize and Translate a Divide."""
        self.__scanner.match('/')
        return value // self.factor()

    def term(self):
        """Parse and Translate a Math Term."""
        value = self.factor()
        while self.__scanner.peek_char() in ('*', '/'):
            match self.__scanner.peek_char():
                case '*':
                    value = self.multiply(value)
                case '/':
                    value = self.divide(value)
                case _: self.__scanner.expected('Mulop')
        return value

    def add(self, value):
        """Recognize and Translate an Add."""
        self.__scanner.match('+')
        return value + self.term()

    def subtract(self, value):
        """Recognize and Translate a Subtract."""
        self.__scanner.match('-')
        return value - self.term()

    def expression(self):
        """Parse and Translate an Expression."""
        if self.__scanner.is_peek_addop():
            value = 0
        else:
            value = self.term()
        while self.__scanner.is_peek_addop():
            match self.__scanner.peek_char():
                case '+': value = self.add(value)
                case '-': value = self.subtract(value)
                case _: self.__scanner.expected("Addop")
        return value

    def assignment(self):
        """Parse and Translate an Assignment Statement."""
        name = self.__scanner.get_name()
        self.__scanner.match('=')
        self.__table[name] = self.expression()

    def __input(self):
        """Input Routine."""
        self.__scanner.match('?')
        name = self.__scanner.get_name()
        value = self.__scanner.get_num()
        self.__table[name] = value

    def __output(self):
        """Output Routine."""
        self.__scanner.match('!')
        name = self.__scanner.get_name()
        print(self.__table.get(name, 0))

    def interpreter(self):
        """Test Assignment."""
        while self.__scanner.peek_char() != '.':
            match self.__scanner.peek_char():
                case '?': self.__input()
                case '!': self.__output()
                case _: self.assignment()
            self.__scanner.new_line()
