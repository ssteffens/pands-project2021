# This program analyses the Fisher Iris data set and outputs:
    # A summary of each veriable to a single text file
    # A histogram of each variable to png files
    # A scatter plot of each pair of variables to png files
# Author: Stefanie Steffens 


# Data source: http://archive.ics.uci.edu/ml/machine-learning-databases/iris/, using the "bezdekIris.data" dataset



# Part 1: Import the pandas library to allow accessing the data in the file as a data frame, the matplotlib.pyplot module and the seaborn library to facilitate plotting of data. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 



# Part 2: Define a function which reads in the dataset from the iris.data file. 
# Referenxce for adding headers to the dataset: https://realpython.com/python-csv/

def read_data():
    dataset = pd.read_table("iris.data", sep=",", names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
    return(dataset)



# Part 3: Define functions that enable filtering the data by iris species
# These filter the data set by the three different species and can be used as arguments for the various analysis functions. This avoids repetitively defining filtering variables for each function.
# Reference: https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#where

# 3.1 Filter for setosa species
def filter_setosa(data):                                                    # Reads in the full data set
    setosa = (data[data["Species"] == "Iris-setosa"])                       # Filters the data set by column "Species", value "Iris-setosa"
    return(setosa)                                                          # Returns a setosa-only data set 


# 3.2 Filter for versicolor species
def filter_versicolor(data):                                                # Functionality as explained above for the setosa species
    versicolor = (data[data["Species"] == "Iris-versicolor"]) 
    return(versicolor)


# 3.3 Filter for virginica species                                          # Functionality as explained above for the setosa species
def filter_virginica(data):
    virginica = (data[data["Species"] == "Iris-virginica"])
    return(virginica)



# Part 4: Define a function to output a summary of each variable to a text file.
# Reference: https://izziswift.com/python-pandas-write-content-of-dataframe-into-text-file/

def text_overview(data):
    with open ("datasummary.txt", "wt") as f:                                  
        #info = data.info()                                                        # Data type of columns                                                   
        rows = data.count()[0]                                                      # https://pythonexamples.org/pandas-dataframe-count-rows/ 
        columns = len(list(data))                                                   # https://www.geeksforgeeks.org/count-number-of-columns-of-a-pandas-dataframe/
        describe_all = data.describe()
        transp = describe_all.transpose()                                           # transpose the describe_all table so that it's aligned with the format of the describe tables of the individual species
        describe_seplen = data.groupby('Species')['Sepal Length'].describe()
        describe_sepwid = data.groupby('Species')['Sepal Width'].describe()
        describe_petlen = data.groupby('Species')['Petal Length'].describe()
        describe_petwid = data.groupby('Species')['Petal Width'].describe()

        f.write("OVERVIEW OF IRIS DATASET\n\n")

        f.write("***Sample of Data Set***\n")
        f.write(data.groupby('Species').head(1).to_string())

        f.write("\n\n\n\n***Count of Rows and Columns***\n")
        f.write("Rows: {}, Columns: {}".format(str(rows), (str(columns))))                                      # count of rows and columns

        f.write("\n\n\n\n***Datatype of Columns***\n")
        f.write(data.dtypes.to_string())                                            # https://www.datasciencemadesimple.com/get-data-type-of-column-pandas-python-2/        
                
        f.write("\n\n\n\n***Overview for all Species***\n")
        f.write(transp.to_string())                                                 
                                                                                    # source: https://note.nkmk.me/en/python-pandas-t-transpose/
        f.write("\n\n\n\n***Overview for Sepal Length by Species***\n")
        f.write(describe_seplen.to_string())
        f.write("\n\n\n\n***Overview for Sepal Width by Species***\n")
        f.write(describe_sepwid.to_string())
        f.write("\n\n\n\n***Overview for Petal Length by Species***\n")
        f.write(describe_petlen.to_string())
        f.write("\n\n\n\n***Overview for Petal Width by Species***\n")
        f.write(describe_petwid.to_string())



# Part 5: Define functions to output histograms for each variable to png files
# References used: 
    # For displaying 4 different histograms on one page: https://www.python-graph-gallery.com/25-histogram-with-several-variables-seaborn 
    # https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html#sphx-glr-gallery-statistics-histogram-multihist-py


# 5.1 Histograms for Sepal Length - All data vs species
def hist_seplen(data, setosa, versicolor, virginica):
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize = (7, 7))                     # Defines the overall plot, displaying 4 histograms in 2 rows, 2 columns
    data["Sepal Length"].hist(color = '#9A9CEE', ax=axs[0,0])                       # First histogram containing all data. ax=axs[] defines the position within the overall plot (row 1, column 1)
    axs[0,0].set_title("All Species")                                               # Sets title for first histogram
    setosa["Sepal Length"].hist(color = '#8D66BE', ax=axs[0, 1])                    # Second histogram filtered for setosa
    axs[0,1].set_title("Iris setosa")                                               # Sets title for second histogram
    versicolor["Sepal Length"].hist(color = '#7938C4', ax=axs[1, 0])                # Third histogram filtered for versicolor
    axs[1,0].set_title("Iris versicolor")                                           # Sets title for third histogram
    virginica["Sepal Length"].hist(color = '#8587BE', ax=axs[1, 1])                 # Forth histogram filtered for virginica
    axs[1,1].set_title("Iris virginica")                                            # Sets title for forth histogram
    fig.suptitle("Sepal Length")                                                    # Sets the overall title for the plot
    plt.savefig("sepallength")                                                      # Saves the plot to a png file called "sepallength"


# 5.2 Histograms for Sepal Width
def hist_sepwid(data, setosa, versicolor, virginica):                               # Functionality as explained above for sepal length
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize = (7, 7))
    data["Sepal Width"].hist(color = '#9A9CEE', ax=axs[0,0])
    axs[0,0].set_title("All Species")
    setosa["Sepal Width"].hist(color = '#8D66BE', ax=axs[0, 1])
    axs[0,1].set_title("Iris setosa")
    versicolor["Sepal Width"].hist(color = '#7938C4', ax=axs[1, 0])
    axs[1,0].set_title("Iris versicolor") 
    virginica["Sepal Width"].hist(color = '#8587BE', ax=axs[1, 1])
    axs[1,1].set_title("Iris virginica")  
    fig.suptitle("Sepal Width")
    plt.savefig("sepalwidth")


# 5.3 Histograms for Petal Length
def hist_petlen(data, setosa, versicolor, virginica):                               # Functionality as explained above for sepal length
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize = (7, 7))
    data["Petal Length"].hist(color = '#9A9CEE', ax=axs[0,0])
    axs[0,0].set_title("All Species")
    setosa["Petal Length"].hist(color = '#8D66BE', ax=axs[0, 1])
    axs[0,1].set_title("Iris setosa")
    versicolor["Petal Length"].hist(color = '#7938C4', ax=axs[1, 0])
    axs[1,0].set_title("Iris versicolor") 
    virginica["Petal Length"].hist(color = '#8587BE', ax=axs[1, 1])
    axs[1,1].set_title("Iris virginica")  
    fig.suptitle("Petal Length")
    plt.savefig("petallength")    


# 5.4 Histograms for Petal Width
def hist_petwid(data, setosa, versicolor, virginica):                               # Functionality as explained above for sepal length
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize = (7, 7))
    data["Petal Width"].hist(color = '#9A9CEE', ax=axs[0,0])
    axs[0,0].set_title("All Species")
    setosa["Petal Width"].hist(color = '#8D66BE', ax=axs[0, 1])
    axs[0,1].set_title("Iris setosa")
    versicolor["Petal Width"].hist(color = '#7938C4', ax=axs[1, 0])
    axs[1,0].set_title("Iris versicolor")
    virginica["Petal Width"].hist(color = '#8587BE', ax=axs[1, 1])
    axs[1,1].set_title("Iris virginica")  
    fig.suptitle("Petal Width")
    plt.savefig("petalwidth")  



# Part 6: Define functions to output scatter plots for each pair of variables to png files
# References used: 
    # https://www.w3schools.com/python/pandas/pandas_plotting.asp
    # https://datascienceparichay.com/article/create-scatter-plot-python-matplotlib/
    # https://datascienceparichay.com/article/scatter-plot-from-pandas-dataframe/


# 6.1 Scatter plot comparing petal length and width     
def scatter_petlen_petwid(data):
    sns.lmplot(x = "Petal Length", y = "Petal Width", data=data, markers = ["o", "^", "s"], palette = ["Red", "Blue", "Green"], hue = 'Species', height = 7, aspect = 1, fit_reg=False)
    plt.title("Petal Length vs Petal Width", y = 0.97)                                  # Sets the title of the plot, y indicates the height of the title
    plt.savefig("petlenpetwid")                                                         # Saves the plot to a png file called "petlenpetwid"

  
# 6.2 Scatter plot comparing sepal length and width
def scatter_seplen_sepwid(data):
    sns.lmplot(x = "Sepal Length", y = "Sepal Width", data=data, markers = ["o", "^", "s"], palette = ["Red", "Blue", "Green"], hue = 'Species', height = 7, aspect = 1, fit_reg=False)
    plt.title("Sepal Length vs Sepal Width", y = 0.97) 
    plt.savefig("seplensepwid")


# 6.3 Scatter plot comparing petal length and sepal length
def scatter_petlen_seplen(data):
    sns.lmplot(x = "Petal Length", y = "Sepal Length", data=data, markers = ["o", "^", "s"], palette = ["Red", "Blue", "Green"], hue = 'Species', height = 7, aspect = 1, fit_reg=False)
    plt.title("Petal Length vs Sepal Length", y = 0.97) 
    plt.savefig("petlenseplen")


# 6.4 Scatter plot comparing petal length and sepal width
def scatter_petlen_sepwid(data):
    sns.lmplot(x = "Petal Length", y = "Sepal Width", data=data, markers = ["o", "^", "s"], palette = ["Red", "Blue", "Green"], hue = 'Species', height = 7, aspect = 1, fit_reg=False)
    plt.title("Petal Length vs Sepal Width", y = 0.97) 
    plt.savefig("petlensepwid")


# 6.5 Scatter plot comparing petal width and sepal length
def scatter_petwid_seplen(data):
    sns.lmplot(x = "Petal Width", y = "Sepal Length", data=data, markers = ["o", "^", "s"], palette = ["Red", "Blue", "Green"], hue = 'Species', height = 7, aspect = 1, fit_reg=False)
    plt.title("Petal Width vs Sepal Length", y = 0.97) 
    plt.savefig("petwidseplen")


# 6.6 Scatter plot comparing petal width and sepal width
def scatter_petwid_sepwid(data):
    sns.lmplot(x = "Petal Width", y = "Sepal Width", data=data, markers = ["o", "^", "s"], palette = ["Red", "Blue", "Green"], hue = 'Species', height = 7, aspect = 1, fit_reg=False)
    plt.title("Petal Width vs Sepal Width", y = 0.97) 
    plt.savefig("petwidsepwid")



# Part 7: Define the main program function that calls all of the above functions

def main():
    data = read_data()
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
    print("Please check the associated files for details of the Iris Data Set")
    


# Part 8: Calls exectution of the main() function

if __name__ == "__main__":
    main()