# Note

- Convert Unix timestamps into excel format

  - https://www.extendoffice.com/documents/excel/2473-excel-timestamp-to-date.html
  - "=(((A1/60)/60)/24)+DATE(1970,1,1)"
  - ![image](https://cdn.extendoffice.com/images/stories/doc-excel/convert-date-unixtimestamp/doc-convert-timestamp-4.png)

- countifs

  - https://support.microsoft.com/en-us/office/countifs-function-dda3dc6e-f74e-4aee-88bc-aa8c2a866842

- Standard Deviation
  - The standard deviation is a measure of how spread out numbers are
  - a measure of the extent to which data varies from the mean.
  - If the data is close together, the standard deviation will be small.
  - if the data is spread out, the standard deviation will be large.
  - **Describes how spread out the data is from the mean**
  - Calculated from the square root of the variance
  - In the same units of measurement as the mean
- Variance
  - The average of the **squared** differences from the Mean
  - measures the average degree to which each number is different from the mean.
  - **Used to describe how far values in the data set are from the mean**
  - **Describes how much variation exists in the data**
  - **Variance considers the distance of each value in the data set from the center of the data**
  - describe the variability of the observations from its arithmetic mean
  - Variance measure how far individuals in the group are spread out from the mean
  - the variance is greater when there is a wider range of numbers in the group.
  - the variance is less when there is a narrower range of numbers.
- Mean
  - The arithmetic average
  - The **AVERAGE** OF ALL NUMBERS
- Midium
  - The number in the **MIDDLE** when they are IN ORDER
- Mode

  - The most repetitive nmber

- Z-Score

  - Describe **a single value's distance** from the mean of the data set
  - The distance is in terms of standard deviations
  - Can be positive or negative
    - if positive, the value is greater than the mean
    - if negative, the value is less than the mean
  - The smaller the z-score, the closer the value is to the mean

- Extreme values

  - Real world data can contain extreme values
  - Some summary statistics such as the mean take into account all values of a data set
  - Extreme values can skew these statistics
  - Extreme values may not always be reliable
    - In data science, extreme values are often suspicious
    - Suspicious values are called **potential outliers**
    - An **outlier** is a data point that differs from the rest of a data set
    - Outliers can inaccurately skew a data set
      - Can causes us to misrepresent the actual data

- Quantiles

  - Quantiles seperate a sorted data into equal-sized fragments
  - Quantiles divide the data set into four equal parts
    - while percentiles divide the data set into 100 equal parts

- Potential outliers
  - To identify potential outliers quantitatively
    - outlier boundaries = 1.5 IQR
      - IDR is the interquartile range, or the range between the 1st and 3rd quartiles
      - Anything below **Q1 - 1.5 IQR** could be an outlier
      - Anything above **Q3 - 1.5 IQR** could be an outlier
  - Box and Whiskers Plot / Box plot
    - ![image](https://github.com/Simon-Xu-Lan/coding-notes/blob/master/pictures/Box_and_whisker_plots.png)
