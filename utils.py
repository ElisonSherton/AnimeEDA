import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import numpy as np

class Utils:
    @classmethod
    def annotate(self, ax, title, xax, yax, fs = 16):
        ax.set_title(title, fontsize = fs)
        ax.set_xlabel(xax, fontsize = fs - 2)
        ax.set_ylabel(yax, fontsize = fs - 2)
        
    @classmethod
    def histogram(self, df, colname, bins = None):
        # Create an axis object using subplots from matplotlib
        fig, ax = plt.subplots(1, 1 ,figsize = (20, 6))
        
        # Plot a histogram of the column from the dataframe mentioned
        if bins:
            sns.distplot(df[colname], ax = ax, bins = bins)
        else:
            sns.distplot(df[colname], ax = ax)
        
        # Set the title of the plot
        title = f"Histogram of {colname} feature."
        xax   = f"{colname.title()} values."
        yax   = f"Frequency of occurence"
        self.annotate(ax, title, xax, yax)
        
        # Save the plot to an image
        plt.savefig(f"./img/Histogram_{colname.title()}.png")
        plt.close()
    
    @classmethod
    def genre_countplot(self, df, colname):
        # Process the genre column to split on comma and append resulting
        # genres all to a single list
        all_genres = []
        for item in df[colname]:
            item = item.strip()
            all_genres.extend(item.split(', '))
        
        # Count the number of items in the genre and create a dataframe
        c = Counter(all_genres)
        
        # Plot the genres and their count respectively
        fig, ax = plt.subplots(1, 1, figsize = (20, 6))
        sns.countplot(all_genres)
        
        # Set the axes and title of the plot
        title = f"Countplot of {colname} feature"
        xax   = f"{colname}"
        yax   = f"Counts/ Occurrences"
        self.annotate(ax, title, xax, yax)
        plt.xticks(rotation = 45)
        plt.tight_layout()
        
        # Save the plot to an image
        plt.savefig(f"./img/Countplot_{colname.title()}.png")
        plt.close()
    
    @classmethod
    def barplot(self, df, xcolname, ycolname):
        # Create an axis object in which to place our barchart
        fig, ax = plt.subplots(1, 1, figsize = (15, 8))
        
        # Plot the barchart
        sns.barplot(x = xcolname, y = ycolname, data = df, ax = ax)
        
        # Set the axes and title of the plot
        title = f"Barchart of {xcolname.title()} vs {ycolname.title()}"
        xax   = xcolname.title()
        yax   = ycolname.title()
        self.annotate(ax, title, xax, yax)
        plt.tight_layout()
        
        # Save the plot to an image
        plt.savefig(f"./img/Barplot_{xcolname.title()}_vs{ycolname.title()}")
        plt.close()
    
    @classmethod
    def pieplot(self, data, colname):
        # Create an axis object
        fig, ax = plt.subplots(1, 1, figsize = (15, 8))
        
        # Get the data in the right format
        labels = list(data.keys())
        sizes  = list(data.values())
        
        # Plot the pie chart
        ax.pie(sizes, labels = labels, shadow = False, startangle = 0, autopct = "%1.2f%%")
        ax.axis('equal')
        ax.set_title(f"Pie chart for {colname} feature.")
        
        # Save the plot to an image
        plt.savefig(f"./img/Pieplot_{colname.title()}")
        plt.close()
    
    @classmethod
    def boxplot(self, data, xcolname, ycolname, ax, log=False):
        # Create a copy of the data to work with
        df = data.copy()
        
        # Check on the log condition
        name = None
        if log:
            name = f'Log_{ycolname}'
            df[name] = np.log(df[ycolname])
            sns.boxplot(y = name, x = xcolname, data = df, ax = ax)
        else:
            name = ycolname
            sns.boxplot(y = name, x = xcolname, data = df, ax = ax)
        
        # Set the title and axes names
        title = f"Box plot of {name.title()} wrt {xcolname.title()}"
        xax   = xcolname.title()
        yax   = ycolname.title()
        self.annotate(ax, title, xax, yax)
    
    @classmethod
    def violinplot(self, data, xcolname, ycolname, ax, log=False):
        # Create a copy of the data to work with
        df = data.copy()
        
        # Check on the log condition
        name = None
        if log:
            name = f'Log_{ycolname}'
            df[name] = np.log(df[ycolname])
            sns.violinplot(y = name, x = xcolname, data = df, ax = ax)
        else:
            name = ycolname
            sns.violinplot(y = name, x = xcolname, data = df, ax = ax)
        
        # Set the title and axes names
        title = f"Violin plot of {name.title()} wrt {xcolname.title()}"
        xax   = xcolname.title()
        yax   = ycolname.title()
        self.annotate(ax, title, xax, yax)
    
    @classmethod
    def scatterplot(self, data, xcolname, ycolname):
        # Create an axis object to plot on
        fig, ax = plt.subplots(1, 1, figsize = (15, 8))
        
        # Plot the scatterplot
        sns.regplot(x = xcolname, y = ycolname, ax = ax, data = data)
        
        # Set the title and axes names
        title = f"Scatterplot of {ycolname.title()} vs {xcolname.title()}"
        xax   = xcolname.title()
        yax   = ycolname.title()
        self.annotate(ax, title, xax, yax)
        
        # Save the plot to an image
        plt.savefig(f"./img/Scatter_{yax}_vs{xax}")
        plt.close()
    
    @classmethod
    def heatmap(self, data, xcolname, ycolname, cmap = 'YlGnBu', quantity = "occurrences"):
        # Create an axis object to plot on
        fig, ax = plt.subplots(1, 1, figsize = (20, 15))
        
        # Plot the heatmap
        sns.heatmap(data, ax = ax, annot = True, cmap = cmap, fmt=".2f", linewidth=0.3)
        
        # Set the title and name the axes
        title = f"Heatmap describing {quantity}: {ycolname.title()} vs {xcolname.title()}"
        xax   = xcolname.title()
        yax   = ycolname.title()
        self.annotate(ax, title, xax, yax)
        
        plt.tight_layout()
        
        # Save the plot to an image
        plt.savefig(f"./img/Heatmap_of_{quantity}_{ycolname}_{xcolname}")
        plt.close()