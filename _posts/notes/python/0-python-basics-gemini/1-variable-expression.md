Detailed notes on **Python Variables, Expressions, and Statements** should cover the fundamental building blocks of any Python program, focusing on definition, syntax, and how they relate to code execution.

## 1. Variables (Data Containers) 📦
***
* **Definition:** A variable is a named storage location that holds a value. It's an **identifier** used to reference data in the computer's memory.
* **Assignment:**
    * Using the single equal sign (`=`) operator to assign a value to a variable (e.g., `age = 30`).
    * Variables are created the moment you first assign a value to them.
* **Dynamic Typing (Crucial):**
    * Python is **dynamically typed**, meaning you do not declare the variable's data type; the type is determined at runtime based on the value assigned.
    * Variables can be **reassigned** to hold a value of a completely different type (e.g., `x = 10`, then `x = "hello"`).
* **Variable Naming Rules (Identifiers):**
    * Must begin with a letter (a-z, A-Z) or an underscore (`_`).
    * Cannot start with a number.
    * Can only contain alphanumeric characters and underscores (A-z, 0-9, and `_`).
    * Are **case-sensitive** (`Age` is different from `age`).
* **Conventions (PEP 8):** Use **lowercase with underscores** (snake_case) for variable names (e.g., `user_name`).
* **Garbage Collection:** Briefly mention that Python automatically reclaims memory when an object is no longer referenced by any variable.
* **Variable Identity:** Use the built-in `id()` function to see the unique memory address of the object a variable refers to.

## 2. Expressions (Value Producers) 💡
***
* **Definition:** An expression is a combination of **values, variables, operators, and function calls** that the Python interpreter evaluates to produce a single **result (value)**.
* **Key Characteristic:** Every expression **returns a value**.
* **Types of Expressions:**
    * **Mathematical:** `5 + 3` (evaluates to `8`).
    * **Logical:** `x > 10 and y < 5` (evaluates to `True` or `False`).
    * **Functional:** `len("Python")` (evaluates to `6`).
    * **Primary:** A single variable or literal value is also a simple expression (e.g., `42`, `my_variable`).
    * **Conditional (Ternary Operator):** `a if condition else b`.

## 3. Statements (Execution Instructions) 🎬
***
* **Definition:** A statement is a programming instruction that the Python interpreter can **execute**. A statement performs an action but **does not necessarily return a value**.
* **Key Characteristic:** A statement is a unit of execution.
* **Simple Statements (Single Line):**
    * **Assignment Statement:** `x = 5 + y` (Uses an expression on the right side).
    * **`print()` Statement:** `print("Hello")`.
    * **`import` Statement:** `import math`.
    * **`pass` Statement:** Does nothing, often used as a placeholder.
* **Compound Statements (Multiple Lines):**
    * Statements that contain groups of other statements (called **blocks** or **suites**).
    * Require a header line ending with a colon (`:`) and a body defined by **indentation** (e.g., 4 spaces).
    * Examples: `if/elif/else`, `for` loops, `while` loops, `def` (function definition), `class` (class definition), `try/except`.

## 4. Relationship and Execution Flow ➡️
***
* **Relationship:** Every **Expression** can be part of a **Statement**, but not every Statement is an Expression (e.g., `if` statements don't return values).
* **Expression Statements:** A statement that consists solely of an expression (e.g., `x * 2`—the interpreter computes the result but throws it away unless the result is assigned or printed).
* **Execution Order:** The interpreter executes statements sequentially unless directed otherwise by control flow statements (e.g., `if`, `for`).
* **Side Effects:** Statements often result in **side effects** (changes outside the statement itself), such as modifying a variable's value, printing output to the console, or writing to a file.