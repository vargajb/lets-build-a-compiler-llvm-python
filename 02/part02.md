## Part II: Expression Parsing

[Part 2 of Jack W. Crenshaw's "Let's Build a Compiler!" series](https://xmonader.github.io/letsbuildacompiler-pretty/tutor02_expressionparsing.html) focuses on parsing and translating mathematical expressions into assembler-language statements. Through a step-by-step approach, it ensures even beginners can grasp the concepts while laying a foundation for advanced features.

Key topics include:

1. **Single-digit Expressions:** Parsing single-digit expressions to generate assembler code and recognizing errors for invalid inputs.

2. **Binary Expressions:** Extending the parser to handle addition and subtraction with expressions like `1+2` or `4-3`, while introducing the concept of preserving intermediate results using registers.

3. **General Expressions:** Implementing support for expressions with multiple terms (e.g., `1+2-3`) through iterative parsing.

4. **Using the Stack:** Addressing the limitations of registers by introducing stack usage to handle complex expressions like `1+(2-(3+(4-5)))`.

5. **Multiplication and Division:** Adding support for multiplication and division while respecting operator precedence.

6. **Parentheses:** Enabling support for expressions with parentheses, allowing precise control over operator precedence and complex nesting.

7. **Unary Minus:** Handling expressions with leading `+` or `-` signs (e.g., `-1`, `-(3-2))`.

8. **Optimization:** Discussing basic optimization techniques, such as peephole optimization and using CPU registers for improved efficiency, while emphasizing the focus on functionality over tight code in this tutorial.

This chapter concludes with a functional parser capable of handling basic expressions, preparing readers for more advanced topics in subsequent lessons.

---
### Modernized Version
This chapter expands the modernized compiler to parse and handle more complex mathematical expressions while leveraging the modular structure introduced earlier. Updates in this part focus on efficient parsing techniques and enhancing code generation for more advanced arithmetic operations.


### Files
This section retains the modular structure introduced in Part I, incorporating updates to `code_processor.py` for advanced expression parsing. Examples are provided in `test_1_expression.txt` and `test_200_expression.txt`. Additionally, a script, `build_and_run.sh`, has been added for compiling and executing LLVM IR code.

---

### Steps for Compilation and Execution
This chapter uses the same workflow introduced in Part I. Below are the steps, with updates specific to the new functionality in this part:

**Step 1: Check the Prerequisites:**

Ensure the required tools (`opt`, `llc`, `clang`) are installed before proceeding.

**Step 2: Generate LLVM IR and Assembly Code**
```bash
python cradle.py test_1_expression.txt --M68k test_1_expression.m68k.asm --LLVM test_1_expression.ll
```
**Step 3: Compile and Execute LLVM IR Code**
Refer to the script `build_and_run.sh` for automation:
```bash
./build_and_run.sh test_1_expression
./build_and_run.sh test_200_expression
```
**Step 4: Verify the Output**

Test cases in `test_1_expression.txt` and `test_200_expression.txt` demonstrate the extended functionality.

**Example Input:**
```csv
3+5*7
```
**Example Output:**
```csv
counter;expected;current
1;38;38
```
1. **Counter:** Test case number.
2. **Expected:** Result computed by Python.
3. **Current:** Result from LLVM IR-generated code.



---

### Notes for LLVM IR version
#### Static Single Assignment (SSA) variables

LLVM IR uses [SSA](https://en.wikipedia.org/wiki/Static_single-assignment_form), where each variable is assigned exactly once. For example:
```asm
%ssa_0 = add i32 3, 0  ; Equivalent to initializing %ssa_0 to 3
```
#### The expression `3+5*7` in different targets

This example illustrates how LLVM IR abstracts low-level details like register management, simplifying the process of generating code for multiple architectures.

<table>
  <tr>
    <th>Motorola 68000 Assembly</th>
    <th>LLVM IR</th>
  </tr>
  <tr>
    <td>
      <pre><code class="asm">
MOVE #3, D0      ; D0 = 3
MOVE D0,-(SP)    ; push D0 onto stack
MOVE #5, D0      ; D0 = 5
MOVE D0,-(SP)    ; decrement SP; (SP)=D0 (push)
MOVE #7, D0      ; D0 = 7
MULS (SP)+,D0    ; D0 *= (SP); increment SP (pop)
ADD (SP)+,D0     ; D0 += (SP); increment SP (pop)
      </code></pre>
    </td>
    <td>
      <pre><code class="asm">
%ssa_0 = add i32 3, 0          ; %ssa_0 = 3
%stack_0 = add i32 %ssa_0, 0
%ssa_1 = add i32 5, 0          ; %ssa_1 = 5
%stack_1 = add i32 %ssa_1, 0   ; %stack_1 = %ssa_1
%ssa_2 = add i32 7, 0          ; %ssa_2 = 7
%ssa_3 = mul i32 %stack_1, %ssa_2
%ssa_4 = add i32 %stack_0, %ssa_3
      </code></pre>
    </td>
</table>

Since we emit LLVM IR code, we don't have to worry too much about optimization. Because these simple expressions can be and will be evaluated at compile time, when compiling with optimization level `-O1`, the expression is converted into a single statement for the target CPU: `movl $38, %ecx`.

#### Truncating and Floor Division

**Explanation:**
- **Truncating Division** Used in languages like Java and C, rounding towards zero. Example:
```java
System.out.println(7 / 3);   // Output: 2 (truncating division)
System.out.println(-7 / 3);  // Output: -2 (truncating division)
```
- **Floor Division** Python rounds towards negative infinity. Example:
```python
print(7 / 3)   # Output: 2.3333333333333335 (float)
print(7 // 3)  # Output: 2 (integer floor division)
print(-7 // 3) # Output: -3 (integer floor division)
```
The `floor_div` function ensures Python-like behavior for division in LLVM IR.

Java's `Math.floorDiv()` logic:
```java
public static int floorDiv(int x, int y) {
    int r = x / y;
    // if the signs are different and modulo not zero, round down
    if ((x ^ y) < 0 && (r * y != x)) {
        r--;
    }
    return r;
}
```
Function for floor division in LLVM IR:
```asm
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
```
---
### Known Issues
Unary operators (`-`, `+`) are partially implemented. In Part VI, we will address their handling to ensure seamless parsing and accurate code generation for complex expressions.

---

### Summary

This chapter expands on the foundation by teaching readers how to parse and translate mathematical expressions into assembler-language statements. With step-by-step guidance, it covers operator precedence, multi-term expressions, and parentheses, culminating in a functional parser capable of handling basic arithmetic operations. These capabilities set the stage for future enhancements like variables and function calls.
