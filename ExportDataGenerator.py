from Company import Company;
from XMLGenerator import GenerateXML;
from XMLGenerator import GenerateChunkedXML;
from Account import Account;
import pyodbc;
from DataReader import DataReader;
from ExcelReader import ExcelReader;
from SQLReader import SQLReader;
from ExcelGenerator import GenerateChunkedExcel;
from ExcelGenerator import GenerateExcel;
host='127.0.0.1';

#con = pyodbc.connect(r"DRIVER=SQL Server;SERVER=SIDDJAIN-WX-5\SQLEXPRESS;DATABASE=vardhman")
#cursor = con.cursor();
#cursor.execute("select l.name as name, sum(payment)-sum(recepit) as balance, n, c, note, address, pincode, phno_1, phno_2 from ledger_showall l left outer join customer c on l.n = c.name and l.c = c.city \
#where l.name not in ('DEMO DEMO', 'CGST', 'SGST', 'VAT')");
accountsFilePath = r'C:\Temp\busy\customerData.xls';
itemGroupFilePath = r'C:\Temp\busy\itemGroup.xls';
itemFilePath = r'C:\Temp\busy\items.xls';
#reader = ExcelReader();
reader = SQLReader(r'C:\Temp\busy\itemType.xls');
#company.AddAccountFromExcel(accountsFilePath);
#company.AddItemGroupFromExcel(itemGroupFilePath);
reader.AddAccount(accountsFilePath);
reader.AddItemGroup(itemGroupFilePath);
reader.AddItem(itemFilePath);
#string = GenerateXML(reader.company, r'C:\Temp\busy\customerData1.dat');
#GenerateChunkedXML(reader.company, r'C:\Temp\busy\VT')
GenerateChunkedExcel(reader.company, r'C:\Temp\busy\VT')