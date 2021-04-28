# This program analyses the Fisher Iris data set and outputs:
    # A summary of each veriable to a single text file
    # A histogram of each variable to png files
    # A scatter plot of each pair of variables to png files
# Author: Stefanie Steffens 


# Data source: http://archive.ics.uci.edu/ml/machine-learning-databases/iris/, using the "bezdekIris.data" dataset



# First step: Import the pandas library to allow accessing the data in the file as a data frame and the matplotlib.pyplot module to facilitate plotting of data.

import pandas as pd
import matplotlib.pyplot as plt



# Second step: Define a function which reads in the dataset from the iris.data file. 
# Referenxce for adding headers to the dataset: https://realpython.com/python-csv/

def read_data():
    dataset = pd.read_table("iris.data", sep=",", names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
    return(dataset)



# Third step: Define functions that enable filtering the data by iris species
# These filter the data set by the three different species and can be used as arguments for the various analysis functions. This avoids repetitively defining filtering variables for each function.
# Reference: https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#where

# 3.1 Filter for setosa species
def filter_setosa(data):
    setosa = (data[data["Species"] == "Iris-setosa"])
    return(setosa)


# 3.2 Filter for versicolor species
def filter_versicolor(data):
    versicolor = (data[data["Species"] == "Iris-versicolor"]) 
    return(versicolor)


# 3.3 Filter for virginica species
def filter_virginica(data):
    virginica = (data[data["Species"] == "Iris-virginica"])
    return(virginica)



# Forth step: Define a function to output a summary of each variable to a text file
# Reference: https://izziswift.com/python-pandas-write-content-of-dataframe-into-text-file/

def text_overview(data):
    with open ("datasummary.txt", "wt") as f:
        describe_all = data.describe()
        transp = describe_all.transpose()                                           # transpose the describe_all table so that it's aligned with the format of the describe tables of the individual species
        describe_seplen = data.groupby('Species')['Sepal Length'].describe()
        describe_sepwid = data.groupby('Species')['Sepal Width'].describe()
        describe_petlen = data.groupby('Species')['Petal Length'].describe()
        describe_petwid = data.groupby('Species')['Petal Width'].describe()

        f.write("OVERVIEW OF IRIS DATASET\n\n")
        f.write("Overview for all Species\n")
        f.write(transp.to_string())                                                 
                                                                                    # source: https://note.nkmk.me/en/python-pandas-t-transpose/
        f.write("\n\n\n\nOverview for Sepal Length by Species\n")
        f.write(describe_seplen.to_string())
        f.write("\n\n\n\nOverview for Sepal Width by Species\n")
        f.write(describe_sepwid.to_string())
        f.write("\n\n\n\nOverview for Petal Length by Species\n")
        f.write(describe_petlen.to_string())
        f.write("\n\n\n\nOverview for Petal Width by Species\n")
        f.write(describe_petwid.to_string())



# Fifth step: Define functions to output histograms for each variable to png files
# References used: 
    # For displaying 4 different histograms on one page: https://www.python-graph-gallery.com/25-histogram-with-several-variables-seaborn 
    # https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html#sphx-glr-gallery-statistics-histogram-multihist-py


# 5.1 Histograms for Sepal Length - All data vs species
def hist_seplen(data, setosa, versicolor, virginica):
    fig, axs = plt.subplots(nrows=2, ncols=2)                                       # defines the output, display 4 plots in 2 rows, 2 columns
    data["Sepal Length"].hist(color = 'black', ax=axs[0,0])                         # all data
    setosa["Sepal Length"].hist(color = '#8D66BE', ax=axs[0, 1])                        # setosa
    versicolor["Sepal Length"].hist(color = '#7938C4', ax=axs[1, 0])                   # versicolor
    virginica["Sepal Length"].hist(color = '#7782B0', ax=axs[1, 1])                   # virginica
    fig.tight_layout()
    plt.savefig("sepallength")


# 5.2 Histograms for Sepal Width
def hist_sepwid(data, setosa, versicolor, virginica):
    fig, axs = plt.subplots(nrows=2, ncols=2)
    data["Sepal Width"].hist(color = 'black', ax=axs[0,0])                         # all data
    setosa["Sepal Width"].hist(color = 'red', ax=axs[0, 1])                        # setosa
    versicolor["Sepal Width"].hist(color = 'blue', ax=axs[1, 0])                   # versicolor
    virginica["Sepal Width"].hist(color = 'green', ax=axs[1, 1])                   # virginica
    fig.tight_layout()
    plt.savefig("sepalwidth")


# 5.3 Histograms for Petal Length
def hist_petlen(data, setosa, versicolor, virginica):
    fig, axs = plt.subplots(nrows=2, ncols=2)
    data["Petal Length"].hist(color = 'black', ax=axs[0,0])                         # all data
    setosa["Petal Length"].hist(color = 'red', ax=axs[0, 1])                        # setosa
    versicolor["Petal Length"].hist(color = 'blue', ax=axs[1, 0])                   # versicolor
    virginica["Petal Length"].hist(color = 'green', ax=axs[1, 1])                   # virginica
    fig.tight_layout()
    plt.savefig("petallength")    


# 5.4 Histograms for Petal Width
def hist_petwid(data, setosa, versicolor, virginica):
    fig, axs = plt.subplots(nrows=2, ncols=2)
    data["Petal Width"].hist(color = 'black', ax=axs[0,0])                         # all data
    setosa["Petal Width"].hist(color = 'red', ax=axs[0, 1])                        # setosa
    versicolor["Petal Width"].hist(color = 'blue', ax=axs[1, 0])                   # versicolor
    virginica["Petal Width"].hist(color = 'green', ax=axs[1, 1])                   # virginica
    fig.tight_layout()
    plt.savefig("petalwidth")  



# Sixth step: Define functions to output scatter plots for each pair of variables to png files
# References used: 
    # https://www.w3schools.com/python/pandas/pandas_plotting.asp
    # https://datascienceparichay.com/article/scatter-plot-from-pandas-dataframe/


# 6.1 Scatter plot comparing petal length and width     
def scatter_petlen_petwid(data):
    data['Colour'] = data['Species'].map({'Iris-setosa': 'Red', 'Iris-versicolor': 'Blue', 'Iris-virginica': 'Green'})  # Sets the colour scales for the individual species
    data.plot.scatter(x = "Petal Length", y = "Petal Width", c = "Colour")
    plt.savefig("petlenpetwid")


# 6.2 Scatter plot comparing sepal length and width
def scatter_seplen_sepwid(data):
    data['Colour'] = data['Species'].map({'Iris-setosa': 'Red', 'Iris-versicolor': 'Blue', 'Iris-virginica': 'Green'})  # Sets the colour scales for the individual species
    data.plot.scatter(x = "Sepal Length", y = "Sepal Width", c = "Colour")
    plt.savefig("seplensepwid")


# 6.3 Scatter plot comparing petal length and sepal length
def scatter_petlen_seplen(data):
    data['Colour'] = data['Species'].map({'Iris-setosa': 'Red', 'Iris-versicolor': 'Blue', 'Iris-virginica': 'Green'})  # Sets the colour scales for the individual species
    data.plot.scatter(x = "Petal Length", y = "Sepal Length", c = "Colour")
    plt.savefig("petlenseplen")


# 6.4 Scatter plot comparing petal length and sepal width
def scatter_petlen_sepwid(data):
    data['Colour'] = data['Species'].map({'Iris-setosa': 'Red', 'Iris-versicolor': 'Blue', 'Iris-virginica': 'Green'})  # Sets the colour scales for the individual species
    data.plot.scatter(x = "Petal Length", y = "Sepal Width", c = "Colour")
    plt.savefig("petlensepwid")


# 6.5 Scatter plot comparing petal width and sepal length
def scatter_petwid_seplen(data):
    data['Colour'] = data['Species'].map({'Iris-setosa': 'Red', 'Iris-versicolor': 'Blue', 'Iris-virginica': 'Green'})  # Sets the colour scales for the individual species
    data.plot.scatter(x = "Petal Width", y = "Sepal Length", c = "Colour")
    plt.savefig("petwidseplen")


# 6.6 Scatter plot comparing petal width and sepal width
def scatter_petwid_sepwid(data):
    data['Colour'] = data['Species'].map({'Iris-setosa': 'Red', 'Iris-versicolor': 'Blue', 'Iris-virginica': 'Green'})  # Sets the colour scales for the individual species
    data.plot.scatter(x = "Petal Width", y = "Sepal Width", c = "Colour")
    plt.savefig("petwidsepwid")



# Seventh step: Define the main program function that calls all of the above functions

def main():
    data = read_data()
    print("Please check the associated files for details of the Iris Data Set")
    setosa = filter_setosa(data)
    versicolor = filter_versicolor(data)
    virginica = filter_virginica(data)
    text_overview(data)
    hist_seplen(data, setosa, versicolor, virginica)
    hist_sepwid(data, setosa, versicolor, virginica)
    hist_petlen(data, setosa, versicolor, virginica)
    hist_petwid(data, setosa, versicolor, virginica)
    scatter_petlen_petwid(data)
    scatter_seplen_sepwid(data)
    scatter_petlen_seplen(data)
    scatter_petlen_sepwid(data)
    scatter_petwid_seplen(data)
    scatter_petwid_sepwid(data)
    


# Calls exectution of the main() function

if __name__ == "__main__":
    main()