# Python and LLVM IR Implementation of Jack Crenshaw's "Let's Build a Compiler"
Learn compiler construction with this Python and LLVM IR implementation of Jack Crenshaw's classic step-by-step "[Let's Build a Compiler](https://compilers.iecc.com/crenshaw/)" series. This repository modernizes Crenshaw's original lightweight compiler, written in Pascal for educational purposes and targeting the [Motorola 68000 processor](https://en.wikipedia.org/wiki/Motorola_68000), by using [Python](https://www.python.org/) and generating [LLVM IR](https://llvm.org/docs/LangRef.html).


This project is based on Jack Crenshaw's "Let's Build a Compiler," a classic step-by-step guide to building a compiler, now modernized with Python and LLVM IR."

[LLVM IR](https://llvm.org/docs/LangRef.html) is a high-level assembly language that offers several advantages:
- **Flexibility and Optimization**: LLVM IR strikes a balance between portability and optimization, facilitating efficient code generation for different platforms.
- **Wide Platform Support**: LLVM backends can target a wide range of platforms including Windows, Linux, macOS, mobile systems, and embedded systems. It also supports various CPU architectures such as x86, ARM, and RISC-V.
- **Cross-Platform Compilation**: The platform-independent nature of LLVM IR enables easy cross-platform compilation, making this compiler highly flexible.

## Development Environment

This project was developed and tested on Ubuntu 24.04 LTS with recent versions of Python, Clang, LLVM, and related tools.

The following tools are required:
- `python`
- `clang`
- `llc`
- `opt`

Installation for Linux:

```bash
sudo apt update && sudo apt full-upgrade
sudo apt install python3 clang llvm lld llvm-dev
