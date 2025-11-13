
### Core Data Structures
- Series: Creation, attributes, operations
  - From lists, dictionaries, scalars
  - Indexing, slicing, and alignment

- DataFrame: Creation, attributes, columns, rows
  - From dictionaries, lists, NumPy arrays, other DataFrames
  - Column selection, addition, deletion
  - Row selection, addition, deletion
  
- Index objects: Types (Index, MultiIndex, DatetimeIndex)
  - Index properties and methods
  - Hierarchical indexing (MultiIndex)

- Panel (deprecated, but note alternatives like xarray)


### Viewing and Inspecting Data
- 
- Column and index inspection (.columns, .index, .dtypes)
- Transposing (.T)

### Indexing, Selecting, and Filtering Data
- Basic indexing: 
  - Label-based (.loc), position-based (.iloc), mixed (.ix deprecated)
- Slicing rows and columns
- Boolean indexing and conditional selection
- Advanced indexing: MultiIndex slicing, xs method
- Setting and resetting index (.set_index(), .reset_index())
- Query method (.query()) for SQL-like filtering
- Attribute access (df.column_name)

### Data Cleaning and Preparation
- Handling missing data
  - Detection (.isnull(), .notnull())
  - Dropping (.dropna(): axis, how, thresh)
  - Filling (.fillna(): method like ffill, bfill; value)
  - Interpolation (.interpolate())
- Dealing with duplicates
  - Detection (.duplicated())
  - Removal (.drop_duplicates(): subset, keep)
- Data type conversions (.astype(), pd.to_numeric(), pd.to_datetime())
- Renaming columns and indices (.rename())
- Replacing values (.replace())
- String methods for text data (.str accessor: lower, upper, split, etc.)
- Categorical data: Creation, ordering, categories management

### Data Manipulation and Transformation
- Ranking (.rank())
- Applying functions (.apply(), .map(), .applymap())
- Element-wise operations (arithmetic, comparison)
- Window functions: Rolling, expanding (.rolling(), .expanding(): mean, sum, etc.)
- Aggregation (.agg(): custom functions)
- Transformation (.transform())

### Merging, Joining, and Concatenating
- Concatenation (.concat(): axis, join, ignore_index)
- Merging (.merge(): how (inner, outer, left, right), on, suffixes)
- Joining (.join(): on index or columns)
- Appending (.append() deprecated, use concat)
- Handling overlapping data
- Database-style joins with indicators

### Grouping and Aggregation
- GroupBy mechanics: Splitting, applying, combining
- Grouping by columns, levels, functions
- Aggregation functions: sum, mean, count, std, etc.
- Multiple aggregations (.agg() with dict)
- Transformation and filtration (.transform(), .filter())
- Grouping with MultiIndex
- Pivot tables (.pivot_table(): values, index, columns, aggfunc, fill_value)
- Cross-tabulation (.crosstab())

### Time Series and Date Functionality
- Date/time types: Timestamp, DatetimeIndex, Period
- Parsing dates (pd.to_datetime())
- Date offsets and frequency
- Resampling (.resample(): upsampling, downsampling)
- Time zone handling (.tz_convert(), .tz_localize())
- Period and PeriodIndex
- Time deltas (pd.Timedelta)
- Shifting and lagging (.shift())
- Rolling time windows

### Advanced Topics
- Categorical data: Memory efficiency, ordering, categories
- Nullable types: Integer, Boolean
- Sparse data structures: SparseSeries, SparseDataFrame
- Styling DataFrames (.style: formatting, highlighting)
- Visualization integration (.plot(): kinds like line, bar, hist; matplotlib kwargs)
- Options and settings (pd.options.display, pd.set_option())
- Performance enhancements: Vectorization, eval/query engines, caching
- Integration with other libraries: NumPy, SciPy, scikit-learn
- Extensions: Custom accessors, extension arrays

### Data Analysis and Statistics
- Correlation and covariance (.corr(), .cov())
- Unique values and membership (.unique(), .isin())
- Histogramming and discretization (.cut(), .qcut())
- Dummy variables (.get_dummies())
- Factorizing values (.factorize())



### Best Practices and Common Pitfalls
- Avoiding chained assignment warnings
- Copy vs. view (.copy())
- Handling large datasets efficiently
- Debugging common errors (KeyError, SettingWithCopyWarning)
- Frequently Asked Questions (e.g., from official docs)

### Resources and Ecosystem
- Official documentation and cheatsheets
- Tutorials and cookbooks
- Community resources (Stack Overflow, GitHub)
- Related libraries and tools (Dask for scaling, Vaex for out-of-core)