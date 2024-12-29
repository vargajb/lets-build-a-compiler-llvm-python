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

    def match(self, x):
        """Match a Specific Input Character."""
        if self.peek_char() == x:
            self.next_char()
        else:
            self.expected(f"'{x}'", self.peek_char())

    def is_alpha(self, c):
        """Recognize an Alpha Character."""
        return isinstance(c, str) and c.isalpha()

    def is_digit(self, c):
        """Recognize a Decimal Digit."""
        return isinstance(c, str) and c.isdigit()

    def get_name(self):
        """Get an Identifier."""
        if not self.is_alpha(self.peek_char()):
            self.expected("Name", self.peek_char())
        name = self.peek_char().upper()
        self.next_char()
        return name

    def get_num(self):
        """Get a Number."""
        if not self.is_digit(self.peek_char()):
            self.expected("Integer", self.peek_char())
        num = self.peek_char()
        self.next_char()
        return num
