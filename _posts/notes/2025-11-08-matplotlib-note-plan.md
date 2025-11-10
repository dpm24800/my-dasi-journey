---
layout: post
title:  "Matplotlib – note plan"
author: Dipak Pulami Magar
date:   2025-11-08 10:12:45 +0545
categories: note-plans
status: draft
---
## **1. Introduction to Matplotlib**
* What is Matplotlib?
* Why use Matplotlib (vs Seaborn, Plotly, etc.)
* Installation (`pip install matplotlib`)
* Import conventions (`import matplotlib.pyplot as plt`)
* Understanding the pyplot interface
* Overview of Matplotlib architecture: Figure, Axes, Axis, Artist hierarchy

---

## **2. Basic Plotting**
* Creating simple line plots
  * `plt.plot()` basic syntax
  * Plotting multiple lines
  * Customizing line style, color, and width
* Adding labels and titles:
  * `plt.title()`, `plt.xlabel()`, `plt.ylabel()`
* Displaying grid: `plt.grid()`
* Showing and saving plots:
  * `plt.show()`, `plt.savefig()` (format options, dpi, bbox_inches)

---

## **3. Figure and Axes**
* Understanding the **object-oriented interface**
  * `fig, ax = plt.subplots()`
* Working with multiple subplots:
  * `plt.subplot()` vs `plt.subplots()`
  * Grid layout of plots
  * Adjusting spacing: `plt.tight_layout()` and `fig.subplots_adjust()`
* Controlling figure size and DPI
* Adding and managing multiple Axes in one Figure
* Using `add_subplot()` and `add_axes()`

---

## **4. Customization and Styling**
* Line properties: color (`color`, `c`), linewidth, linestyle, marker
* Marker customization: shape, size, edge color, face color
* Fonts and text properties:
  * `fontdict`, `fontsize`, `fontweight`, `fontstyle`
* Colors:
  * Named colors, RGB, RGBA, HEX
  * Using colormaps (`cmap`)
* Background and face color customization
* Global style settings:
  * `plt.style.use()`
  * Common styles (`'ggplot'`, `'seaborn'`, `'dark_background'`, etc.)
  * Creating custom styles

---

## **5. Common Plot Types**
### a. Line Plot
### b. Scatter Plot

* `plt.scatter()`
* Controlling marker size (`s`), color (`c`), alpha, and colormap

### c. Bar and Barh Plot
* `plt.bar()` and `plt.barh()`
* Grouped and stacked bars

### d. Histogram
* `plt.hist()`
* Bins, density, cumulative, histogram type

### e. Pie Chart
* `plt.pie()`
* Labels, explode, shadow, startangle, autopct

### f. Box Plot and Violin Plot
* `plt.boxplot()`, `plt.violinplot()`

### g. Area Plot (`plt.fill_between()`)
### h. Step Plot (`plt.step()`)
### i. Stem Plot (`plt.stem()`)
### j. Error Bars (`plt.errorbar()`)

---

## **6. Axes and Ticks**
* Setting axis limits: `plt.xlim()`, `plt.ylim()`
* Customizing tick marks: `plt.xticks()`, `plt.yticks()`
* Rotating tick labels
* Logarithmic scales: `plt.xscale('log')`, `plt.yscale('log')`
* Axis labels and formatting
* Twin axes: `ax.twinx()`, `ax.twiny()`
* Secondary axis: `ax.secondary_xaxis()`

---

## **7. Legends and Annotations**
* Adding legend: `plt.legend()` or `ax.legend()`
  * Location, labels, frame options, transparency
* Adding annotations and text:
  * `plt.text()`, `plt.annotate()`
  * Arrows, coordinates, alignment
* Customizing legend handles and labels

---

## **8. Working with Images**
* Displaying images: `plt.imshow()`
* Image interpolation and color maps
* Adjusting color bars: `plt.colorbar()`
* Reading and writing images with Matplotlib
* Rescaling and aspect ratio

---

## **9. Layout and Subplots**
* `plt.subplot()` basics
* Using `plt.subplots()` for complex layouts
* Sharing axes: `sharex`, `sharey`
* `GridSpec` for flexible layout control
* Adjusting spacing (`wspace`, `hspace`)
* Adding overall title: `fig.suptitle()`

---

## **10. Saving and Exporting Figures**
* `plt.savefig()` parameters:
  * Format (`.png`, `.jpg`, `.pdf`, `.svg`, `.eps`)
  * DPI, transparent background
  * `bbox_inches='tight'`
* Vector vs raster formats
* Exporting for web or publication

---

## **11. Advanced Customization**
* Using custom fonts and LaTeX text rendering (`rcParams['text.usetex'] = True`)
* Adding multiple legends
* Combining different plot types in one figure
* Polar plots: `projection='polar'`
* 3D plots: `mpl_toolkits.mplot3d`
  * `ax.plot3D()`, `ax.scatter3D()`, `ax.plot_surface()`

---

## **12. Matplotlib Configuration (rcParams)**
* Overview of `matplotlib.rcParams`
* Temporary style using `plt.rc_context()`
* Persistent custom styles using `.matplotlibrc`
* Setting figure size, font, line width globally

---

## **13. Integration with Other Libraries**
* Plotting Pandas DataFrames (`df.plot()`)
* Integration with NumPy arrays
* Using Matplotlib with Seaborn, Plotly, or Scikit-learn
* Interactive plots in Jupyter Notebook (`%matplotlib inline`, `%matplotlib notebook`)

---

## **14. Interactivity and Animation**
* Interactive mode (`plt.ion()`)
* Adding widgets and sliders
* Animations using `FuncAnimation`
* Saving animations as `.gif` or `.mp4`

---

## **15. Practical Use Cases and Projects**
* Plotting time series data
* Visualizing statistical distributions
* Correlation matrix heatmaps
* Visualizing confusion matrices
* Real-world examples: stock trends, sensor data, etc.

---

## **16. Common Errors and Debugging**
* “Figure size too small” or DPI issues
* Overlapping labels
* Missing legend labels
* `RuntimeError: Invalid DISPLAY variable` (for headless systems)
