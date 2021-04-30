# This program analyses the Fisher Iris data set and outputs:
    # A summary of each veriable to a single text file
    # A histogram of each variable to png files
    # A scatter plot of each pair of variables to png files
# Author: Stefanie Steffens 



# Data source: http://archive.ics.uci.edu/ml/machine-learning-databases/iris/, using the "bezdekIris.data" dataset. Note that the file has been renamed to "iris.data". 



# Part 1: Import the pandas library to allow accessing the data in the file as a data frame and the matplotlib.pyplot module as well as the seaborn library to facilitate plotting of data. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 



# Part 2: Define a function which reads in the dataset from the iris.data file using the pandas read_table() function. 

def read_data():
    data = pd.read_table("iris.data", sep=",", names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
    return(data)



# Part 3: Define functions that enable filtering the data by iris species
# These filter the data set by the three different species and can be used as arguments for the following analysis functions. This avoids repetitively defining filtering variables for each function.

# 3.1 Filter for setosa species
def filter_setosa(data):                                                            # Reads in the full data set
    setosa = (data[data["Species"] == "Iris-setosa"])                               # Filters the data set by column "Species", value "Iris-setosa"
    return(setosa)                                                                  # Returns a setosa-only data set 


# 3.2 Filter for versicolor species
def filter_versicolor(data):                                                        # Functionality as explained above for the setosa species
    versicolor = (data[data["Species"] == "Iris-versicolor"]) 
    return(versicolor)


# 3.3 Filter for virginica species                                                  # Functionality as explained above for the setosa species
def filter_virginica(data):
    virginica = (data[data["Species"] == "Iris-virginica"])
    return(virginica)



# Part 4: Define a function to output a summary of each variable to a text file.

def text_overview(data):
    with open ("datasummary.txt", "wt") as f:                                       # Defines the file name to be created/updated with the following content
        rows = data.count()[0]                                                      # Counts the rows in the data set
        columns = len(list(data))                                                   # Counts the columns in the data set
        describe_all = data.describe()                                              # Runs the describe() function which returns a statistical summary of the data set
        transp = describe_all.transpose()                                           # Transposes the describe_all table so that it's aligned with the format of the following describe tables of the individual species
        describe_seplen = data.groupby("Species")["Sepal Length"].describe()        # Runs the describe() function for the Sepal Length column and groups the results by Species
        describe_sepwid = data.groupby("Species")["Sepal Width"].describe()         # Runs the describe() function for the Sepal Width column and groups the results by Species
        describe_petlen = data.groupby("Species")["Petal Length"].describe()        # Runs the describe() function for the Petal Length column and groups the results by Species
        describe_petwid = data.groupby("Species")["Petal Width"].describe()         # Runs the describe() function for the Petal Width column and groups the results by Species

        f.write("OVERVIEW OF IRIS DATASET\n\n")                                     # The write() functions outputs text to the defined txt file

        f.write("***Sample of Data Set***\n")
        f.write(data.groupby("Species").head(1).to_string())                        # Prints out a sample of the data set containing one row (spcified by head(1) ) for each Species

        f.write("\n\n\n\n***Count of Rows and Columns***\n")                        
        f.write("Rows: {}, Columns: {}".format(str(rows), (str(columns))))          # Prints out the count of rows and columns

        f.write("\n\n\n\n***Data Type of Columns***\n")
        f.write(data.dtypes.to_string())                                            # Prints out the data type of each column     
                
        f.write("\n\n\n\n***Overview for all Species***\n")
        f.write(transp.to_string())                                                 # Prints out the transposed table returned by the describe() function

        f.write("\n\n\n\n***Overview for Sepal Length by Species***\n")
        f.write(describe_seplen.to_string())                                        # Prints out the result of the describe() function for the Sepal Length column
        f.write("\n\n\n\n***Overview for Sepal Width by Species***\n")
        f.write(describe_sepwid.to_string())                                        # Prints out the result of the describe() function for the Sepal Width column
        f.write("\n\n\n\n***Overview for Petal Length by Species***\n")
        f.write(describe_petlen.to_string())                                        # Prints out the result of the describe() function for the Petal Length column
        f.write("\n\n\n\n***Overview for Petal Width by Species***\n")
        f.write(describe_petwid.to_string())                                        # Prints out the result of the describe() function for the Petal Width column



# Part 5: Define functions to output histograms for each variable to png files

# 5.1 Histograms for Sepal Length - All data vs species
def hist_seplen(data, setosa, versicolor, virginica):
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize = (7, 7))                     # Defines the overall plot, displaying 4 histograms in 2 rows, 2 columns
    data["Sepal Length"].hist(color = "#9A9CEE", ax=axs[0,0])                       # First histogram containing all data. ax=axs[] defines the position within the overall plot (row 1, column 1)
    axs[0,0].set_title("All Species")                                               # Sets title for first histogram
    setosa["Sepal Length"].hist(color = "#8D66BE", ax=axs[0, 1])                    # Second histogram filtered for setosa
    axs[0,1].set_title("Iris setosa")                                               # Sets title for second histogram
    versicolor["Sepal Length"].hist(color = "#7938C4", ax=axs[1, 0])                # Third histogram filtered for versicolor
    axs[1,0].set_title("Iris versicolor")                                           # Sets title for third histogram
    virginica["Sepal Length"].hist(color = "#8587BE", ax=axs[1, 1])                 # Forth histogram filtered for virginica
    axs[1,1].set_title("Iris virginica")                                            # Sets title for forth histogram
    fig.suptitle("Sepal Length")                                                    # Sets the overall title for the plot
    plt.savefig("sepallength")                                                      # Saves the plot to a png file called "sepallength"


# 5.2 Histograms for Sepal Width
def hist_sepwid(data, setosa, versicolor, virginica):                               # Functionality as explained above for sepal length
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize = (7, 7))
    data["Sepal Width"].hist(color = "#9A9CEE", ax=axs[0,0])
    axs[0,0].set_title("All Species")
    setosa["Sepal Width"].hist(color = "#8D66BE", ax=axs[0, 1])
    axs[0,1].set_title("Iris setosa")
    versicolor["Sepal Width"].hist(color = "#7938C4", ax=axs[1, 0])
    axs[1,0].set_title("Iris versicolor") 
    virginica["Sepal Width"].hist(color = "#8587BE", ax=axs[1, 1])
    axs[1,1].set_title("Iris virginica")  
    fig.suptitle("Sepal Width")
    plt.savefig("sepalwidth")


# 5.3 Histograms for Petal Length
def hist_petlen(data, setosa, versicolor, virginica):                               # Functionality as explained above for sepal length
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize = (7, 7))
    data["Petal Length"].hist(color = "#9A9CEE", ax=axs[0,0])
    axs[0,0].set_title("All Species")
    setosa["Petal Length"].hist(color = "#8D66BE", ax=axs[0, 1])
    axs[0,1].set_title("Iris setosa")
    versicolor["Petal Length"].hist(color = "#7938C4", ax=axs[1, 0])
    axs[1,0].set_title("Iris versicolor") 
    virginica["Petal Length"].hist(color = "#8587BE", ax=axs[1, 1])
    axs[1,1].set_title("Iris virginica")  
    fig.suptitle("Petal Length")
    plt.savefig("petallength")    


# 5.4 Histograms for Petal Width
def hist_petwid(data, setosa, versicolor, virginica):                               # Functionality as explained above for sepal length
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize = (7, 7))
    data["Petal Width"].hist(color = "#9A9CEE", ax=axs[0,0])
    axs[0,0].set_title("All Species")
    setosa["Petal Width"].hist(color = "#8D66BE", ax=axs[0, 1])
    axs[0,1].set_title("Iris setosa")
    versicolor["Petal Width"].hist(color = "#7938C4", ax=axs[1, 0])
    axs[1,0].set_title("Iris versicolor")
    virginica["Petal Width"].hist(color = "#8587BE", ax=axs[1, 1])
    axs[1,1].set_title("Iris virginica")  
    fig.suptitle("Petal Width")
    plt.savefig("petalwidth")  



# Part 6: Define functions to output scatter plots for each pair of variables to png files

# 6.1 Scatter plot comparing petal length and width     
def scatter_petlen_petwid(data):
    sns.lmplot(x = "Petal Length", y = "Petal Width", data=data, markers = ["o", "^", "s"], palette = ["Red", "Blue", "Green"], hue = "Species", height = 7, aspect = 1, fit_reg=False)
                                                                                    # Defines the plot by specifying the x and y axes, the data to be used, markers and colours, size and whether to display regression lines
    plt.title("Petal Length vs Petal Width", y = 0.97)                              # Sets the title of the plot, y indicates the height of the title
    plt.savefig("petlenpetwid")                                                     # Saves the plot to a png file called "petlenpetwid"

  
# 6.2 Scatter plot comparing sepal length and width
def scatter_seplen_sepwid(data):                                                    # Functionality as explained above for scatter plot 6.1
    sns.lmplot(x = "Sepal Length", y = "Sepal Width", data=data, markers = ["o", "^", "s"], palette = ["Red", "Blue", "Green"], hue = "Species", height = 7, aspect = 1, fit_reg=False)
    plt.title("Sepal Length vs Sepal Width", y = 0.97) 
    plt.savefig("seplensepwid")


# 6.3 Scatter plot comparing petal length and sepal length
def scatter_petlen_seplen(data):                                                    # Functionality as explained above for scatter plot 6.1
    sns.lmplot(x = "Petal Length", y = "Sepal Length", data=data, markers = ["o", "^", "s"], palette = ["Red", "Blue", "Green"], hue = "Species", height = 7, aspect = 1, fit_reg=False)
    plt.title("Petal Length vs Sepal Length", y = 0.97) 
    plt.savefig("petlenseplen")


# 6.4 Scatter plot comparing petal length and sepal width
def scatter_petlen_sepwid(data):                                                    # Functionality as explained above for scatter plot 6.1
    sns.lmplot(x = "Petal Length", y = "Sepal Width", data=data, markers = ["o", "^", "s"], palette = ["Red", "Blue", "Green"], hue = "Species", height = 7, aspect = 1, fit_reg=False)
    plt.title("Petal Length vs Sepal Width", y = 0.97) 
    plt.savefig("petlensepwid")


# 6.5 Scatter plot comparing petal width and sepal length
def scatter_petwid_seplen(data):                                                    # Functionality as explained above for scatter plot 6.1
    sns.lmplot(x = "Petal Width", y = "Sepal Length", data=data, markers = ["o", "^", "s"], palette = ["Red", "Blue", "Green"], hue = "Species", height = 7, aspect = 1, fit_reg=False)
    plt.title("Petal Width vs Sepal Length", y = 0.97) 
    plt.savefig("petwidseplen")


# 6.6 Scatter plot comparing petal width and sepal width
def scatter_petwid_sepwid(data):                                                    # Functionality as explained above for scatter plot 6.1
    sns.lmplot(x = "Petal Width", y = "Sepal Width", data=data, markers = ["o", "^", "s"], palette = ["Red", "Blue", "Green"], hue = "Species", height = 7, aspect = 1, fit_reg=False)
    plt.title("Petal Width vs Sepal Width", y = 0.97) 
    plt.savefig("petwidsepwid")



# Part 7: Define the main program function that calls all of the above functions

def main():
    data = read_data()                                                              # Sets the data argument by calling the read_data() function which reads in the data set from the source file
    setosa = filter_setosa(data)                                                    # Sets the setosa filter argument as returned by the filter_setosa() function
    versicolor = filter_versicolor(data)                                            # Sets the versicolor filter argument as returned by the filter_versicolor() function
    virginica = filter_virginica(data)                                              # Sets the virginica filter argument as returned by the filter_virginica() function
    text_overview(data)                                                             # Calls the function to create the datasummary.txt file
    hist_seplen(data, setosa, versicolor, virginica)                                # Calls the function to create the set of histograms for the Sepal Length attribute 
    hist_sepwid(data, setosa, versicolor, virginica)                                # Calls the function to create the set of histograms for the Sepal Width attribute
    hist_petlen(data, setosa, versicolor, virginica)                                # Calls the function to create the set of histograms for the Petal Length attribute
    hist_petwid(data, setosa, versicolor, virginica)                                # Calls the function to create the set of histograms for the Petal Width attribute
    scatter_petlen_petwid(data)                                                     # Calls the functions to create the Petal Length vs Petal Width scatter plot
    scatter_seplen_sepwid(data)                                                     # Calls the functions to create the Sepal Length vs Sepal Width scatter plot
    scatter_petlen_seplen(data)                                                     # Calls the functions to create the Petal Length vs Sepal Length scatter plot
    scatter_petlen_sepwid(data)                                                     # Calls the functions to create the Petal Length vs Sepal Width scatter plot
    scatter_petwid_seplen(data)                                                     # Calls the functions to create the Petal Width vs Sepal Lengths scatter plot
    scatter_petwid_sepwid(data)                                                     # Calls the functions to create the Petal Width vs Sepal Width scatter plot
    print("Please check the associated files for details of the Iris Data Set")     # Prints out advice for a potential user of the program to check the files created 
    


# Part 8: Calls execution of the main() function

if __name__ == "__main__":
    main()