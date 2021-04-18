# This program analyses the Fisher Iris data set and outputs:
    # A summary of each veriable to a single text file
    # A histogram of each variable to png files
    # A scatter plot of each pair of variables to png files
# Author: Stefanie Steffens 

# Resources: http://archive.ics.uci.edu/ml/machine-learning-databases/iris/ using the "bezdekIris.data" dataset


# Import pandas library to allow accessing the data in the file as a data frame

import pandas as pd


# First step: Define a function which reads in the data set 
# https://realpython.com/python-csv/ to add headers

def read_data():
    dataset = pd.read_table("iris.data", sep=",", names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
    #print(dataset)
    #print(dataset.head(2))                                         # Remove, for checking top 2 rows of data
    #print(dataset[["Sepal Length", "Sepal Width"]].head(2))        # Remove, for checking values by column
    #print(dataset.info())                                          # Remove, shows data type of columns
    #print(dataset.describe())                                      # Remove, calculates count, mean, min, max values, median (quartiles) for each columnn
    return(dataset)


# Main program: 

def main():
    data = read_data()
    print(data)


if __name__ == "__main__":
    main()