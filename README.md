# Python and LLVM IR Implementation of Jack Crenshaw's "Let's Build a Compiler"

## About

Learn the fundamentals of compiler construction with this modernized implementation of Jack Crenshaw's classic step-by-step "[Let's Build a Compiler](https://compilers.iecc.com/crenshaw/)" series. Originally written in Pascal and targeting the [Motorola 68000 processor](https://en.wikipedia.org/wiki/Motorola_68000), this educational project has been updated to use [Python](https://www.python.org/) and generate [LLVM IR](https://llvm.org/docs/LangRef.html).

### Why LLVM IR?

[LLVM IR](https://llvm.org/docs/LangRef.html) is a versatile intermediate representation that offers several benefits:
- **Portability and Optimization**: Enables efficient and portable code generation across multiple architectures and platforms.
- **Platform Support**: Targets a wide range of systems, including Windows, Linux, macOS, mobile devices, and embedded platforms, supporting architectures like x86, ARM, and RISC-V.
- **Cross-Platform Capabilities**: Simplifies cross-platform compilation, making this compiler a flexible and modern educational tool.

### Development Environment

This project was developed and tested on Ubuntu 24.04 LTS with recent versions of Python, Clang, and LLVM. To follow along, ensure you have the following tools installed:

- `python3`
- `clang`
- `llc`
- `opt`

#### Installation (Linux)

```bash
sudo apt update && sudo apt full-upgrade
sudo apt install python3 clang llvm lld llvm-dev
