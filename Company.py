from Account import Account;
from ItemGroup import ItemGroup;
from Item import Item;
class Company:
    def __init__(self):
        self.accounts = [];
        self.itemGroups = [];
        self.items = [];
    def AddAccount(self, account):
        self.accounts.append(account);
    def AddItemGroup(self, itemGroup):
        self.itemGroups.append(itemGroup);
    def AddItem(self, item):
        self.items.append(item);