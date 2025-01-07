## Part IV: Interpreters

[Part 4 of Jack W. Crenshaw's "Let's Build a Compiler!" series](https://xmonader.github.io/letsbuildacompiler-pretty/tutor04_interpreters.html#part-iv-interpreters---24-july-1988) introduces the concept of interpreters and their differences from compilers. While compilers generate object code for execution later, interpreters evaluate expressions and execute actions immediately during parsing. This approach emphasizes immediate feedback, showcasing a more dynamic and interactive method of processing code.

Key advancements in this chapter include:

**1. Input and Output Operations:**
* Introducing the `?` operator for user input and the `!` operator for output.
* Demonstrating how these operators enable immediate interaction with the interpreter.

**2. Assignment Evaluation:**
* Parsing and executing assignments interactively.
* Using the interpreter to evaluate expressions and update variable values in real-time.

**3. Immediate Execution:**
* Highlighting the structural changes required to support real-time execution during parsing.
* Contrasting this approach with the deferred execution characteristic of compilers.

This chapter establishes the foundation for more complex features in interpreters, such as control statements, which will be introduced in the next part.

---

### Files
This part primarily utilizes the existing modular structure from previous chapters.

The key files include:
* **`cradle.py`:** Coordinates the interpreter's execution.
* **`code_processor.py`:** Updated to support interactive input/output and assignment evaluation.
* **`scanner.py`:** Handles character-by-character processing of the source code.
* **`test_assignments.txt`:** Input file to test assignment and evaluation functionality.

---

### Steps for Testing the Interpreter
To test the interpreter with assignments, use the following command:
```bash
python cradle.py test_assignments.txt
```
**Input and Output Example**

The following example demonstrates how the interpreter processes input, evaluates assignments, and provides immediate output:
<table>
  <tr>
    <th>Input: test_assignments.txt</th>
    <th>Output</th>
  </tr>
  <tr>
    <td>
      <pre><code class="c">
?a 2
b=a*(5/2)-3*5
c=b+1
!a
!b
!c
.
      </code></pre>
    </td>
    <td>
      <pre><code class="c">
2
-11
-10
      </code></pre>
    </td>
</table>

**Explanation:**
* `?a 2` assigns the value `2` to variable `a`.
* `b=a*(5/2)-3*5` computes the value of `b` using `a` and stores `-11`.
* `c=b+1` computes the value of `c` as `-10`.
* `!a`, `!b`, and `!c` output the current values of `a`, `b`, and `c`, respectively.

This example illustrates the immediate execution of assignments and expressions, showcasing the interactive nature of the interpreter.

---

### Summary

Part IV shifts the focus from compilation to interpretation, emphasizing immediate feedback and execution. By introducing input/output operations, the interpreter becomes interactive and practical for real-time evaluation.
