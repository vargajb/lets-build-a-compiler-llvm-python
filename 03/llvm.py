"""
A helper class for generating LLVM Intermediate Representation (IR) code.

This class provides functionality for generating LLVM IR `printf` statement,
and managing SSA (Static Single Assignment) variables, which are extensively
used in LLVM IR and are a critical concept in compiler design, simplifying
program analysis and optimization. It allows for creating new SSA variables
with unique names, pushing and popping them from a stack for temporary storage,
and managing variable counters to ensure unique variable names are generated.

Further reading: https://en.wikipedia.org/wiki/Static_single-assignment_form

Methods
-------
- push_new_llvm_variable_to_stack: Creates a new SSA variable and pushes it
  onto a stack.
- pop_llvm_variable_from_stack: Pops an SSA variable from the stack.
- new_ssa_variable: Creates a new SSA variable with a specified prefix.
- last_ssa_variable: Returns the most recently created SSA variable with a
  given prefix.
- get_printf_statement: Generate an LLVM IR `printf` statement.
- llvm_declare_strings(self): Generate LLVM IR declarations for all string
  constants.
"""
class Llvm:
    """Helper class to generate LLVM IR code."""

    __disabled = True
    __ssa_variable_counters = dict()
    __ssa_variable_stack = list()

    def __init__(self, enabled=False):
        self.__disabled = not enabled

    def new_ssa_variable(self, prefix='ssa'):
        """Create a new SSA variable with the specified prefix."""
        if self.__disabled:
            return None
        counter = self.__ssa_variable_counters.get(prefix, -1) + 1
        self.__ssa_variable_counters[prefix] = counter
        return self.last_ssa_variable(prefix)

    def last_ssa_variable(self, prefix='ssa'):
        """Get the most recent SSA variable with the given prefix."""
        if self.__disabled:
            return None
        counter = self.__ssa_variable_counters.get(prefix)
        if counter is None:
            raise ValueError(f'prefix={prefix} is invalid.')
        return f'%{prefix}_{counter}'

    def push_new_llvm_variable_to_stack(self):
        """
        Create a new SSA variable and push it onto the stack.

        Returns
        -------
        str
            The newly created SSA variable (e.g., %stack_0).
        """
        if self.__disabled:
            return None
        ssa_variable = self.new_ssa_variable('stack')
        self.__ssa_variable_stack.append(ssa_variable)
        return ssa_variable

    def pop_llvm_variable_from_stack(self):
        """Pop an SSA variable from the stack."""
        if self.__disabled:
            return None
        return self.__ssa_variable_stack.pop()

    def get_last_new_and_pop_ssa(self):
        """Get last SSA variable, create a new one, and pop from the stack."""
        return (self.last_ssa_variable(),
                self.new_ssa_variable(),
                self.pop_llvm_variable_from_stack())

    __string_constants = dict()
    def get_printf_statement(self, s, *args):
        """Generate an LLVM IR `printf` statement."""
        if s not in self.__string_constants:
            self.__string_constants[s] = f'@str_{len(self.__string_constants)}'
        str = self.__string_constants[s]
        length = len(s) + 1
        result = 'call i32 (i8*, ...) @printf(i8* getelementptr ' \
            f'inbounds([{length} x i8], [{length} x i8]* {str}, i32 0, i32 0)'
        for arg in args:
            result += f', {arg}'
        result += ')'
        return result

    def escape_string(self, s):
        """Escape non-printable characters in a string."""
        result = []
        for c in s:
            if c.isprintable():
                result.append(c)
            else:
                result.append(f'\\{ord(c):02x}')
        return ''.join(result)

    def llvm_declare_strings(self):
        """Generate LLVM IR declarations for all string constants."""
        result = ''
        for (k, v) in self.__string_constants.items():
            result += f'{v} = private unnamed_addr constant ' \
                f'[{len(k) + 1} x i8] c"{self.escape_string(k)}\\00", ' \
                'align 1\n'
        return result

    LLVM_MAIN_HEADER = "define i32 @main(i32 %argc, i8** %argv) {"
    LLVM_MAIN_RETURN = """   ret i32 0
}"""

    LLVM_USED_FUNCTIONS = """
declare i32 @printf(i8*, ...)

; Function for integer division that truncates to zero. (default in many
; programming languages like Java, LLVM, C, etc.)
define i32 @truncating_div(i32 %op1, i32 %op2) alwaysinline {
entry:
  %result = sdiv i32 %op1, %op2
  ret i32 %result
}

; Function for integer division that rounds to negative infinity.
; Compatible with Python's // operator
; Implements Java's Math.floorDiv() logic:
;    public static int floorDiv(int x, int y) {
;        int r = x / y;
;        // if the signs are different and modulo not zero, round down
;        if ((x ^ y) < 0 && (r * y != x)) {
;            r--;
;        }
;        return r;
;    }
define i32 @floor_div(i32 %x, i32 %y) alwaysinline {
    %q = sdiv i32 %x, %y
    %q_mul_y = mul i32 %q, %y
    %remainder = sub i32 %x, %q_mul_y
    %xor_result = xor i32 %x, %y
    %sign_diff = icmp slt i32 %xor_result, 0
    %non_zero_remainder = icmp ne i32 %remainder, 0
    %round_down_condition = and i1 %sign_diff, %non_zero_remainder
    %q_minus_1 = sub i32 %q, 1
    %final_result = select i1 %round_down_condition, i32 %q_minus_1, i32 %q
    ret i32 %final_result
}
"""
