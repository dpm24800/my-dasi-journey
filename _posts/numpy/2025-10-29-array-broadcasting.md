## Broadcasting Arrays
- Concept and rules of broadcasting
- Examples of compatible and incompatible shapes
- Broadcasting in arithmetic and aggregation
- A set of rules that allows NumPy to work with arrays of different shapes when performing arithmetic operations.
- Understanding the rules for how a smaller array is "stretched" to match the shape of a larger array.
-   **The Rule:** Arrays can be operated on if their dimensions are compatible.
    -   **Rules:** 1) Trailing dimensions equal, or 2) One of them is 1.
    -   Examples: Adding a 1D array to a 2D array, scalar with an array.
    -   Using `np.newaxis`/`None` to reshape arrays for broadcasting.