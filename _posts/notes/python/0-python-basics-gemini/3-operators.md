Detailed notes on **Python Operators** should categorize them based on their function and cover their syntax, specific behavior, and precedence.

## 1. Introduction and Core Concepts 💡

* **Definition:** What an operator is (a symbol or keyword that performs an operation on one or more values, called operands).
* **Types of Operators:**
    * **Unary:** Operate on one operand (e.g., `-5`).
    * **Binary:** Operate on two operands (e.g., `5 + 3`).
    * **Ternary:** Operate on three operands (only the Conditional Expression in Python).
* **Operator Precedence:** The rules that determine the order in which operations are performed (e.g., multiplication before addition).
* **Operator Associativity:** The rule that defines the grouping of operators that have the same precedence (usually left-to-right).

***

## 2. Arithmetic Operators 🧮

These perform mathematical calculations.

| Operator | Name | Description | Example |
| :---: | :---: | :--- | :--- |
| `+` | **Addition** | Sums two operands. | `x + y` |
| `-` | **Subtraction** | Subtracts the right operand from the left. | `x - y` |
| `*` | **Multiplication** | Multiplies two operands. | `x * y` |
| `/` | **Division** | Returns a float result (true division). | `10 / 3` (3.333...) |
| `//` | **Floor Division** | Returns the integer part of the quotient (rounds down). | `10 // 3` (3) |
| `%` | **Modulus** | Returns the remainder of the division. | `10 % 3` (1) |
| `**` | **Exponentiation** | Raises the left operand to the power of the right. | `2 ** 3` (8) |
* **String Overloading:** Note on how `+` and `*` are overloaded for strings (concatenation and repetition, respectively).

***

## 3. Assignment Operators ⬅️

These are used to assign values to variables, often combined with an arithmetic operation.

| Operator | Example | Equivalent To |
| :---: | :---: | :--- |
| `=` | `x = 5` | Basic assignment. |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |
* **Chained Assignment:** Assigning the same value to multiple variables (e.g., `a = b = 10`).

***

## 4. Comparison (Relational) Operators ⚖️

These compare two operands and always return a **Boolean** value (`True` or `False`).

| Operator | Name | Example |
| :---: | :---: | :--- |
| `==` | **Equal to** | `x == y` |
| `!=` | **Not equal to** | `x != y` |
| `>` | **Greater than** | `x > y` |
| `<` | **Less than** | `x < y` |
| `>=` | **Greater than or equal to** | `x >= y` |
| `<=` | **Less than or equal to** | `x <= y` |
* **Chained Comparisons (Python Specific):** The ability to chain operators logically, like in math (e.g., `0 < x <= 10`).

***

## 5. Logical Operators 🧐

These combine conditional statements and return a Boolean value.

| Operator | Name | Description |
| :---: | :---: | :--- |
| `and` | **Logical AND** | Returns `True` if both operands are true. |
| `or` | **Logical OR** | Returns `True` if at least one operand is true. |
| `not` | **Logical NOT** | Reverses the logical state of the operand. |
* **Short-Circuit Evaluation:** Crucial concept explaining that:
    * With **`and`**, if the left operand is false, the right is **never evaluated**.
    * With **`or`**, if the left operand is true, the right is **never evaluated**.
* **Result Value:** The result of `and` and `or` is not necessarily `True` or `False`; it can be one of the operands involved, depending on which one determines the result (e.g., `5 and 'hello'` returns `'hello'`).

***

## 6. Identity Operators 🆔

These compare the **memory location** of two objects, not their values.

| Operator | Description | Example |
| :---: | :--- | :--- |
| `is` | Returns `True` if both variables are the **same object**. | `a is b` |
| `is not` | Returns `True` if both variables are **not the same object**. | `a is not b` |
* **Key Distinction:** **`is`** checks identity (`id(a) == id(b)`), while **`==`** checks value. This difference is critical for mutable types (lists, dictionaries).
* **Interning:** Brief note on how Python often interns small integers and specific strings, leading to surprising `is` results.

***

## 7. Membership Operators 👥

These test whether a sequence (string, list, tuple, set, dictionary) contains a specific element.

| Operator | Description | Example |
| :---: | :--- | :--- |
| `in` | Returns `True` if the value is found in the sequence. | `'a' in 'apple'` |
| `not in` | Returns `True` if the value is **not** found in the sequence. | `'z' not in 'apple'` |
* **Dictionary Use:** When used with dictionaries, these operators check for the presence of a **key** (not a value).

***

## 8. Bitwise Operators (Advanced) ⚙️

These operate directly on the individual bits of integer operands (often used in low-level programming or certain optimizations).

| Operator | Name | Description |
| :---: | :---: | :--- |
| `&` | **Bitwise AND** | Sets each bit to 1 if both bits are 1. |
| `\|` | **Bitwise OR** | Sets each bit to 1 if at least one bit is 1. |
| `^` | **Bitwise XOR** | Sets each bit to 1 if only one of the bits is 1. |
| `~` | **Bitwise NOT** | Inverts all the bits (bitwise negation). |
| `<<` | **Left Shift** | Shifts bits to the left, effectively multiplying by $2^n$. |
| `>>` | **Right Shift** | Shifts bits to the right, effectively dividing by $2^n$. |

***

## 9. Operator Precedence Table 📈

A comprehensive table listing all operators from highest precedence to lowest.

| Precedence Group | Operators | Description |
| :--- | :--- | :--- |
| **Highest** | `()` | Parentheses (grouping/function call) |
| | `**` | Exponentiation |
| | `+x, -x, ~x` | Unary positive, negative, bitwise NOT |
| | `*, /, //, %` | Multiplication, division, floor, modulus |
| | `+, -` | Addition, subtraction |
| | `<<, >>` | Bitwise shifts |
| | `&` | Bitwise AND |
| | `^` | Bitwise XOR |
| | `\|` | Bitwise OR |
| | `in, not in, is, is not, <, >, <=, >=, ==, !=` | Comparisons, Identity, Membership |
| **Lowest** | `not` | Logical NOT |
| | `and` | Logical AND |
| | `or` | Logical OR |
| | `if/else` | Conditional expression |
| | `=`, `+=`, etc. | Assignment operators |