---
layout: post
title:  "Pandas – note plan"
author: Dipak Pulami Magar
date: 2025-11-05 10:12:45 +0545
categories: note-plans
status: draft
---

## 1. Introduction to Pandas
### What is Pandas 
  * Definition: A fast, powerful, and flexible open-source data analysis and manipulation library for Python.
  * Built on top of NumPy.
### Key features and benefits
  - History and development
### Key uses: and why it’s used/ primary use cases
  * Data cleaning, transformation, analysis, and visualization preparation.
  * data manipulation, analysis, cleaning.
* Comparison with NumPy
  * Relation to **NumPy** (Pandas is built on top of NumPy).
  * Comparison with other libraries (e.g., NumPy, Polars)

* Installation and Import 
  * `pip install pandas`:
  * `import pandas as pd`: 
  * Installation and setup (using pip, conda)
- Pandas data structures overview (`Series` vs/& `DataFrame`)
  * Data structures in Pandas: `Series` and `DataFrame`
- Key features and advantages
- Overview of Pandas ecosystem (relation to NumPy, Matplotlib, etc.)

---

## 2. The Fundamental/Core Data Structures
### (Pandas) Series:
  * One-dimensional labeled array.
  * Creation: from list, dictionary, NumPy array.
  * Anatomy: Index and Values.
  * Key attributes: `.index`, `.values`, `.dtype`, `.name`.
  +++  
  - Creating Series: from lists, dictionaries, NumPy arrays
  - Indexing and index objects
  - Series attributes (index, values, dtype, name, shape)
  - Vectorized operations
  - Boolean indexing with Series
  - Handling missing values in Series

### 2. Pandas Series
* Creating a Series
  * From lists, arrays, dictionaries, scalar values
* Indexes and Labels
* Accessing elements (`.loc[]`, `.iloc[]`, slicing)
* Operations on Series
  * Arithmetic, comparison, and broadcasting
* Useful Series methods
  * `head()`, `tail()`, `describe()`, `value_counts()`, `unique()`, `nunique()`, `map()`, `apply()`
* Handling missing values in Series (`isna()`, `fillna()`, `dropna()`)


### (Pandas) DataFrame:
  * Two-dimensional labeled data structure (like a spreadsheet or SQL table).
  * Creation: from dict of Series/lists, list of dicts, NumPy array, from a file (e.g., CSV, Excel).
  * Anatomy: Index, Columns, and Data.
  * Key attributes: `.index`, `.columns`, `.dtypes`, `.shape`, `.info()`, `.head()`, `.tail()`.
  +++  
- Creating DataFrames from:
  - Dictionaries of lists/Series
  - List of dictionaries
  - NumPy arrays
  - CSV, Excel files
  - External databases
- DataFrame anatomy (index, columns, data)
- Essential attributes:
  - `.index`, `.columns`, `.dtypes`
  - `.shape`, `.size`, `.ndim`
  - `.values`, `.axes`
- Essential methods:
  - `.info()`, `.describe()`
  - `.head()`, `.tail()`, `.sample()`

### 3. Pandas DataFrame
* Creating DataFrames
  * From dicts, lists of dicts, NumPy arrays, CSV/Excel files
* DataFrame structure: rows, columns, index, dtypes
* Accessing data
  * Selecting columns (`df['col']`), rows (`.loc[]`, `.iloc[]`), slices
* Adding, modifying, and deleting columns/rows
* Renaming columns or indexes (`rename()`)
* Copying vs referencing (`copy(deep=True)`)

---

## 3. Data Input and Output (I/O) Operations
### Reading data: from various sources/formats (common file types)
  * `pd.read_csv()`: # key parameters: sep, header, index_col, usecols, dtype; Parameters like sep, header, index_col, dtype
  * `pd.read_excel()`: # sheet_name, engine; from Excel; Sheet selection, multi-sheet handling
  * `pd.read_json()`: # orient, lines; from JSON; Orientation options
  * `pd.read_html()`: # web scraping; HTML tables
  * `pd.read_sql()`: # sql, con; Queries, connections
  * `pd.read_clipboard()`: from Clipboard; Clipboard
  * `pd.read_table()`: from Flat Files?? with `read_csv`
  * From URLs.
  * Parquet, HDF5, Feather, and other efficient formats

#### Important Parameters for reading:
  - `index_col`: 
  - `header`: 
  - `usecols`: 
  - `parse_dates`: 
  - `sep`: 
  - `dtype`:  
  - `nrows`: 

### Writing Data: to files
  * `df.to_csv()`:  # index=False, header, encoding; (important: `index=False`); Parameters like index, header, mode
  * `df.to_excel()`: # sheet_name, index; Multi-sheet writing with ExcelWriter
  * `df.to_sql()`: writing to a database; Handling if_exists, chunksize
  * `df.to_json()`: # orient; Orientation (split, records, etc.)
  * `df.to_parquet()`: # efficient storage; efficient binary format, highly recommended for large datasets.
* Parameters for performance and memory optimization
* Key **parameters** for writing:
  * (e.g., `index=False`, `header=False`, `sheet_name`).
* Handling large datasets: Chunking, iterators

---

## 4. Data Inspection and Summary (Statistics)
### Basic Inspection/Initial Data Inspection

* **Initial Review:**
    * Viewing data: `.head()`, `.tail()`.
    * Concise summary: `.info()` (data types, non-null values, memory usage).
    * `.describe()`: Descriptive statistics (count, mean, std, min, max, quartiles).
    * Column value counts: `.value_counts()`.
    * `.sample()`: 
* **Data Types:**
    * Checking types: `.dtypes`.
    * Converting types: `.astype()`.
    * Understanding common Pandas dtypes (`int64`, `float64`, `object`, `category`, etc.).


* Checking basic info: 
  * `df.info()`: comprehensive overview; Data types and non-null counts.
  * `df.describe()`: Summary statistics for numerical columns.
  * `df.shape`: Dimensions of the DataFrame.
  * `df.columns`: List of column names.
  * `df.index`:
  * `df.dtypes`: Data types of each column.
  * Shape, size, and info (
  * .shape: 
  * .memory_usage()

* Detecting duplicates:
  * `duplicated()`: 
  * `drop_duplicates()`: 

- `.describe()` - summary stats (include/exclude parameters)
- `.memory_usage()` - memory consumption

* Checking for missing data: 
  * `isnull()`:
  - `.isnull().sum()` - missing value counts; Count of missing values per column.
  * `notnull()`

### Statistical Methods/Descriptive statistics
- `describe()`: Summary statistics for numerical columns.?? 
- `sum()`: 
- Central tendency: `.mean()`, `.median()`, `.mode()`
- Dispersion: `.std()`, `.var()`, `.mad()`
- Extremes: `.min()`, `.max()`
- Quantiles: `.quantile()`, `.percentile()`
- Counts: 
  - `.count()`: 
  - `.value_counts()`: For categorical columns.
  - `.nunique()`:

---

## 5. Data Selection and Filtering/
## 5. Data Selection & Indexing and Subsetting
*This is a critical section. Understand the difference between `[]`, `.loc[]`, and `.iloc[]`.*


* Conditional selection (`df[df['col'] > value]`)
* `query()` method
* Multi-condition filtering with `&`, `|`, `~`
* Selecting subsets of rows and columns
* `isin()`, `between()`, `where()`, `mask()`

---
* **Basic Selection:**
    * Selecting columns (as Series and as a DataFrame subset).
    * Selecting rows using list slicing (`df[10:20]`).
* **Label-based Indexing:**
    * Using **`.loc[]`** (selection by labels/names for rows and columns).
    * Conditional/Boolean filtering (e.g., `df[df['Age'] > 25]`).
* **Position-based Indexing:**
    * Using **`.iloc[]`** (selection by integer position for rows and columns).
* **Advanced Indexing:**
    * Setting, resetting, and modifying the index: `.set_index()`, `.reset_index()`.
    * Working with **MultiIndex** (Hierarchical Indexing).
---


### Column Selection/Selecting Columns
- Single column: `df['col']` (Series) vs `df[['col']]` (DataFrame)
- Multiple columns: `df[['col1', 'col2']]`
- Column attributes: `df.columns`
- Renaming columns: `.rename(columns={})`

* Single column as Series: `df['column_name']`
* Single column as DataFrame: `df[['column_name']]`
* Multiple columns: `df[['col1', 'col2']]`

### Row Selection/Selecting Rows
#### By label/index: `.loc[]` (label-based)
  - Single row: `df.loc['label']`
  - Multiple rows: `df.loc[['label1', 'label2']]`
  - Slicing: `df.loc['start':'end']` (inclusive)
  - Boolean indexing: `df.loc[df['age'] > 30]`

 * Single row: `df.loc['index_label']`
 * Multiple rows: `df.loc[['label1', 'label2']]`
 * Slicing with labels: `df.loc['label1':'label3']` (inclusive!)

#### By integer position: `.iloc[]` (position-based)
  - Single row: `df.iloc[0]`
  - Multiple rows: `df.iloc[[0, 2, 4]]`
  - Slicing: `df.iloc[0:5]` (exclusive)
  - Single row: `df.iloc[0]`
  - Multiple rows: `df.iloc[[0, 2, 4]]`
  - Slicing with integers: `df.iloc[0:5]` (exclusive of the stop index)

* By boolean indexing (filtering): `df[df['age'] > 30]`
- **Boolean Indexing**
  - Single condition: `df[df['age'] > 30]`
  - Multiple conditions: `(df['age'] > 30) & (df['city'] == 'NYC')`
  - `.isin()` method
  - `.query()` method for complex filtering

### Combined Selection/Selecting Subsets (Rows and Columns): Subsetting
- `df.loc[row_labels, col_labels]`
- `df.iloc[row_positions, col_positions]`
- `df.at[]` and `df.iat[]` for scalar access

* Using `.loc[]`: `df.loc[rows_selection, columns_selection]`
  * Example: `df.loc[df['age'] > 25, ['name', 'city']]`
* Using `.iloc[]`: `df.iloc[row_indices, column_indices]`
  * Example: `df.iloc[0:5, [1, 3]]`

---

## 5. Data Cleaning & Preprocessing
* Handling missing data (`fillna()`, `dropna()`, `interpolate()`)
* Replacing values (`replace()`)
* Changing data types (`astype()`)
* Renaming columns or indexes (`rename()`)
* String operations (`str.upper()`, `str.contains()`, etc.)
* Handling outliers
* Dropping or filling NaNs conditionally

### Handling Missing Data
- Detecting/Identifying missing values:
  - `.isna()`: 
  - `.isnull()`: 
  - `.notna()`: 
  - `.notnull()`: 
- Counting: 
  - `.isnull().sum()`, 
  - `.isnull().mean()`
- Dropping missing values: 
  - `.dropna()` (axis, how, thresh, subset)
  - `.dropna()` (how='any'/'all', axis, thresh, subset)
  - `.dropna()` (rows/columns, parameters like `how='all'`, `subset`).
- Filling missing values: 
  - `.fillna()` (value, method='ffill'/'bfill', limit)
  - `.fillna()` (with a scalar, mean/median/mode, or forward fill `ffill` and backward fill `bfill`)
- Interpolation: 
  - `.interpolate()` (method, limit_direction)

### Handling Duplicates/duplicate data
- Detection/identifying duplicates: `.duplicated()` (subset, keep)
- Removal/Dropping duplicates: `.drop_duplicates()` (subset, keep='first'/'last'/False)
- Counting duplicates

### Data Type Conversion
- `.astype()` - basic type conversion; for simple conversions (e.g., `df['col'].astype('int32')`)
- `pd.to_numeric()` - with error handling; more robust, handles errors (`errors='coerce'`)
- `pd.to_datetime()` - date parsing; convert to datetime.
- `pd.to_timedelta()`: 
- `infer_objects()` - smart type inference

### String Operations
- String accessor: `.str`
- Common methods:
  - Case: `str.lower()`, `str.upper()`, `.title()`
  - Searching: `.contains()`, `.startswith()`, `.endswith()`
  - Manipulation: `.replace()`, `.strip()`, `.split()`, `.extract()`
  - Information: `.len()`, `.find()`
  - `.str.lower()`, `.str.upper()`, `.str.contains()`, `.str.replace()`, `.str.split()`, `.str.strip()`, `.str.len()`

### Column Operations: Renaming, Adding, and Dropping Columns  

- Adding columns: `df['new'] = values` or `.assign()`
- Dropping columns: `.drop(columns=[])`
- Renaming columns/index (`.rename()`): `.rename(columns={})`
- Reordering: column selection or `.reindex()`

* Rename: `df.rename(columns={'old':'new'})`
* Add: `df['new_col'] = ...` or `df.assign(new_col=...)`
* Drop: `df.drop(columns=['col1', 'col2'])` or `df.drop(['col1'], axis=1)`

#### (Renaming and Modifying)
  * Renaming columns/index: **`.rename()`**.
  * Mapping and replacing values: `.replace()`, `.map()`.

---

## 7. Data Transformation (and Manipulation)
* Applying functions (`apply()`, `applymap()`, `map()`)
* Lambda functions
* Vectorized operations
* Sorting (`sort_values()`, `sort_index()`)
* Reindexing (`reindex()`)
* Changing column order


### Sorting
- Sorting by index:
  - `.sort_index()` (ascending, inplace)
- Sorting by values:
  - `.sort_values()` (by, ascending, na_position)
  - `.sort_values(by='col1', ascending=[False])` (multiple columns)

### Applying Functions
- **`.map()`** - element-wise Series transformation
- **`.apply()`** - row/column-wise DataFrame operations
- **`.applymap()`** - element-wise on entire DataFrame
- **Vectorized operations** - preferred for performance
- **Lambda functions** with apply

* `map()` - Element-wise transformation on a Series.
* `apply()` - Row-wise or column-wise transformation on a DataFrame. More flexible, but slower.
* `applymap()` - Element-wise on a whole DataFrame (less common).
* **Vectorized operations are preferred for performance.**

* Applying Functions:
    * Element-wise operations: Using NumPy functions or lambda functions with **`.apply()`** on a Series.
    * Row-wise or Column-wise operations: Using **`.apply()`** with `axis=0` or `axis=1`.


### Binning & Discretization
- `pd.cut()` - equal-sized bins
- `pd.qcut()` - quantile-based bins
- Boolean indexing with multiple categories

2.  Filtering Data
  * Boolean indexing with multiple conditions (`&`, `|`, `~`).
  * Using `.isin([list])`.
  * Using `.str` methods for text filtering.
  * Using `.query()` method.
---

## 8. Data Aggregation & Grouping: Grouping and Aggregation
* `groupby()` basics
* Aggregation functions (`sum()`, `mean()`, `count()`, `agg()`)
* Grouping by multiple columns
* Iterating over groups
* Transformations (`transform()`)
* Pivot tables (`pivot_table()`)
* Cross-tabulation (`pd.crosstab()`)

### Basic/Simple Aggregation
- Single function: `.sum()`, `.mean()`, `.count()`
- Multiple functions: `.agg(['mean', 'std', 'count'])`
- Column-specific: `.agg({'col1': 'mean', 'col2': ['min', 'max']})`
- `.sum()`, `.mean()`, `.median()`, `.std()`, `.min()`, `.max()`, `.count()`, `.describe()`

### GroupBy Operations
- **Split-Apply-Combine pattern**
  - Single column grouping: `.groupby('col')`
  - Multiple columns: `.groupby(['col1', 'col2'])`
  - Grouping with functions: `.groupby(lambda x: x.year)`

1.  **The `groupby` Mechanism**
    * Concept: Split-Apply-Combine.
    * Syntax: `df.groupby('by_column')`
    * Aggregating: `.agg(['mean', 'std'])` or `.agg({'col1':'sum', 'col2':'mean'})`
    * Iterating over groups.
    * Grouping by multiple columns.

- **GroupBy methods**:
  - Aggregation: `.sum()`, `.mean()`, `.size()`
  - Transformation: `.transform()`
  - Filtration: `.filter()`
  - Iteration: `for name, group in df.groupby()`

* **Grouping and Aggregation:**
    * The **Split-Apply-Combine** strategy.
    * Using **`.groupby()`** and common aggregation functions (e.g., `.mean()`, `.sum()`, `.count()`, `.agg()`).



### Advanced Grouping: Pivot Tables & Cross-Tabulation
- `.agg()` with custom functions
- Named aggregation with tuples
- `.pivot_table()` - multi-dimensional analysis
- `.crosstab()` - frequency tables
- `pd.pivot_table()` - `index`, `columns`, `values`, `aggfunc`.
- `pd.crosstab()` - For computing a simple frequency table.

---
## Data Manipulation??
## 9. Combining (Merging, Joining, and Concatenating) DataFrames
## 9. Combining DataSets

### **Concatenation**
- `pd.concat()` - axis (0/1), join, ignore_index, keys
- Row-wise vs column-wise concatenation

* **Concatenation (`pd.concat()`)**
  * `axis=0` (row-wise, stacking), `axis=1` (column-wise, side-by-side).
  * `join='inner'/'outer'`.





### **Merging & Joining**
- **`pd.merge()`** - SQL-style joins
  - Join types: inner, left, right, outer, cross
  - Key parameters: on, left_on, right_on, how, suffixes
  - Indicator for merge diagnostics
- **`.join()`** - index-based joining
- **`.combine_first()`** - filling missing values

* **Joining and Merging:**
    * Combining DataFrames: **`pd.concat()`** (stacking/side-by-side).
    * Database-style joins: **`pd.merge()`** (Inner, Outer, Left, Right joins, parameters like `on`, `left_on`, `right_on`).
    * Combining on index: `.join()`.

* **Merging / Joining (`pd.merge` / `df.join`)**
  * SQL-style joins (inner, left, right, outer, cross).
  * Key parameters: `on`, `left_on`, `right_on`, `how`, `suffixes`.
  * Difference between `merge` (general) and `join` (on index).
* Merging DataFrames (`pd.merge()`)
  * Inner, Outer, Left, Right joins
* Joining on indexes (`.join()`)
* Combining data from multiple sources


---

## **10. Reshaping and Pivoting**
* `melt()` and `pivot()`
* Stacking and unstacking
* Wide vs long format
* MultiIndex and hierarchical indexing

### **Pivot Tables & Melting**
- `pd.pivot_table()` - multi-dimensional aggregation
- `.pivot()` - reshaping without aggregation
- `.melt()` - wide to long format
- `.stack()` and `.unstack()` - hierarchical indexing

* **Reshaping Data:**
    * Pivoting data: **`.pivot_table()`** (similar to pivot tables in spreadsheets).
    * Melting data: `pd.melt()` (wide to long format).
    * Stacking/Unstacking.

---

## **11. Working with Indexes**
* Setting and resetting indexes (`set_index()`, `reset_index()`)
* Hierarchical (multi-level) indexes
* Index sorting and selection
* Reindexing and alignment

---

## 12. (Working with) Time Series and Categorical Data
## 12. Time Series Analysis
* Converting to datetime (`pd.to_datetime()`)
* **Working with DateTimeIndex**
  * `pd.to_datetime()`: Converting to datetime
  * Setting a datetime column as the index.
  * `pd.date_range()`
  * Setting a DateTimeIndex.
  * Accessing date/time components (e.g., `.dt.year`, `.dt.day_name()`).
  * Resampling, shifting, and time zone handling.
* Date indexing and slicing
* **Time-Based Indexing & Slicing**
  * Partial string indexing: `df.loc['2020']`, `df.loc['2020-01']`
  * Slicing: `df.loc['2020-01-01':'2020-01-15']`
* **Resampling** (`resample()`)
  * Downsampling: `.resample('M').mean()` (to a lower frequency).
  * Upsampling: `.resample('D').ffill()` (to a higher frequency).
* Shifting and lagging (`shift()`, `tshift()`)
* Rolling and expanding windows (`rolling()`, `expanding()`)

### **DateTime Handling**
- `pd.to_datetime()` - parsing dates
- `pd.date_range()` - generating date sequences
- DateTimeIndex properties and methods
- Timezone handling with `tz_convert()`, `tz_localize()`

### **Time-Based Operations**
- Setting datetime index: `.set_index()`
- Time-based indexing: `df.loc['2023']`, `df.loc['2023-01':'2023-03']`
- Date properties: `.dt.year`, `.dt.month`, `.dt.day_name()`

### **Resampling & Rolling**
- **Resampling**: `.resample()` (up/down sampling)
  - Downsampling: 'D'→'M', 'H'→'D'
  - Upsampling: 'D'→'H' with filling/interpolation
- **Rolling operations**: `.rolling()` for moving averages
- **Expanding operations**: `.expanding()`

* **Categorical Data:**
    * Creating and converting to `category` dtype.
    * Benefits of using categorical data (memory and speed).
    * Getting dummy variables/one-hot encoding: **`pd.get_dummies()`**.
---

## **14. Performance Optimization**
* Memory usage and profiling (`memory_usage()`, `info(memory_usage='deep')`)
* Using `categorical` data types
* Vectorization over loops
* Chunked reading of large files
* Using `df.eval()` and `df.query()` for performance


### **Performance Optimization**
- Method chaining for readability
- Vectorized operations vs apply
- Efficient dtypes and memory usage
- `pd.eval()` for expression evaluation
- Using `.isin()` instead of multiple OR conditions

* **Performance and Optimization:**
    * Using optimized methods like `.at`, `.iat`, `.loc`, `.iloc` over iterative loops.
    * The efficiency of vectorized operations over **`.apply()`** (when possible).
    * Understanding **`copy()`** and "SettingWithCopyWarning" to avoid chained assignment issues.


---

## 15. Visualization with Pandas
* Plotting built-in (`df.plot()`, `plot(kind='bar')`, etc.)
* Histogram, line, bar, scatter, box plots
* Customizing plots (titles, labels, colors)
* Integration with Matplotlib and Seaborn

* **Integration with Visualization:**
    * Basic built-in plotting: **`.plot()`** (line, bar, hist, box plots).
    * Integration with Matplotlib and Seaborn (passing the DataFrame as data).

---

## 16. Advanced Topics
* MultiIndex operations
* Working with categorical data
* Handling large datasets (`chunksize`, `Dask`)
* Method chaining (using `pipe()`)
* Pandas options and settings (`pd.set_option()`)
* Style formatting (`df.style`)

### Categorical Data
- `astype('category')` for memory efficiency
- Ordered categories
- Performance benefits with groupby and sorting
* Benefits: Memory efficiency and performance for fixed, repeating values.

### MultiIndex DataFrames
- Creating MultiIndex (from_tuples, from_product)
- Indexing with MultiIndex (.loc with tuples)
- Cross-sections with `.xs()`
- Stacking and unstacking levels

4. **Styling DataFrames**
  * Using `.style` to apply conditional formatting for display in Jupyter notebooks.

2. **Handling Large Data**
  * Specifying `dtype` on import.
  * Using `chunksize` for iterative processing.
  * **Dask** as a parallel-computing alternative.

3. **Method Chaining**
  * Writing clean, readable code by chaining methods.
  * Example: `(df.load_data().query('age > 30').groupby('city')['income'].mean().round(2))`

---

## 17. Integration with Other Libraries
* Pandas + NumPy
* Pandas + Matplotlib / Seaborn
* Pandas + Scikit-learn (`train_test_split`, `get_dummies()`)
* Pandas + SQL / Databases

---

## 18. Real-World Case Studies / Practice
* Exploratory Data Analysis (EDA) workflow
* Cleaning messy datasets (missing values, inconsistent text)
* Combining datasets (merging, reshaping)
* Feature engineering with Pandas
* Time series analysis
* Generating reports or dashboards

## 12. Practical Patterns & Best Practices
### Common Operations
- Handling large datasets with chunksize
- Memory optimization with categoricals and dtypes
- Method chaining patterns
- Pipeline creation

### Troubleshooting & Debugging
- Common errors and solutions
- Performance profiling with `%timeit`
- Memory usage analysis
- Data validation techniques

### Integration with Other Libraries
- Visualization with Matplotlib/Seaborn
- Statistical analysis with SciPy/StatsModels
- Machine learning with Scikit-learn
- Web applications with Streamlit

## 13. Real-world Applications
- Data cleaning pipelines
- Exploratory Data Analysis (EDA) workflow
- Time series forecasting preparation
- Feature engineering examples
- Data validation and quality checks


### Pro-Tips for Your Notes:
* **Code Snippets:** For every topic, include a small, clear code example.
* **Common Pitfalls:** Note down common errors, like using chained assignment (`df[df.age > 25]['salary'] = 1000`), which should be avoided in favor of `.loc`.
* **"Cheat Sheet" Section:** Create a quick-reference page with the most common operations and their syntax.
* **Visuals:** Use diagrams to explain concepts like `groupby` (Split-Apply-Combine) and `merge` operations.