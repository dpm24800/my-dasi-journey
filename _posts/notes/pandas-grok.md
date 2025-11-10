
## 1. **Pandas Fundamentals**
| Sub-topic | Key Points |
|-----------|------------|
| **Installation & Import** | `pip install pandas`, `import pandas as pd`, `import numpy as np` |
| **Core Data Structures** | `Series`, `DataFrame`, `Index` (immutable, label-based) |
| **Creating Objects** | `pd.Series()`, `pd.DataFrame()`, from dict/list/NumPy/array/CSV |
| **Attributes** | `.shape`, `.ndim`, `.size`, `.dtypes`, `.index`, `.columns`, `.values` |
| **Memory Usage** | `.memory_usage()`, `deep=True` |

---

## 2. **Indexing & Selection**
| Sub-topic | Key Points |
|-----------|------------|
| **Label vs Position** | `.loc[]` (label), `.iloc[]` (position), `.at[]`, `.iat[]` |
| **Boolean Indexing** | Mask creation, chaining, `.isin()`, `.query()` |
| **MultiIndex / Hierarchical Indexing** | Creating (`pd.MultiIndex.from_tuples`), slicing, `xs()`, `swaplevel()` |
| **Index Operations** | `.set_index()`, `.reset_index()`, `.reindex()`, `.sort_index()` |
| **Alignment** | Automatic alignment on labels, `NaN` handling |

---

## 3. **Data Input / Output**
| Sub-topic | Key Points |
|-----------|------------|
| **Flat Files** | `read_csv`, `to_csv`, `read_table`, `read_fwf` |
| **Excel** | `read_excel`, `ExcelWriter`, `to_excel` |
| **JSON** | `read_json`, `to_json` (orient options) |
| **SQL** | `read_sql`, `to_sql`, SQLAlchemy engine |
| **Clipboard / HTML / SAS / Stata** | `read_clipboard`, `read_html`, etc. |
| **Compression & Large Files** | `compression=`, `chunksize`, `iterator=True` |
| **Feather / Parquet / HDF5** | Fast binary formats, `engine='pyarrow'` |

---

## 4. **Data Cleaning & Preparation**
| Sub-topic | Key Points |
|-----------|------------|
| **Missing Data** | `isnull()`, `notnull()`, `dropna()`, `fillna()` (ffill/bfill, interpolation) |
| **Duplicates** | `duplicated()`, `drop_duplicates()` |
| **String Methods** | `.str.` accessor (lower, contains, replace, split, extract) |
| **Type Conversion** | `astype()`, `pd.to_numeric()`, `pd.to_datetime()`, `pd.to_timedelta()` |
| **Category Type** | `astype('category')`, `.cat` accessor |
| **Outliers & Validation** | Custom functions, `assert_frame_equal` |

---

## 5. **Data Transformation**
| Sub-topic | Key Points |
|-----------|------------|
| **Adding / Deleting Columns** | `df['new'] = ...`, `assign()`, `drop()` |
| **Apply, Map, Applymap** | `Series.map`, `DataFrame.apply`, `DataFrame.applymap` (deprecated → `map`) |
| **Vectorized Operations** | NumPy ufuncs, arithmetic, comparison |
| **Binning** | `pd.cut`, `pd.qcut` |
| **Dummy / One-Hot Encoding** | `pd.get_dummies`, `explode` |
| **Pivot & Melt** | `pivot`, `pivot_table`, `melt`, `stack`, `unstack` |
| **Crosstab** | `pd.crosstab` |

---

## 6. **Grouping & Aggregation (GroupBy)**
| Sub-topic | Key Points |
|-----------|------------|
| **Splitting** | `df.groupby(level/by)` |
| **Aggregation** | `.agg()`, multiple functions, named agg (`{'col': ['mean','sum']}`) |
| **Transformation** | `.transform()` (e.g., z-score per group) |
| **Filtration** | `.filter()` |
| **Applying Custom Functions** | `.apply()` on GroupBy object |
| **Grouped Iteration** | `for name, group in grouped:` |
| **Expanding / Rolling** | `.expanding()`, `.rolling()` with GroupBy |

---

## 7. **Time Series & Date Functionality**
| Sub-topic | Key Points |
|-----------|------------|
| **Date Parsing** | `pd.to_datetime`, `format=`, `errors=` |
| **Date Ranges** | `pd.date_range`, `period_range`, `timedelta_range` |
| **Resampling** | `.resample('M')`, `ohlc`, `asfreq` |
| **Time Zones** | `tz_localize`, `tz_convert`, `pytz` / `dateutil` |
| **Shifting / Lagging** | `.shift()`, `.pct_change()` |
| **Window Functions** | `.rolling()`, `.ewm()` |
| **Holiday Calendars** | `pd.offsets`, `CustomBusinessDay` |

---

## 8. **Merging, Joining, Concatenating**
| Sub-topic | Key Points |
|-----------|------------|
| **Concat** | `pd.concat([df1,df2], axis=, join=, keys=, ignore_index=)` |
| **Merge** | `pd.merge(left, right, on=, how=, suffixes=, validate=)` |
| **Join** | Instance method `.join()` on index |
| **Update / Combine** | `.combine_first()`, `.update()` |

---

## 9. **Reshaping & Wide-to-Long**
| Sub-topic | Key Points |
|-----------|------------|
| **Stack / Unstack** | MultiIndex ↔ columns |
| **Pivot Table** | `pivot_table(values, index, columns, aggfunc, margins)` |
| **Melt** | `melt(id_vars, value_vars, var_name, value_name)` |

---

## 10. **Performance & Memory Optimization**
| Sub-topic | Key Points |
|-----------|------------|
| **Data Types** | Downcast `int64→int32`, `float64→float32`, `category` for low-cardinality strings |
| **Copy vs View** | `.copy()`, avoiding chained assignment (`SettingWithCopyWarning`) |
| **Eval / Query** | `df.eval()`, `df.query()` for faster arithmetic / filtering |
| **Chunking Large Files** | `chunksize` with `read_csv` |
| **Categorical Joins** | Faster merges on categorical keys |
| **Sparse Data** | `SparseDataFrame` / `SparseSeries` |
| **Parallel Apply** | `swifter`, `dask`, `modin` (external) |

---

## 11. **Visualization (Integrated)**
| Sub-topic | Key Points |
|-----------|------------|
| **Plotting** | `.plot()`, kind= (`line`,`bar`,`hist`,`box`,`scatter`), `subplots=True` |
| **Integration** | Matplotlib backend, `pandas.plotting` (scatter_matrix, parallel_coordinates) |

---

## 12. **Advanced Topics**
| Sub-topic | Key Points |
|-----------|------------|
| **Styler** | `df.style.format`, conditional formatting, bar charts in cells |
| **Options & Settings** | `pd.set_option`, `pd.describe_option` |
| **Extension Arrays** | Custom dtypes (`pd.api.types`) |
| **Testing** | `pd.testing.assert_frame_equal`, `assert_series_equal` |
| **Integration with Other Libraries** | NumPy, SciPy, scikit-learn (`X.values`), Polars, Dask, Vaex |

---

## 13. **Common Pitfalls & Best Practices**
1. **Chained Indexing** → Use `.loc` in one go.  
2. **Modifying a Slice** → Always `.copy()` if needed.  
3. **In-place Operations** → Prefer `inplace=True` or reassign for clarity.  
4. **Memory Explosion** → Avoid `df.apply(lambda row: ...)` on large frames; use vectorized ops.  
5. **Datetime Naivety** → Always localize if mixing time zones.  
6. **Categorical Ordering** → Set `ordered=True` when order matters.  

---

## Suggested Note Structure (Markdown / Jupyter)

```markdown
# Pandas Mastery Notes

## 1. Fundamentals
- [x] Installation
- [x] Series vs DataFrame
- Code: `pd.Series([...])`

## 2. Indexing
### 2.1 .loc / .iloc
```python
df.loc[rows, cols]
```

### Common Pitfall: SettingWithCopyWarning
> **Fix:** `df = df.copy()` or use `.loc`


## Cheat Sheet (Appendix)
| Task | Code |
|------|------|
| Read CSV | `pd.read_csv('file.csv', dtype={'id': 'category'})` |
| Group & agg | `df.groupby('cat')['val'].agg(['mean','sum'])` |
```

---

### How to Use This Outline
1. **Create one markdown/Jupyter cell per sub-topic.**  
2. **Include 1–3 minimal, reproducible code examples** per cell.  
3. **Add a “Gotcha” box** for pitfalls.  
4. **End each major section with a mini-exercise** (e.g., “Load `titanic.csv` and compute survival rate by class and gender”).  

With this structure, your Pandas notes will be **complete, searchable, and exam/project-ready**. Happy data wrangling!



