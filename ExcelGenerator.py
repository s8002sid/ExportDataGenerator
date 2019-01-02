import xlrd;
import xlwt;
from Company import Company;
from Item import Item;
from ItemGroup import ItemGroup;
def GenerateChunkedExcel(company, fileName):
    workbook = xlwt.Workbook(encoding = 'ascii');
    tmpCompany = Company();
    #if (len(company.accounts) > 0):
    #    tmpCompany.accounts = company.accounts;
    #    tmpFileName = fileName + '_accounts.xls';
    #    GenerateExcel(workbook, tmpCompany, tmpFileName);
    #    tmpCompany.accounts = [];
    if (len(company.itemGroups) > 0):
        tmpCompany.itemGroups = company.itemGroups;
        tmpFileName = '_sheet'
        GenerateExcel(workbook, tmpCompany, tmpFileName);
        tmpCompany.itemGroups = [];
    j = 1;
    if (len(company.items) > 0):
        start = 0;
        while(True):
            end = start + 10000;
            if (end > len(company.items)):
                end = len(company.items);
            for i in range(start, end):
                tmpCompany.AddItem(company.items[i]);
            start = end;
            tmpFileName = 'sheet_' + str(j);
            GenerateExcel(workbook, tmpCompany, tmpFileName);
            if (start == len(company.items)):
                break;
            tmpCompany.items = [];
            j+=1;
    workbook.save(fileName + 'data_2.xls');
def GenerateExcel(workbook, company, sheetName):
    itemGroups = company.itemGroups;
    items = company.items;
    if (len(itemGroups) > 0):
        sheet = workbook.add_sheet('ItemGroup_' + sheetName);
        itemGroups = company.itemGroups;
        items = company.items;
        for i in range(len(itemGroups)):
            sheet.write(i, 0, label = itemGroups[i].name);
            sheet.write(i, 1, label = itemGroups[i].primaryGroup);
            sheet.write(i, 2, label = itemGroups[i].taxCatName);
            sheet.write(i, 3, label = itemGroups[i].hsnCode);
    sheet = workbook.add_sheet('Item_' + sheetName);
    for i in range(len(items)):
        if (items[i].parentGroup.lower() == 'general'):
            continue;
        if (items[i].parentGroup.lower().strip() == ''):
            continue;
        sheet.write(i, 0, label = items[i].parentGroup + ' ' + items[i].name);
        sheet.write(i, 2, label = items[i].parentGroup);
        sheet.write(i, 3, label = items[i].unit);
        sheet.write(i, 5, label = items[i].salePrice);
        sheet.write(i, 6, label = items[i].taxCategory);
        sheet.write(i, 7, label = items[i].taxRateLocal);