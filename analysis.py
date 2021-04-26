# This program analyses the Fisher Iris data set and outputs:
    # A summary of each veriable to a single text file
    # A histogram of each variable to png files
    # A scatter plot of each pair of variables to png files
# Author: Stefanie Steffens 

# Resources: http://archive.ics.uci.edu/ml/machine-learning-databases/iris/ using the "bezdekIris.data" dataset


# Import pandas library to allow accessing the data in the file as a data frame
# Import matplotlib.pyplot to facilitate plotting of data
import pandas as pd
import matplotlib.pyplot as plt


# First step: Define a function which reads in the data set from the iris.data file. 
# https://realpython.com/python-csv/ to add headers

def read_data():
    dataset = pd.read_table("iris.data", sep=",", names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
    #print(dataset)
    #print(dataset.head(2))                                         # Remove, for checking top 2 rows of data
    #print(dataset[["Sepal Length", "Sepal Width"]].head(2))        # Remove, for checking values by column
    #print(dataset.info())                                          # Remove, shows data type of columns
    #print(dataset.describe())                                      # Remove, calculates count, mean, min, max values, median (quartiles) for each columnn
    return(dataset)


# Filtering data by species
# https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#where
def filter_setosa(data):
    setosa = (data[data["Species"] == "Iris-setosa"])
    return(setosa)


def filter_versicolor(data):
    versicolor = (data[data["Species"] == "Iris-versicolor"]) 
    return(versicolor)


def filter_virginica(data):
    virginica = (data[data["Species"] == "Iris-virginica"])
    return(virginica)


# Plot (scatter), comparing petal length and width
def plot_data(data):
    print("plot!")
    data.plot(kind = "scatter", x = "Petal Length", y = "Petal Width")              # https://www.w3schools.com/python/pandas/pandas_plotting.asp
    plt.show()


# Output to text file:                                                              https://izziswift.com/python-pandas-write-content-of-dataframe-into-text-file/
def text_output(data):
    with open ("output.txt", "wt") as f:
        f.write(data.to_string())


# Output to text file for "Setosa"
def text_setosa(setosa):
    with open ("setosa.txt", "wt") as f:
        #f.write(setosa.to_string())
        describe = setosa.describe()
        f.write(describe.to_string())


# Output to text file:                                                              https://izziswift.com/python-pandas-write-content-of-dataframe-into-text-file/
def text_overview(data):
    with open ("datasummary.txt", "wt") as f:
        describe_all = data.describe()
        transp = describe_all.transpose()
        describe_seplen = data.groupby('Species')['Sepal Length'].describe()
        describe_sepwid = data.groupby('Species')['Sepal Width'].describe()
        describe_petlen = data.groupby('Species')['Petal Length'].describe()
        describe_petwid = data.groupby('Species')['Petal Width'].describe()

        f.write("OVERVIEW OF IRIS DATASET\n\n")
        f.write("Overview for all Species\n")
        f.write(transp.to_string())                                                 # transpose the describe table so that it's aligned with the below format
                                                                                    # source: https://note.nkmk.me/en/python-pandas-t-transpose/
        f.write("\n\n\n\n Overview for Sepal Length by Species\n")
        f.write(describe_seplen.to_string())
        f.write("\n\n\n\n Overview for Sepal Width by Species\n")
        f.write(describe_sepwid.to_string())
        f.write("\n\n\n\n Overview for Petal Length by Species\n")
        f.write(describe_petlen.to_string())
        f.write("\n\n\n\n Overview for Petal Width by Species\n")
        f.write(describe_petwid.to_string())


def histo_all(data):
    data.hist()
    plt.show()

        

# Main program: 

def main():
    data = read_data()
    #print(data)
    text_output(data)
    text_overview(data)
    plot_data(data)
    setosa = filter_setosa(data)
    versicolor = filter_versicolor(data)
    virginica = filter_virginica(data)
    print(virginica)
    histo_all(data)
    
    
    text_setosa(setosa)


if __name__ == "__main__":
    main()