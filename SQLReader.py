from DataReader import DataReader;
from Item import Item;
from ItemGroup import ItemGroup;
from Account import Account;
import pyodbc;

class SQLReader(DataReader):
    def __init__(self):
        self.con = pyodbc.connect(r"DRIVER=SQL Server;SERVER=SIDDJAIN-WX-5\SQLEXPRESS;DATABASE=vardhman");
    def AddAccount(self, filePath = ''):
        print "Future"