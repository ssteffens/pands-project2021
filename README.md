# Programming and Scripting 2021 - Project

## Analysis of the Fisher Iris Data Set

<br />

This repository contains a program analysis.py which carries out analysis of the Iris flower data set. It produces various output files displaying results of the analysis. 

<br />

---
### **Introduction**
The Iris flower data set was first published as part of a research paper by British statistician and geneticist R.A. Fisher in 1936. Its content describes how to cperform linear discriminant analysis as a statistical method to recognise patterns and to differentiate between two or more classification groups. 
<br />
For Fisher's research, samples were taken of 150 Iris flowers, 50 each of three different species (Iris setosa, Iris virginica and Iris versicolor). Each flower's sepals and petals were measured, resulting in a data set containing: 
<br />
- Length of sepals (in centimetres)
- Width of sepals (in centimetres)
- Length of petals (in centimetres)
- Width of petals (in centimetres)
- Name of the species

Because of its relatively small size and consistent data profile, the Iris flower data set has been used in numerous publications as well as for training and doemonstration purposes. 
<br />
<br />

**References:**
<br />

R. A. Fischer (1936): The Use Of Multipe Measurements In Taxonomic Problems, accessed through http://hdl.handle.net/2440/15227 
<br />
General information on Iris flower data set:
<br />
https://archive.ics.uci.edu/ml/datasets/Iris
<br />
https://en.wikipedia.org/wiki/Iris_flower_data_set


<br />

---
### **Information Gathering**
As a first step to start analysis of the Iris data set, I began with getting an understanding of what the data set is, where it originated and how it was used. 

For a broader overview of the actual data, my initial investigation also included looking at the different Iris species, and understanding the terms petal and sepal and which part of a flower they are referring to. 

A useful resource was an online article about using Python for a machine learning project. It makes use of the Iris data set, and the first part outlines an approach to start investigating and analysing a data set with Python. I used this as an inspiration for structuring my own program. 

- Function for reading the data
- Function for filtering the data by species
- Functions creating the various outputs
- main() function which runs the program by calling the previously defined functions
<br />
<br />

**References:**
<br />

General Information on Iris flower data set: 
<br />
https://en.wikipedia.org/wiki/Iris_flower_data_set
<br />
https://archive.ics.uci.edu/ml/datasets/Iris
<br />
R. A. Fischer (1936): The Use Of Multipe Measurements In Taxonomic Problems, accessed through http://hdl.handle.net/2440/15227
<br />
https://en.wikipedia.org/wiki/Ronald_Fisher


Iris plants: 
<br />
https://en.wikipedia.org/wiki/Iris_(plant) 
<br />
https://en.wikipedia.org/wiki/Flower#Floral_parts 


Analysing the data set: 
<br />
https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ 


<br />

---
### **Obtaining the Data Set**
As the Iris data set is very commonly used for data investigation and teaching purposes, it can be found in numerous locations online. There is a large variety of sources ranging from scanned copies of the original paper to .csv and other data files.  It is also included in the sklearn library of Python so it can be accessed without having to download a data file or referencing it from an online source. 

For this project, I opted to use the .data file provided by the University of California, Irvine. On their website, two versions of the data set are available: 
- The one originally used by the university since 1988. However, two of the data attributes captured in this file differ from the original data set published by Fisher. 
- An updated version reflecting the original data set 

I have used the updated version (called bezdekIris.data on the UCI website) and saved it to the pands-project201 folder as iris.data. 
<br />
<br />

**References:**
<br />

Data file source: 
<br />
https://archive.ics.uci.edu/ml/datasets/Iris


<br />

---
### **Reading the Data Set into Python - Program Part 2**
To be able to call dat from the data set to a Python program, I defined a function (`read_data()`) which uses the pandas `read_table()` function to read the data from the iris.data file as comma separated values. It also assigns headers for easier differentiation of columns. The function returns a variable called "data" which is being called and distributed to the sub-functions by the `main()` function. 
<br />
<br />

**References:**
<br />

Adding headers to the dataset: https://realpython.com/python-csv/ 

<br />

---
### **Analysing the Data Set**
As a first approach for familiarising myself with the data, I used several inbuilt Python and pandas functions which provide an overview of the data set: 
- `print(data)`: Prints out the whole data set
- `data.shape()`: Returns the number of columns and rows in the data set
- `data.info()`: For each column returns the data types, row count and count of non-null values
- `data.describe()`: For each column returns the count of records, average, minimum and maximum values, median and quartiles

Using these functions I was able to determine that the data set consists of 5 columns and 150 rows. 4 of the columns contain floating point numbers which allows for using them for arithmetic and statistics calculations. The data set contains no empty ("null") fields making it easily usable for calculations because there is no requirement to filter out or omit emppty values. 

The remaining column contains integer values - referred to as "object" in pandas - and references the species of Iris plant. 
<br />
<br />

In addition to showing summaries of the whole data set, I wanted to be able to show some of the above information by individual Iris species. As writing a filtering argument for each species and each function soon became a somewhat repetitive and tedious task, I investigated how to define a filtering function which could subsequently be used for filtering the data set. 

These filters can be found in sections 3.1 to 3.3 of the program. 
<br />
<br />

**References:**
<br />

`Describe()` function: 
<br />
https://www.w3resource.com/pandas/dataframe/dataframe-describe.php 
<br />
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html


Pandas data types: 
<br />
https://pbpython.com/pandas_dtypes.html


Filter functions: 
<br />
https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#where
<br />
https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#where

<br />

---
### **Summary of Data Set in Text File (datasummary.txt) - Program Part 4**
To provide a summary of the data set, I defined a function which outputs the result of several statistical summaries to a text file using the pandas `write()` function.

These include a sample of the data set (one row for each species), row and column count and the data type of each column. 

First I applied the `describe()` function to the whole data set. In addition, I also used `describe()` in combination with the `groupby()` function to provide analysis for each of the four attributes (sepal length and width, petal length and width). 
<br />
<br />

**Output file created:**
<br />
- datasummary.txt 
<br />
<br />

**References:**
<br />

Outputting content of a data set to a text file: 
<br />
https://izziswift.com/python-pandas-write-content-of-dataframe-into-text-file/


Counting rows and columns of a data set: 
<br />
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html
<br />
https://pythonexamples.org/pandas-dataframe-count-rows/  


Getting information on data types of columns:
<br />
https://www.geeksforgeeks.org/count-number-of-columns-of-a-pandas-dataframe/
<br />
https://www.datasciencemadesimple.com/get-data-type-of-column-pandas-python-2/ 
<br />
https://pbpython.com/pandas_dtypes.html


Transposing table data:
<br />
https://note.nkmk.me/en/python-pandas-t-transpose/ 


Selecting a single column in pandas:
<br />
https://datagy.io/pandas-select-columns/

<br />

---
### **Part 5 - Histogram of each Variable in .png File - Program Part 5**
For the histograms of each variable, I combined four histograms for each attribute into one figure, using the `pyplot.subplots()` function. It gives the flexibility to add single plots to one joint figure, specifying how many subplots should be displayed per row and column. As I was aiming to display four histograms, I opted for a 2x2 matrix.


I defined separate functions for each of the four variables, which create the four subplots for the whole data set and the three individual species. For filtering the species, I used the filter functions created previously. 
<br />
<br />

**Output files created:**
<br />
- sepallength.png 
- sepalwidth.png
- petallength.png
- petalwidth.png
<br />
<br />

**References:**
<br />

Creating a histogram from data in a data set: 
<br />
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.hist.html


Displaying 4 different histograms on one page: 
<br />
https://www.python-graph-gallery.com/25-histogram-with-several-variables-seaborn 
<br />
https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html#sphx-glr-gallery-statistics-histogram-multihist-py
<br />
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html 


Managing layout of subplots:
<br />
https://matplotlib.org/stable/gallery/lines_bars_and_markers/spectrum_demo.html#sphx-glr-gallery-lines-bars-and-markers-spectrum-demo-py 


Specifying colours: 
<br />
https://matplotlib.org/stable/tutorials/colors/colors.html 


<br />

---
### **Scatter Plots of each Pair of Variables - Program Part 6**
After numerous unsuccessful attempts to create a plot with a meaningful legend using pandas or pyplot, I began looking into other options for plotting scatter plots. 
The seaborn library turned out to be a suitable solution. Using the seaborn lmplot also shortened the code compared to the initial attemps because, for example, axis titles automatically included and do not need to be specifically added.  


The findings of the original Fisher study are clearly replicated in the scatter plots: One of the species (Iris setosa) can be distinguished from the other two by pairing the length and width of their sepals and petals. 
<br />
<br />

**Output files created:**
<br />
- petlenpetwid.png
- seplensepwid.png
- petlenseplen.png
- petlensepwid.png
- petwidseplen.png
- petwidsepwid.png
<br />
<br />

**References:**
<br />

Creating a scatter plot from a pandas data set: 
<br />
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html

Scatter plots with pandas and matplotlib (not used in final program version):
<br />
https://www.w3schools.com/python/pandas/pandas_plotting.asp
<br />
https://datascienceparichay.com/article/create-scatter-plot-python-matplotlib/
<br />
https://datascienceparichay.com/article/scatter-plot-from-pandas-dataframe/
<br />
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
<br />
https://www.delftstack.com/howto/matplotlib/scatter-plot-legend-in-matplotlib/ 
<br />
https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/
<br />
https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html#sphx-glr-tutorials-intermediate-legend-guide-py 



Seaborn lmplot: 
<br />
https://seaborn.pydata.org/generated/seaborn.lmplot.html
<br />
https://pythonbasics.org/seaborn-line-plot/

Seaborn colour legends:
<br />
https://www.python-graph-gallery.com/43-use-categorical-variable-to-color-scatterplot-seaborn 
<br />
https://stackoverflow.com/questions/38362573/assign-map-colors-to-the-points-in-seaborn-regplot-python-3

Seaborn adding a title: 
<br />
https://www.statology.org/seaborn-title/
<br />
https://www.dataforeverybody.com/change-seaborn-title-chart-axes-font/ 

Seaborn solution for cut off title:
<br />
https://github.com/streamlit/streamlit/issues/336 

<br />

---
### **Main function - Program Part 7/8**
The `main()` function calls all the separated functions to be executed in a row. It also passes arguments of the data set on to the individual functions. 

The `main()` function itself is called by an if __name__ == "__main__" statement. 

<br />

---
### **Part 8 - Conclusion**
Using Python for analysing the Iris flower data set offered a huge number of options for carrying out the actual analysis and presenting the findings as text format and visual outputs. The different libraries and modules used while writing this program provided a lot of flexibility for summarising, analysing and formatting the data.  