class Product:
    def __init__(self):
        # private members that won't be accessed directly during instantiation
        self.__ProductID = ""
        self.__ProductName = ""
        self.__Price = ""

    def setProduct(self, pid, pname, price):
        self.__ProductID = pid
        self.__ProductName = pname
        self.__Price = price

    # Product members can only be changed via methods
    def updateProduct(self, newPrice):
        self.__Price = newPrice

    def showProduct(self):
        print(
            " Product ID: {}\n Product Name: {} \n Price: {}".format(
                self.__ProductID, self.__ProductName, self.__Price
            )
        )


tv = Product()
tv.setProduct("TV1", "LG Golden", 1850)
tv.showProduct()
tv.updateProduct(800)
tv.showProduct()
