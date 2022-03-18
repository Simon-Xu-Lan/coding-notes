## Matplotlib

- A Python Library that Visualizes a Dataset
- Types of datasets include:
  - Pandas DataFrames
  - Lists, tuples, and dictionaries
  - NumPy arrays
- Types of visualizations include:

  - Bar charts
  - Pie charts
  - Line charts
  - Scatter plots

- General plotting process using pyplot

1. Create your dataset.

   - Data can be generated from functions, pulled from Pandas DataFrames, etc

2. Generate your plot.

   - Use the **pyplot.plot()** function to tell Matplotlib what data to use and which plot to make

3. Customize your plot

   - Change the axis,
   - label the figures,
   - color the data points
   - make the plot as informative to the reader as possible.

- Steps to improve readability of plots

1. Add labels to x and y axis

   ```py
     plt.xlabel()
     plt.ylabel()
   ```

2. Add title to plots

   ```py
     plt.title()
   ```

3. Limit the boundaries oa the x and y axes

   ```py
     plt.xlim()
     plt.ylim()
   ```

❓❓❓ why here is axes slides 24

- Adding labels makes graphics easier to understand and prevents them from being inadvertently misleading.
  - Limiting the range of the plot maximizes the data-to-ink ratio:
  - “Ink” used to make data/Total “ink” of the plot
  - It’s best to use the least amount of ink to show the most amount of data

❓❓❓ low data-to-ink ratio slide 26

## It's very important to choose the right plot for a given dataset

- Bar Charts
  - Useful for comparing different entities to one another
  - Bar charts help to visualize **UniVariate data**
    - Univariate data refers to data with one variable, or one type of measurement.
    - eg.
      - Amount of rainfall, in inches
      - Number of votes in a poll
      - Number of people per category
    - Bar charts are particularly useful when a single variable is being counted multiple times.
  - Bar charts are NOT effective for visualizing bivariate data
    - Bivariate data refers to data with two variables.
      -Anything you can plot as a line or scatter plot is bivariate data.
      - Example: A dataset comparing the number of ice cream bars sold versus daily temperature.
- Pie Charts

  - Useful for demonstrating different elements of a complete dataset
  - Pie Charts Help Visualize Simple Categorical Data
    - Pie charts are great for visualizing data that is percentages, or proportions.
    - Examples:
      - Proportion of Democrat versus Republican versus independent voters
      - Percentage of children’s favorite story characters
      - Distribution of left-handed versus right- handed pitchers in baseball
    - Fewer categories increase the effectiveness of a pie chart.
  - Pie charts are NOT effective for large or multivariate data
    - With more than ~10 categories, pie charts become too crowded and lose effectiveness.
    - Like bar charts, pie charts are only effective for visualizing univariate data.
    - When in doubt, just use a bar chart.

- Scatter Plots

  - Useful for displaying where values fall in respect to two factors
  - Powerful visualizations for bivariate data
    - Bivariate data refers fo data with two variables
      - Each data point is a combination of two variables
      - Anything plotted on an x- and y-axis is bivariate data.
      - Example: The amount of ice cream sold per daily temperature
    - Scatter plots are helpful for visualizing large datasets (i.e., thousands of data points).
    - Scatter plots are frequently used to visualize clustering in a dataset.
  - Scatter plots are NOT effective for continuous measurements.

    - When data is continuous, we’ll often want to interpolate between measurements.
      - The most common continuous data is time series.
    - Scatter plots visualize “scattered” data, so interpolation is almost impossible.
    - Line plots allow the audience to read between the data points.

  - np.arange(start, end, step)

  - the [Matplotlib documentation](https://matplotlib.org/2.0.2/index.html) to see what additional formatting could be added to the chart.

## Difference between "axes" and "axis" in matplolib

- Axis is the axis of the plot, the thing that gets ticks and tick labels. The axes is the area your plot appears in.
- https://stackoverflow.com/questions/5575451/difference-between-axes-and-axis-in-matplotlib
- This figure from the documentation will answer your question:
- ![figue](https://i.stack.imgur.com/HZWkV.png)

  - Figure:
    - The whole figure (marked as the outer red box).
    - The figure keeps track of all the child Axes,
    - The canvas
    - A figure can have any number of Axes, but to be useful should have at least one.
    ```py
      fig = plt.figure()  # an empty figure with no axes
      fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
    ```
  - Axes:

    - This is what you think of as ‘a plot’.
    - it is the region of the image with the data space (marked as the inner blue box).
    - A given figure can contain many Axes, but a given Axes object can only be in one Figure.
    - The Axes contains two (or three in the case of 3D) Axis objects
      - Axis is the object which take care of the data limits
      - the data limits can also be controlled via set via the set_xlim() and set_ylim() Axes methods

  - Axis / plot

    - These are the number-line-like objects (circled in green).
    - it is the region of the image with the data space
    - They take care of setting the graph limits
    - generating the ticks (the marks on the axis)
    - generating ticklabels (strings labeling the ticks).

  - Artist
    - Basically everything you can see on the figure is an artist (even the Figure, Axes, and Axis objects).
    - This includes Text objects, Line2D objects, collection objects, Patch objects
    - all of the artists are drawn to the canvas.
    - Most Artists are tied to an Axes;
      - such an Artist cannot be shared by multiple Axes, or moved from one to another.
