import pandas as pd
import matplotlib.pyplot as plt



class CompanySales:
    def __init__(self, CompanyName="", CompanyAddress="", FiletoRead=""):
        self.CompanyName = CompanyName
        self.CompanyAdress = CompanyAddress
        self.FiletoRead = FiletoRead
        self.salesdata = pd.read_csv(FiletoRead)
        print(self.salesdata)
    def setName(self, newname):
        self.CompanyName = newname
    def setAddr(self, newaddr):
        self.CompanyAdress = newaddr
    def getName(self):
        return self.CompanyName
    def getAddr(self):
        return self.CompanyAdress
    def filterData(self,col_names):
        self.col_names = col_names
        self.filter_data = self.salesdata[col_names]
        return self.filter_data
    def Stats(self,filterDF,colmname):
        self.filterDF = filterDF
        self.colmname = colmname
        self.newsubDF = self.filterDF[colmname]
        print(self.newsubDF)
        print("Max: ", self.newsubDF.max())
        print("Min: ", self.newsubDF.min())
        print("Average: ", self.newsubDF.mean())
    def lineGraph(self, colmname1, yaxis):
        #retrive colmname and yaxis and plot both according to number of items in category
        self.colmname1 = colmname1
        self.yaxislabel = yaxis
        #self.datatograph = self.salesdata[colmname1]
        # sorted alphabetically
        self.sorted_data = self.filter_data.groupby(colmname1)
        self.sumofgroup = self.sorted_data.sum()
        print (self.sorted_data.size())
        print (self.sumofgroup)
        self.sumofgroup.plot(kind="line")
        plt.show()
    def barPlot(self, colmname2):
        self.colmname2 = colmname2
        #self.datatograph = self.salesdata[colmname1]
        # sorted alphabetically
        self.sorted_data1 = self.filter_data.groupby(colmname2)
        self.sumofgroup1 = self.sorted_data1.sum()
        self.sumofgroup1.plot(kind="bar")
        plt.show()
    def __str__(self):
        # Retrieve name and address and display nicely 
        self.str_name = Sales.getName()
        self.str_addr = Sales.getAddr()
        return ("Company Names: " + Sales.getName() + "\n" + "Company Sales: " + Sales.getAddr() + "\n" + "Sales Data:")

if __name__=='__main__':  
    Sales = CompanySales("ABC","3 River St. N.Y.,N.Y.", "CompanySalesData.csv")
    # the above statement is assuming that the init method receives the company name, 
    # the company address and the name of the file in that order.
    # It creates a CompanySales object and calls the 
    #   constructor ; all the code that is in the constructor is executed
    # the name of the CompanySales object is Sales so now in the unit test we will use 
    # that object name to test the rest of the functionality of our class
    
    Sales.setName("Dallas Store") #change the Company name of the Sales object
    Sales.setAddr("2929 First St., Dallas,Tx.") #change the Company address
    print ("Company Name was changed to")
    print (Sales.getName()) #did the change take place?/does the getName work?
    print ("Company Address was changed to")
    print (Sales.getAddr())#did the change take place?/does the getAddr method work
    # add lines here that test your Data Analysis methods
    print(Sales) # calls the __str__ method of the CompanySales class and returns a
                        # string to the print statement
    #test filterdata
    columnnamelist = ['Quantity', 'Category']
    print(Sales.filterData(columnnamelist))
    post_filterdata = Sales.filterData(columnnamelist)
    #filterdata works
#NOTE: YOU MUST PASS BOTH FILTERDATA AND STATS THE SAME VALUE FOR THE COLMN
    #test stats NOTE: PASS STATS NUMERICAL DATA FOR CORRECT RESULTS

    Sales.Stats(post_filterdata, "Quantity")
    #stats works
    
    #test lineGraph
    Sales.lineGraph("Category", "Quantity")

    Sales.barPlot("Category")
    
