<h1 align="center">Skepti</h1>

<p align="center">A terminal-based local system to detect DeepFake images</p>

<div align="center">

[![Hackathon](https://img.shields.io/badge/hackathon-UIU_HackDay_2026-orange.svg)](https://hackday.pages.dev/hackday)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/Atia-Farha/Skepti.svg)](https://github.com/Atia-Farha/Skepti/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Atia-Farha/Skepti.svg)](https://github.com/Atia-Farha/Skepti/pulls)

</div>

---

A terminal-based DeepFake image detection system designed to run locally on a user’s machine without requiring an
internet connection. It enables users to analyze images and determine whether an image is real or AI-generated (
DeepFake), ensuring privacy-focused predictions.

## Table of Contents

- [Problem Statement](#problem-statement)
- [Idea / Solution](#idea--solution)
- [Dependencies / Limitations](#dependencies--limitations)
- [Future Scope](#future-scope)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Setup before 1st Run](#setup-before-1st-run)
    - [Setup before Every Run](#setup-before-every-run)
    - [Run the Application](#run-the-application)
        - [Windows](#windows)
        - [macOS / Linux](#macos--linux)
- [How to use](#how-to-use)
- [Built With](#built-with)
- [Authors](#authors)

## Problem Statement

It is useful to design and follow a specific format when writing a problem statement. While there are several options
for doing this, the following is a simple and straightforward template often used in Business Analysis to maintain
focus on defining the problem.

- IDEAL: This section is used to describe the desired or “to be” state of the process or product. At large, this section
  should illustrate what the expected environment would look like once the solution is implemented.
- REALITY: This section is used to describe the current or “as is” state of the process or product.
- CONSEQUENCES: This section is used to describe the impacts on the business if the problem is not fixed or improved
  upon.
  This includes costs associated with loss of money, time, productivity, competitive advantage, and so forth.

Following this format will result in a workable document that can be used to understand the problem and elicit
requirements that will lead to a winning solution.

## Idea / Solution

This section is used to describe potential solutions.

Once the ideal, reality, and consequences sections have been
completed, and understood, it becomes easier to provide a solution for solving the problem.

## Dependencies / Limitations

- What are the dependencies of your project?
- Describe each limitation in detailed but concise terms
- Explain why each limitation exists
- Provide the reasons why each limitation could not be overcome using the method(s) chosen to acquire.
- Assess the impact of each limitation in relation to the overall findings and conclusions of your project, and if
  appropriate, describe how these limitations could point to the need for further research.

## Future Scope

Write about what you could not develop during the course of the Hackathon; and about what your project can achieve
in the future.

## Key Features

- Terminal-based interface – Interactive, user-friendly, and visually appealing TUI
- Image file input support – Analyze local image files
- Fully local execution – No internet connection required
- AI-powered detection – Analyzes image patterns to detect DeepFakes
- Visual result representation – Horizontal bar graph visualization of results
- Cross-platform compatibility – Works on Windows, macOS, and Linux

## Getting Started

Follow these instructions to set up and run the application on your local machine.

### Prerequisites

- Python -> [Installation Guide](/docs/PYTHON-INSTALLATION.md)
- Git (to clone the repository)

### Setup before 1st Run

1. Clone the repository
    ```bash
    git clone https://github.com/Atia-Farha/Skepti.git
    ```
2. Open a terminal and navigate to the project directory
    ```bash
    cd path/to/folder/Skepti
    ```
3. Set up a virtual environment (optional but recommended)
    ```bash
    python -m venv .venv
    ```
4. Activate the virtual environment
    - On Windows
        ```bash
        .venv\Scripts\activate
        ```
    - On macOS / Linux
        ```bash
        source .venv/bin/activate
        ```
5. Install the required dependencies
    ```bash
    pip install textual transformers torch pillow
    ```

### Setup before Every Run

1. Navigate to the project directory
    ```bash
    cd path/to/folder/Skepti
    ```
2. Activate the virtual environment
    - On Windows
        ```bash
        .venv\Scripts\activate
        ```
    - On macOS / Linux
        ```bash
        source .venv/bin/activate
        ```

### Run the Application

#### Windows

```bash
python main.py
```

#### macOS / Linux

```bash
python3 main.py
```

## How to Use

- Enter the absolute path of the image file you want to detect.
- Press the "SCAN NOW" button to start the detection process.
- View the generated result with the horizontal bar graph visualization.

## Built With

- **Python** - Core Language
- **Textual** - TUI Framework
- **Transformers** - AI Model Integration
- **Torch** - Deep Learning Library
- **Pillow** - Image Processing Library

## Authors

- [**Atia Farha**](https://github.com/Atia-Farha) - Frontend Developer
- [**S.M Nazmus Sadat**](https://github.com/smsadat-dev) - Backend Developer
