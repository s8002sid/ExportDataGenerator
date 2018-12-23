from Company import Company;
from XMLGenerator import GenerateXML;
from Account import Account;
import pyodbc;
from DataReader import DataReader;
from ExcelReader import ExcelReader;
host='127.0.0.1';

#con = pyodbc.connect(r"DRIVER=SQL Server;SERVER=SIDDJAIN-WX-5\SQLEXPRESS;DATABASE=vardhman")
#cursor = con.cursor();
#cursor.execute("select l.name as name, sum(payment)-sum(recepit) as balance, n, c, note, address, pincode, phno_1, phno_2 from ledger_showall l left outer join customer c on l.n = c.name and l.c = c.city \
#where l.name not in ('DEMO DEMO', 'CGST', 'SGST', 'VAT')");
accountsFilePath = r'C:\Temp\busy\customerData.xls';
itemGroupFilePath = r'C:\Temp\busy\itemGroup.xls';
itemFilePath = r'C:\Temp\busy\items.xls';
excelReader = ExcelReader();
#company.AddAccountFromExcel(accountsFilePath);
#company.AddItemGroupFromExcel(itemGroupFilePath);
excelReader.AddItem(itemFilePath);
string = GenerateXML(excelReader.company, r'C:\Temp\busy\customerData1.dat');
