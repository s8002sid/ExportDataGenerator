from DataReader import DataReader;
from Item import Item;
from ItemGroup import ItemGroup;
from Account import Account;
import pyodbc;
import xlrd;
from Company import Company;
class ItemGroupSetting:
    def __init__(self):
        self.name = '';
        self.completeDel = False;
        self.merge = False;
        self.startPrice = 0;
        self.endPrice = 0;
        self.mergeTo = '';
        self.unit = 'Psc.'
        self.incrementByPoint5 = False;
        self.priceRangeSet = True;
class SQLReader(DataReader):
    def __init__(self, itemTypeFileName):
        self.connStr = r"DRIVER=SQL Server;SERVER=.\SQLEXPRESS;DATABASE=vardhman";
        wb = xlrd.open_workbook(itemTypeFileName) 
        sheet = wb.sheet_by_index(0);
        self.company = Company();
        self.itemGroupSettings = {};
        for i in range(sheet.nrows):
            setting = ItemGroupSetting();
            setting.name = sheet.cell_value(i,0);
            if sheet.cell_value(i,1) == 'compdel':
                setting.completeDel = True;
                setting.priceRangeSet = False;
            elif sheet.cell_value(i,1) == 'merge':
                setting.merge = True;
                setting.priceRangeSet = False;
            setting.mergeTo = sheet.cell_value(i,2);
            setting.startPrice = sheet.cell_value(i,3);
            setting.endPrice = sheet.cell_value(i,4);
            if type(sheet.cell_value(i,5)) == type(0):
                setting.incrementByPoint5 = True;
            if sheet.cell_value(i,6) == '':
                setting.unit = 'Psc.'
            else:
                setting.unit = sheet.cell_value(i,6);
            self.itemGroupSettings[setting.name] = setting;

    def isNumber(self, value):
        if (type(value) == type(0) or type(value) == type(0.0)):
            return True;
        return False;
    def codeGenerator (self, value, code):
        retVal = '';
        if value-int(value) == 0.5:
            retVal = code + str(int(value))+'50' + code;
        else:
            retVal = code + str(value) + code;
        return retVal;
    def AddAccount(self, filePath = ''):
        con = pyodbc.connect(self.connStr);
        cursor = con.cursor();
        cursor.execute("""select l.name as name, sum(payment)-sum(recepit) as balance, n, c, note, 
        address, pincode, phno_1, phno_2 from ledger_showall l left outer join customer c 
        on l.n = c.name and l.c = c.city where l.name not in ('DEMO DEMO', 'CGST', 'SGST', 'VAT')
        group by n,c,note, address, pincode, phno_1, phno_2, l.name having sum(payment)-sum(recepit) > 0 
        order by l.name""");
        while(True):
            row = cursor.fetchone();
            if (row == None):
                break;
            self.company.AddAccount(Account(
                row[0], row[1], row[2], row[3],
                row[4], row[5], row[6], row[7],
                row[8], 'Sundry Debtors'));
        cursor.close();

    def AddItemGroup(self, filePath = ''):
        con = pyodbc.connect(self.connStr);
        cursor = con.cursor();
        cursor.execute("select typename from itemtype where typename not like('')");
        while(True):
            row = cursor.fetchone();
            if (row == None):
                break;
            add = True;
            name = row[0];
            if (self.itemGroupSettings.has_key(name)):
                setting = self.itemGroupSettings[name];
                if (setting.completeDel or setting.merge):
                    add = False;
            if (add == True):
                self.company.AddItemGroup(ItemGroup(row[0], "True", "GST 5%", "HSN0001"));
        self.company.AddItemGroup(ItemGroup(" ",
                                        "True",
                                        "GST 5%",
                                        "HSN0001"));
        con.close();
        
    def AddItem(self, filePath = ''):
        con = pyodbc.connect(self.connStr);
        cursor = con.cursor();
        cursor.execute("""select name, typename, price, metercount, hsnCode from item i 
        inner join itemtype it on i.itemtype_id = it.id where name not like ('5%5') and 
        name not like ('6%6') and name not like ('7%7')""");

        while(True):
            row = cursor.fetchone();
            if (row == None):
                break;
            meterCount = row[3];
            unit = 'Psc.'
            if (type(meterCount) == type('') and meterCount.lower() == 'yes'):
                unit = 'Metre';
            add = True;
            itemType = row[1];
            if self.itemGroupSettings.has_key(itemType):
                setting = self.itemGroupSettings[itemType];
                if (setting.completeDel):
                    add = False;
                if (setting.merge):
                    itemType = setting.mergeTo;
                if (setting.unit == "Metre"):
                    unit = "Metre";
            #self.company.AddItem(Item(row[0], row[1], unit, row[2], "True", row[4], 'GST 5%', 2.5));
        con.close();

        for e in self.itemGroupSettings.keys():
            setting = self.itemGroupSettings[e];
            unit = 'Psc.'
            if (setting.unit == 'Metre'):
                unit = 'Metre';
            if (setting.completeDel or setting.merge):
                continue;
            if (self.isNumber(setting.startPrice) and self.isNumber(setting.endPrice)):
                startPrice = setting.startPrice;
                if (setting.incrementByPoint5  and setting.startPrice < 25):
                    for i in range(startPrice*10, setting.endPrice*10, 5):
                        val = i/10.0;
                        code = self.codeGenerator(val, '7')
                        self.company.AddItem(Item(code, setting.name, unit, val, "True", '', 'GST 5%', 2.5));
                        #code = self.codeGenerator(val, '6')
                        #self.company.AddItem(Item(code, setting.name, unit, val, "True", '', 'GST 5%', 2.5));
                    startPrice = 26;
                if (startPrice < setting.endPrice):
                    for i in range(int(startPrice), int(setting.endPrice)):
                        code = self.codeGenerator(i, '7');
                        self.company.AddItem(Item(code, setting.name, unit, i, "True", '', 'GST 5%', 2.5));
                        #code = self.codeGenerator(i, '6');
                        #self.company.AddItem(Item(code, setting.name, unit, i, "True", '', 'GST 5%', 2.5));
                if (startPrice == setting.endPrice):
                    code = self.codeGenerator(startPrice, '7');
                    self.company.AddItem(Item(code, setting.name, unit, startPrice, "True", '', 'GST 5%', 2.5));
                    #code = self.codeGenerator(startPrice, '6');
                    #self.company.AddItem(Item(code, setting.name, unit, startPrice, "True", '', 'GST 5%', 2.5));