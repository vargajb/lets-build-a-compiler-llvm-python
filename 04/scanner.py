"""Processing source code by reading it character by character."""
import sys

class Scanner:
    """
    A scanner class for processing source code.

    The scanner reads the input data character by character, providing methods
    for matching and extracting tokens from the input stream.

    Parameters
    ----------
    input_data (str): The input data to be scanned.

    Raises
    ------
    IndexError: If an attempt is made to read beyond the end of the input data.
    """

    def __init__(self, input_data):
        self.__input_data = input_data
        self.__input_data_pos = -1
        self.next_char()
        self.skip_white()

    def peek_char(self):
        """Return the current character or None if at the end of input."""
        if self.__input_data_pos < len(self.__input_data):
            return self.__input_data[self.__input_data_pos]
        if self.__input_data_pos == len(self.__input_data):
            return None
        raise IndexError("Attempted to read beyond the end of input data.")

    def next_char(self):
        """Read New Character From Input Stream."""
        self.__input_data_pos += 1
        return self.peek_char()

    def error(self, s):
        """Report an Error."""
        print()
        print(f"Error: {s}. Position in input: {self.__input_data_pos}")

    def abort(self, message):
        """Report Error and Halt."""
        self.error(message)
        sys.exit(1)

    def expected(self, s, was=None):
        """Report What Was Expected."""
        message = f"{s} Expected"
        if was:
            message += f", but was: {was}"
        self.abort(message)

    def is_alpha(self, c):
        """Recognize an Alpha Character."""
        return isinstance(c, str) and c.isalpha()

    def is_peek_alpha(self):
        """Recognize an Alpha Character."""
        return self.is_alpha(self.peek_char())

    def is_digit(self, c):
        """Recognize a Decimal Digit."""
        return isinstance(c, str) and c.isdigit()

    def is_peek_digit(self):
        """Recognize a Decimal Digit."""
        return self.is_digit(self.peek_char())

    def is_alphanum(self, c):
        """Recognize an Alphanumeric."""
        return self.is_alpha(c) or self.is_digit(c)

    def is_peek_alphanum(self):
        """Recognize an Alphanumeric."""
        return self.is_alphanum(self.peek_char())

    def is_addop(self, c):
        """Recognize an Addop."""
        return isinstance(c, str) and c in ('+', '-')

    def is_peek_addop(self):
        """Recognize an Addop."""
        return self.is_addop(self.peek_char())

    def is_white(self, c):
        """Recognize White Space."""
        return isinstance(c, str) and c in (' ', '\t')

    def is_peek_white(self):
        """Recognize White Space."""
        return self.is_white(self.peek_char())

    def skip_white(self):
        """Skip Over Leading White Space."""
        while self.is_peek_white():
            self.next_char()

    def match(self, x):
        """Match a Specific Input Character."""
        if self.peek_char() != x:
            self.expected(f"'{x}'", self.peek_char())
        else:
            self.next_char()
            self.skip_white()

    def get_name(self):
        """Get an Identifier."""
        if not self.is_peek_alpha():
            self.expected("Name", self.peek_char())
        token = []
        while self.is_peek_alphanum():
            token.append(self.peek_char())
            self.next_char()
        self.skip_white()
        return ''.join(token).upper()

    def get_num(self):
        """Get a Number."""
        if not self.is_peek_digit():
            self.expected("Integer", self.peek_char())
        value = []
        while self.is_peek_digit():
            value.append(self.peek_char())
            self.next_char()
        self.skip_white()
        return int(''.join(value))

    def new_line(self):
        """Recognize and Skip Over a Newline."""
        if self.peek_char() == '\n':
            self.next_char()
            if self.peek_char() == '\r':
                self.next_char()
