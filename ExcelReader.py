import xlrd;
import re;
from DataReader import DataReader;
from Item import Item;
from ItemGroup import ItemGroup;
from Account import Account;
class ExcelReader(DataReader):
    def AddAccount(self, filePath = ''):
        wb = xlrd.open_workbook(filePath) 
        sheet = wb.sheet_by_index(0)
        for i in range(sheet.nrows):
            self.company.AddAccount(Account(sheet.cell_value(i, 0),
                              sheet.cell_value(i, 1),
                              sheet.cell_value(i, 2),
                              sheet.cell_value(i, 3),
                              sheet.cell_value(i, 4),
                              sheet.cell_value(i, 5),
                              sheet.cell_value(i, 6),
                              sheet.cell_value(i, 7),
                              sheet.cell_value(i, 8),
                              'Sundry Debtors'));
    def AddItemGroup(self, filePath = ''):
        wb = xlrd.open_workbook(filePath) ;
        sheet = wb.sheet_by_index(0);
        for i in range(sheet.nrows):
            self.company.AddItemGroup(ItemGroup(sheet.cell_value(i,0),
                                        "True",
                                        "GST 5%",
                                        "HSN0001"));
        self.company.AddItemGroup(ItemGroup(" ",
                                        "True",
                                        "GST 5%",
                                        "HSN0001"));
    def AddItem(self, filePath = ''):
        wb = xlrd.open_workbook(filePath) ;
        sheet = wb.sheet_by_index(0);
        for i in range(sheet.nrows):
            #name, price, typename, metercount
            name = sheet.cell_value(i, 0);
            price = sheet.cell_value(i, 1);
            parentGroup = sheet.cell_value(i, 2);
            unit = 'Psc.';
            if (sheet.cell_value(i, 3) == 'YES'):
                unit = 'Metre';
            hsnCode = sheet.cell_value(i, 3);
            patStr = "(^5.*5.*)|(^6.*6.*)|(^7.*7.*)";
            p = re.compile(patStr);
            m = p.match(str(name));
            if (parentGroup == ''):
                parentGroup = ' ';
            if (isinstance(m, type(None))):
                self.company.AddItem(Item(name, parentGroup, unit, price, 'True', hsnCode, 'GST 5%', 2.5)); 

        for i in range(100,1000):
            num = i+101;
            string = '5' + str(num) + '5';
            self.company.AddItem(Item(string, ' ', 'Psc.', str(i), 'True', 'HSN52008', 'GST 5%', 2.5)); 