"""Parsing input data and generating formatted code output."""
import sys
from llvm import Llvm
from scanner import Scanner
from sympy import sympify

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
        self.__file_m68k = None
        self.__file_llvm = None
        self.__llvm = Llvm()

    def set_m68k_code_output_file(self, file):
        """Set output file for M68k code."""
        self.__file_m68k = file

    def set_llvm_code_output_file(self, file):
        """Set output file for LLVM IR code."""
        if file:
            self.__llvm = Llvm(enabled=True)
        self.__file_llvm = file

    def __close(self, file):
        if file is not None and file is not sys.stdout:
            file.close()

    def close(self):
        """Close output files."""
        self.__close(self.__file_m68k)
        self.__close(self.__file_llvm)

    def __emit(self, file, s, comment='', indent=1):
        """Output a string with a tab and aligned trailing comments."""
        tab_size = 4
        base_length = len("\t") + len(s) + tab_size
        padding = max(35 - base_length, 1)
        aligned_comment = f"{' ' * padding} ; {comment}" if comment else ""
        print(f"{' ' * indent * 4}{s}{aligned_comment}", end='', file=file)

    def __emit_ln(self, file, s, comment='', indent=1):
        """Output a string with a tab and a newline."""
        self.__emit(file, s, comment, indent)
        print(file=file)

    def emit_ln_m68k(self, s, comment='', indent=1):
        """Output a string targeting Motorola 68000 code with newline."""
        if self.__file_m68k:
            self.__emit_ln(self.__file_m68k, s, comment)

    def emit_ln_llvm(self, s, comment='', indent=1):
        """Output a string targeting LLVM IR code with newline."""
        if self.__file_llvm:
            self.__emit_ln(self.__file_llvm, s, comment, indent)

    def factor(self):
        """Parse and Translate a Math Factor."""
        if self.__scanner.peek_char() == '(':
            self.__scanner.match('(')
            self.expression()
            self.__scanner.match(')')
        else:
            num = self.__scanner.get_num()
            self.emit_ln_m68k(f'MOVE #{num}, D0', f'D0 = {num}')
            ssa = self.__llvm.new_ssa_variable()
            self.emit_ln_llvm(f'{ssa} = add i32 {num}, 0', f'{ssa} = {num}')

    def multiply(self):
        """Recognize and Translate a Multiply."""
        self.__scanner.match('*')
        self.factor()
        self.emit_ln_m68k('MULS (SP)+,D0', 'D0 *= (SP); increment SP (pop)')
        (last_ssa, new_ssa, stack_ssa) = self.__llvm.get_last_new_and_pop_ssa()
        self.emit_ln_llvm(f'{new_ssa} = mul i32 {stack_ssa}, {last_ssa}')

    def divide(self):
        """Recognize and Translate a Divide."""
        self.__scanner.match('/')
        self.factor()
        self.emit_ln_m68k('MOVE (SP)+,D1', 'D1 = (SP); increment SP (pop)')
        self.emit_ln_m68k('DIVS D1,D0', 'D0 /= D1 (signed division)')
        (op2, ssa, op1) = self.__llvm.get_last_new_and_pop_ssa()
        self.emit_ln_llvm(f'{ssa} = call i32 @floor_div(i32 {op1}, i32 {op2})')

    def term(self):
        """Parse and Translate a Math Term."""
        self.factor()
        while self.__scanner.peek_char() in ('*', '/'):
            self.emit_ln_m68k('MOVE D0,-(SP)', 'decrement SP; (SP)=D0 (push)')
            if self.__file_llvm:
                ssa_stack = self.__llvm.push_new_llvm_variable_to_stack()
                ssa = self.__llvm.last_ssa_variable()
                self.emit_ln_llvm(f'{ssa_stack} = add i32 {ssa}, 0',
                                  f'{ssa_stack} = {ssa}')
            match self.__scanner.peek_char():
                case '*': self.multiply()
                case '/': self.divide()
                case _: self.__scanner.expected('Mulop')

    def add(self):
        """Recognize and Translate an Add."""
        self.__scanner.match('+')
        self.term()
        self.emit_ln_m68k('ADD (SP)+,D0', 'D0 += (SP); increment SP (pop)')
        (last_ssa, new_ssa, stack_ssa) = self.__llvm.get_last_new_and_pop_ssa()
        self.emit_ln_llvm(f'{new_ssa} = add i32 {stack_ssa}, {last_ssa}')

    def subtract(self):
        """Recognize and Translate a Subtract."""
        self.__scanner.match('-')
        self.term()
        self.emit_ln_m68k('SUB (SP)+,D0', 'D0 -= (SP); increment SP (pop)')
        self.emit_ln_m68k('NEG D0', 'D0 = -D0 (negate)')
        (last_ssa, new_ssa, stack_ssa) = self.__llvm.get_last_new_and_pop_ssa()
        self.emit_ln_llvm(f'{new_ssa} = sub i32 {stack_ssa}, {last_ssa}')

    def expression(self):
        """Parse and Translate an Expression."""
        if self.is_addop(self.__scanner.peek_char()):
            self.emit_ln_m68k('CLR D0', 'Clear D0 (set to 0)')
            ssa = self.__llvm.new_ssa_variable()
            self.emit_ln_llvm(f'{ssa} = add i32 0, 0')
        else:
            self.term()
        while self.is_addop(self.__scanner.peek_char()):
            self.emit_ln_m68k('MOVE D0,-(SP)', 'push D0 onto stack')
            ssa = self.__llvm.last_ssa_variable()
            stack_ssa = self.__llvm.push_new_llvm_variable_to_stack()
            self.emit_ln_llvm(f'{stack_ssa} = add i32 {ssa}, 0')
            match self.__scanner.peek_char():
                case '+': self.add()
                case '-': self.subtract()
                case _: self.__scanner.expected("Addop")

    def is_addop(self, c):
        """Recognize an Addop."""
        return c in ('+', '-')

    def test_expression(self, exprs):
        """Generate compilable LLVM code for a list of expressions."""
        self.emit_ln_llvm(self.__llvm.LLVM_MAIN_HEADER, indent=0)
        self.emit_ln_llvm(self.__llvm.get_printf_statement(
            'counter;expected;current\n'))
        count = 0
        for expr in exprs:
            count += 1
            self.__scanner = Scanner(expr)
            self.expression()
            expected = f'i32 {sympify(expr.replace("/", "//"))}'
            current = f'i32 {self.__llvm.last_ssa_variable()}'
            self.emit_ln_llvm(self.__llvm.get_printf_statement(
                '%d;%d;%d\n', f'i32 {count}', expected, current))
        self.emit_ln_llvm(self.__llvm.LLVM_MAIN_RETURN, indent=0)
        self.emit_ln_llvm(self.__llvm.LLVM_USED_FUNCTIONS, indent=0)
        self.emit_ln_llvm(self.__llvm.llvm_declare_strings(), indent=0)
