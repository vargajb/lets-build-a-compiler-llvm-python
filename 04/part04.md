## Part IV: Interpreters

### Files
* **`cradle.py`:** The main program that coordinates the execution of the compiler.
* **`code_processor.py`:** Handles expression parsing.
* **`scanner.py`:** Processes the source code by reading it character by character.
* **`test_assignments.txt`:** Input file to test assignments.

### Test assignments
```bash
python cradle.py test_assignments.txt
```
**Input and Output Example**
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

---
<sub>Source: Adapted from Jack Crenshaw's "<a href="https://xmonader.github.io/letsbuildacompiler-pretty/tutor04_interpreters.html#part-iv-interpreters---24-july-1988" target="_blank">Let's Build a Compiler</a>" series.</sub>
