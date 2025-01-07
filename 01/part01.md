## Part I: Introduction

[Part 1 of Jack W. Crenshaw's "Let's Build a Compiler!" series](https://xmonader.github.io/letsbuildacompiler-pretty/tutor01_introduction.html) sets the stage for a hands-on journey into compiler construction. The tutorial emphasizes a "learn-by-doing" approach, avoiding theoretical complexity and focusing on practical techniques that make compiler construction accessible to readers without a computer science background.

Key points include:

* Emphasizing practical approaches, such as top-down recursive descent parsing.
* Avoiding intermediate representations like P-code, opting instead for direct assembler language output.
* Writing clear, modular code to facilitate understanding and optimization.
* Encouraging readers to follow along using Turbo Pascal, replicating and extending the examples.

The chapter concludes with a minimal "cradle" program that provides essential functionalities, such as input/output handling, error reporting, and character recognition, forming the foundation for subsequent lessons.

---

### Modernized version
This modernized version retains Crenshaw’s hands-on philosophy while adapting the techniques and tools to align with contemporary software engineering practices. The primary goal is to generate executable code while offering flexibility in specifying input and output files via command-line arguments.

#### Key Updates
* **Code Modularization:** The implementation has been divided into multiple source files for better maintainability and scalability.
* **Improved Encapsulation:** The Look global variable has been replaced with the `peek_char` method, and the `GetChar` function has been renamed to `next_char` for clarity.
* **Enhanced Usability:** Command-line arguments allow the compiler to process diverse input sources and outputs.

#### Files
*   **`cradle.py`:** The main program that coordinates the execution of the compiler.
*   **`code_processor.py`:** Contains a class for parsing input data and generating formatted code output. Parsing and code generation remain integrated in this version, following the approach of the original series.
*   **`scanner.py`:** Handles processing of the source code by reading it character by character.

#### Usage
The `cradle.py` script can be executed using the following syntax:

`cradle.py [-h] [input] [--M68k OUTPUT_M68K] [--LLVM OUTPUT_LLVM]`

**Positional Arguments**
*   `input`: Specifies the input source (default: user input).

**Options**
*   `-h, --help`: Show this help message and exit.
*   `--M68k OUTPUT_M68K`: Directs the M68000 code output to a file or `stdout`.
*   `--LLVM OUTPUT_LLVM`: Directs the LLVM IR code output to a file or `stdout`.
