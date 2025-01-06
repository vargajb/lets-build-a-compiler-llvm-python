## Part I: Introduction

[Part 1 of Jack W. Crenshaw's "Let's Build a Compiler!" series](https://xmonader.github.io/letsbuildacompiler-pretty/tutor01_introduction.html) sets the stage for a hands-on journey into compiler construction. The tutorial focuses on practical techniques to make the subject accessible, even to those without a computer science background.

Key points include:

* Emphasizing practical approaches, such as top-down recursive descent parsing.
* Avoiding intermediate representations like P-code, opting instead for direct assembler language output.
* Writing clear, modular code to facilitate understanding and optimization.
* Encouraging readers to follow along using Turbo Pascal, replicating and extending the examples.

The chapter concludes with a minimal "cradle" program that provides essential functionalities, such as input/output handling, error reporting, and character recognition, forming the foundation for subsequent lessons.

### Modernized version
The primary goal of this compiler is to generate executable code. Input and output files can be specified using command-line arguments. This flexibility allows the compiler to process various input sources and generate corresponding outputs.

#### Files
The implementation has been modularized into multiple source files for improved organization and maintainability:

*   **`cradle.py`:** The main program that coordinates the execution of the compiler.
*   **`code_processor.py`:** Contains a class for parsing input data and generating formatted code output. Parsing and code generation remain integrated in this version, following the approach of the original series.
*   **`scanner.py`:** Handles processing of the source code by reading it character by character.
    *   **Key updates:**
        *   Renamed `GetChar` to `next_char` for clarity.
        *   Replaced the global variable `Look` with the `peek_char` method for improved encapsulation.
#### Usage
The `cradle.py` script can be executed using the following syntax:

`cradle.py [-h] [input] [--M68k OUTPUT_M68K] [--LLVM OUTPUT_LLVM]`

**Positional Arguments**
*   `input`: Specifies the input source (default: user input).

**Options**
*   `-h, --help`: Show this help message and exit.
*   `--M68k OUTPUT_M68K`: Directs the M68000 code output to a file or `stdout`.
*   `--LLVM OUTPUT_LLVM`: Directs the LLVM IR code output to a file or `stdout`.
---
<sub>Source: Adapted from Jack Crenshaw's "<a href="https://xmonader.github.io/letsbuildacompiler-pretty/tutor01_introduction.html" target="_blank">Let's Build a Compiler</a>" series.</sub>
