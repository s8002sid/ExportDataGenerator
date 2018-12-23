class Item:
    def __init__(self, name, parentGroup, unit, salePrice, donotMaintainStkBalance, hsnCode, taxCategory, taxRateLocal):
        self.name = name;
        self.parentGroup = parentGroup;
        self.unit = unit;
        self.salePrice = salePrice;
        self.donotMaintainStkBalance = donotMaintainStkBalance;
        self.hsnCode = hsnCode;
        self.taxCategory = taxCategory;
        self.taxRateLocal = taxRateLocal;

