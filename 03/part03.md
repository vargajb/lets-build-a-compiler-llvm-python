## Part III: More Expressions

[Part 3 of Jack W. Crenshaw's "Let's Build a Compiler!" series](https://xmonader.github.io/letsbuildacompiler-pretty/tutor03_moreexpressions.html) removes previous limitations and significantly enhances the parser's functionality. Building on the expression parsing capabilities introduced in Part II, this chapter enables the parser to handle variables, function calls, assignment statements, multi-character tokens, and embedded white spaces, making it closer to a practical language compiler.

Key advancements include:

**1. Variables:**
* Extending the parser to handle variables as factors in expressions.
* Adding support for variable referencing and position-independent code generation.

**2. Function Calls:**
* Introducing simple function calls (e.g., `x()`), using branching statements (e.g., `BSR`).
* Handling ambiguity between variables and functions by utilizing lookahead.

**3. Assignment Statements:**
* Implementing the parsing and translation of assignment statements (e.g., `a = b + c`).
* Generating appropriate assembly code for assignment.

**4. Multi-Character Tokens:**
* Transitioning from single-character tokens to multi-character ones, supporting longer variable names and numbers.
* Adjusting the parser’s lexical recognition for identifiers and numbers.

**5. Embedded White Spaces:**
* Modifying the parser to skip and ignore white spaces for more flexible input handling.

**6. Error Handling:**
* Discussing robust techniques for managing malformed expressions.
* Ensuring the parser correctly flags errors while maintaining simplicity in design.

**7. Code Optimization:**
* Streamlining parsing operations by using structured BNF notation.
* Minimizing complexity in assembly code generation.

The chapter concludes by emphasizing the adaptability of recursive descent parsing for complex language features. It prepares readers for future topics, such as interpreters, by showcasing how changes in functionality affect parser structure.

---

### Files

This chapter updates the following files to handle new features:
* **`code_processor.py`:** Updated to support variable assignments, function calls, and multi-character tokens.
* **`scanner.py`:** Enhanced to recognize multi-character tokens, handle white spaces, and differentiate between variables and numbers.
* **`test_expressions.txt`:** Example input file for testing variable handling, assignments, and complex expressions.
* **`test_expressions.ll`, `test_expressions.m68k.asm`:** Generated LLVM IR and Motorola 68000 assembly code outputs for `test_expressions.txt`.

---

### Steps for Compilation and Execution
This chapter follows the compilation workflow introduced in earlier parts. Below are the steps with updates specific to this part:

**Step 1: Generate LLVM IR and Motorolla 68000 Code**
```bash
python cradle.py test_expressions.txt --M68k test_expressions.m68k.asm --LLVM test_expressions.ll
```
**Step 2: Compile and Execute LLVM IR Code**

Use the provided script to automate compilation and execution:
```bash
./build_and_run.sh test_expressions
```
**Step 3: Verify the Output**

Below is an example demonstrating how the parser handles variables, expressions, and assignments while generating correct outputs for both LLVM IR and assembly code:

<table>
  <tr>
    <th>Input: test_expressions.txt</th>
    <th>Output</th>
  </tr>
  <tr>
    <td>
      <pre><code class="c">
a1 = 3
a2 = 7 + a1 * 5
bb = a2 / a1
bb2 = a2 / (0 - a1)
bb3 = bb - bb2
      </code></pre>
    </td>
    <td>
      <pre><code class="c">
A1 = 3
A2 = 22
BB = 7
BB2 = -8
BB3 = 15
      </code></pre>
    </td>
</table>

---

### Summary

Building on the expression parsing introduced in Part II, this chapter removes earlier restrictions by adding support for variables, function calls, and assignments. The parser transitions to handling multi-character tokens and embedded white spaces, improving its usability and aligning it with real-world programming scenarios. These advancements prepare the parser for even more complex language features in later chapters.
