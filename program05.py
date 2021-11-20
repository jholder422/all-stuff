from CompanySales import CompanySales
if __name__== '__main__':
    menuselection = input("Menu:", "\n", "filterData function: 1", "\n", "Stats function : 2", "\n", "lineGraph function: 3", "\n", "barPlot function: 4", "\n", "Quit Menu: 5")
    Sales = CompanySales()
    colmnlist = []
    while menuselection != "5":
        #filterdata
        if menuselection == 1:
            for i in range(2):
                colmnlist.append(input("input two columns to be chosen for data analysis"))
            postfilterdata =Sales.filterData(colmnlist)
        
        
    #stats
        if menuselection == 2:
            colmname_of_filterdata = input("Enter column to be passed to Stats method")
            Sales.Stats(postfilterdata,colmname_of_filterdata )


    #linegraph
        if menuselection == 3:
            colmnname_for_linegraph = input("Enter column name to send to line graph")
            Sales.lineGraph(colmnname_for_linegraph, colmname_of_filterdata )
    #barplot
        if menuselection == 4:
            colmname_for_bargraph = input("Enter column name to send to barplot")
            Sales.barPlot(colmname_for_bargraph)
    
