# Complementary Topside Control Unit (CTCU) Code Repository

Welcome to the repository for the Complementary Topside Control Unit (CTCU) of Vortex ROV! This README will guide you through the file structure of the CTCU software.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Repository Structure](#repository-structure)
  
## Introduction

The Complementary Topside Control Unit (CTCU) of the Vortex ROV. The CTCU provides all the tools that the copilot needs to perform Mission tasks, including pilot camera mirroring, data plotting, communication, float controls, and other mission-specific tools.

## Installation

To set up the CTCU software on your development environment, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Vortex-ROV/TCU-Code.git
   cd TCU-Code
   ```

2. **Create and Activate a Virtual Environment:**

   It's a good practice to use a virtual environment to manage dependencies. Run the following commands to create and activate one:

   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Packaged Dependencies:**
   ```bash
   pip install .
   ```

4. **Run the TCU Software:**
   ```bash
   python main.py
   ```

## Repository Structure

- **`/src`:** Core source code for communication, control, and data processing.
- **`/tests`:** Test cases to validate the software's functionality and performance.
- **`main.py`:** Main script used to launch the TCU.
- **`TCU.toml`:** Configuration file for packaging TCU code.
