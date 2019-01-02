from Company import Company;
import xml.etree.cElementTree as ET;

def AddMasterDet(etMasterSummary, type, len):
    etMasterDet = ET.SubElement(etMasterSummary, "MastersDet");
    ET.SubElement(etMasterDet, "MasterType").text = type;
    ET.SubElement(etMasterDet, "NoOfMasters").text = str(len);

def GenerateChunkedXML(company, fileName):
    tmpCompany = Company();
    if (len(company.accounts) > 0):
        tmpCompany.accounts = company.accounts;
        tmpFileName = fileName + '_accounts.xml';
        GenerateXML(tmpCompany, tmpFileName);
        tmpCompany.accounts = [];
    if (len(company.itemGroups) > 0):
        tmpCompany.itemGroups = company.itemGroups;
        tmpFileName = fileName + '_itemGroups.xml'
        GenerateXML(tmpCompany, tmpFileName);
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
            tmpFileName = fileName + '_item' + '_' + str(j) +'.xml';
            GenerateXML(tmpCompany, tmpFileName);
            if (start == len(company.items)):
                break;
            tmpCompany.items = [];
            j+=1;

def GenerateXML(company, fileName):
    accounts = company.accounts;
    itemGroups = company.itemGroups;
    items = company.items;

    etRoot = ET.Element("BusyData", FinYear='01-04-2018');
    if (len(accounts) > 0):
        etAccounts = ET.SubElement(etRoot, "Accounts");
        for i in range(len(accounts)):
            etAccount = ET.SubElement(etAccounts, "Account");
            ET.SubElement(etAccount, "Name").text = str(accounts[i].nameAndCity);
            ET.SubElement(etAccount, "PrintName").text = str(accounts[i].nameAndCity);
            ET.SubElement(etAccount, "ParentGroup").text = "Sundry Debtors";
            ET.SubElement(etAccount, "OPBal").text = str(accounts[i].openBal);
            ET.SubElement(etAccount, "PYBal").text = str(accounts[i].openBal);
            ET.SubElement(etAccount, "BillByBillBalancing").text = "True";

            #Address
            etAddress = ET.SubElement(etAccount, "Address");
            ET.SubElement(etAddress, "Address1").text = str(accounts[i].extraInfo);
            ET.SubElement(etAddress, "Address2").text = str(accounts[i].address);
            ET.SubElement(etAddress, "Address4").text = str(accounts[i].city);
            ET.SubElement(etAddress, "TelNo").text = str(accounts[i].phno_1);
            ET.SubElement(etAddress, "Contact").text = str(accounts[i].phno_2);
            ET.SubElement(etAddress, "CountryName").text = "India";
            ET.SubElement(etAddress, "StateName").text = "Chhattisgarh";
            ET.SubElement(etAddress, "CityName").text = str(accounts[i].city);
            ET.SubElement(etAddress, "AreaName").text = "";
            
            ET.SubElement(etAccount, "SupplierType").text = "1";
            ET.SubElement(etAccount, "PriceLevel").text = "@";
            ET.SubElement(etAccount, "PriceLevelForPurc").text = "@";
            ET.SubElement(etAccount, "TaxType").text = "Others";
            ET.SubElement(etAccount, "TypeOfDealerGST").text = "Un-Registered";
            ET.SubElement(etAccount, "ReverseChargeType").text = "Not Applicable";
            ET.SubElement(etAccount, "InputType").text = "None";
    if (len(itemGroups) > 0):
        etItemGroups = ET.SubElement(etRoot, "ItemGroups");
        for i in range(len(itemGroups)):
            etItemGroup = ET.SubElement(etItemGroups, "ItemGroup");
            ET.SubElement(etItemGroup, "Name").text = str(itemGroups[i].name);
            ET.SubElement(etItemGroup, "PrimaryGroup").text = str(itemGroups[i].primaryGroup);
            ET.SubElement(etItemGroup, "TaxCatName").text = str(itemGroups[i].taxCatName);
            ET.SubElement(etItemGroup, "ItemHSNCode").text = str(itemGroups[i].hsnCode);

    if (len(items) > 0):
        etItems = ET.SubElement(etRoot, "Items");
        for i in range(len(items)):
            etItem = ET.SubElement(etItems, "Item");
            ET.SubElement(etItem, "Name").text = str(items[i].name);
            ET.SubElement(etItem, "PrintName").text = str(items[i].name);
            ET.SubElement(etItem, "ParentGroup").text = str(items[i].parentGroup);
            ET.SubElement(etItem, "MainUnit").text = str(items[i].unit);
            ET.SubElement(etItem, "AltUnit").text = str(items[i].unit);
            ET.SubElement(etItem, "ConversionFactor").text = "1";
            ET.SubElement(etItem, "ConFactorType").text = "1";
            ET.SubElement(etItem, "SalePrice").text = str(items[i].salePrice);
            ET.SubElement(etItem, "PurchasePrice").text = "0.0";
            ET.SubElement(etItem, "PackingUnitName").text = str(items[i].unit);
            ET.SubElement(etItem, "ConFactorPU").text = "1";
            ET.SubElement(etItem, "StockValMethod").text = "5";
            ET.SubElement(etItem, "ItemSrNoType").text = "1";
            etAddres = ET.SubElement(etItem, "Address");
            ET.SubElement(etAddres, "OF");
            ET.SubElement(etItem, "DoNotMaintainStkBal").text = str(items[i].donotMaintainStkBalance);
            ET.SubElement(etItem, "PurchaseAccount").text = "Purchase";
            ET.SubElement(etItem, "SalesAccount").text = "Sales";
            ET.SubElement(etItem, "HSNCode").text = str(items[i].hsnCode);
            ET.SubElement(etItem, "TaxCategory").text = str(items[i].taxCategory);
            ET.SubElement(etItem, "HSNCodeGST").text = str(items[i].hsnCode);
            ET.SubElement(etItem, "TaxRateLocal").text = str(items[i].taxRateLocal);
            ET.SubElement(etItem, "TaxRateLocal1").text = str(items[i].taxRateLocal);
            ET.SubElement(etItem, "TaxRateCentral").text = str(2*items[i].taxRateLocal);
            ET.SubElement(etItem, "PercentOfAmount").text = "100";

    etMastersSummary = ET.SubElement(etRoot, "MastersSummary");
    if (len(itemGroups) > 0):
        AddMasterDet(etMastersSummary, "5", len(itemGroups));
    if (len(accounts) > 0):
        AddMasterDet(etMastersSummary, "2", len(accounts));
    if (len(items) > 0):
        AddMasterDet(etMastersSummary, "6", len(items));
    xmlStr = ET.tostring(etRoot);

    searchStr = "</BusyData>"
    replaceStr = """
    <Config>
	<CurDecimal>2</CurDecimal>
	<BillByBill>True</BillByBill>
	<CostCentres>False</CostCentres>
	<Budgets>False</Budgets>
	<Targets>False</Targets>
	<CreditLimits>False</CreditLimits>
	<MultiCurrency>False</MultiCurrency>
	<Brokers>False</Brokers>
	<Royality>False</Royality>
	<BatchByBatch>False</BatchByBatch>
	<AlternateUnit>False</AlternateUnit>
	<SalesTaxReports>True</SalesTaxReports>
	<ExciseReports>False</ExciseReports>
	<EnableOED>False</EnableOED>
	<EnableCess>False</EnableCess>
	<SalePurcAccWith>0</SalePurcAccWith>
	<AllocateExpenses>False</AllocateExpenses>
	<QtyDecimal>2</QtyDecimal>
	<PostAccSRPR>True</PostAccSRPR>
	<OrderProcessing>False</OrderProcessing>
	<SepStockUpdDate>False</SepStockUpdDate>
	<SepSVMForItems>False</SepSVMForItems>
	<DoubleEntry>True</DoubleEntry>
	<MultiplePriceList>False</MultiplePriceList>
	<SalesTaxType>1</SalesTaxType>
	<ExciseType>Mfr.</ExciseType>
	<STSurcharge>False</STSurcharge>
	<FBTEnable>False</FBTEnable>
	<ServiceTaxReports>False</ServiceTaxReports>
	<EnableSTCess>False</EnableSTCess>
	<TDSReports>False</TDSReports>
	<CompDep>False</CompDep>
	<BaseCurrency>Rs.</BaseCurrency>
	<EnableItemSizingInfo>False</EnableItemSizingInfo>
	<MultiGodown>True</MultiGodown>
	<EnableMRPWiseStock>False</EnableMRPWiseStock>
	<BatchReferenceMode>1</BatchReferenceMode>
	<EnableFreeQty>False</EnableFreeQty>
	<EnablePDC>True</EnablePDC>
	<EnableSerialNoTracking>False</EnableSerialNoTracking>
	<MaintainItemSNAltUnitAlso>False</MaintainItemSNAltUnitAlso>
	<MaintainItemSerialNoDescAlso>False</MaintainItemSerialNoDescAlso>
	<ItemSNDescLines>4</ItemSNDescLines>
	<EnableChallan>False</EnableChallan>
	<EnableSalesRetInSale>False</EnableSalesRetInSale>
	<EnablePurcRetInPurc>False</EnablePurcRetInPurc>
	<ItemSNWarranty>False</ItemSNWarranty>
	<EnableMultiParamStock>False</EnableMultiParamStock>
	<NoOfStockParam>1</NoOfStockParam>
	<InputTranPriceForParam>False</InputTranPriceForParam>
	<Parameter1 />
	<Parameter2 />
	<Parameter3 />
	<Parameter4 />
	<Parameter5 />
	<MaintainSalesPriceAlso>False</MaintainSalesPriceAlso>
	<MaintainMRPWithBatch>False</MaintainMRPWithBatch>
	<MaintainSalesPriceWithBatch>False</MaintainSalesPriceWithBatch>
	<MaintainMRPWithParam>False</MaintainMRPWithParam>
	<MaintainSalesPriceWithParam>False</MaintainSalesPriceWithParam>
	<MaintainMRPWithSrNo>False</MaintainMRPWithSrNo>
	<MaintainSalesPriceWithSrNo>False</MaintainSalesPriceWithSrNo>
	<MCAtItemLevel>False</MCAtItemLevel>
	<BrokerageLevel>0</BrokerageLevel>
	<MaintainSubLedger>False</MaintainSubLedger>
	<ParamStockConfig />
	<SaleQuotation>False</SaleQuotation>
	<PurchaseQuotation>False</PurchaseQuotation>
	<AllocateExtraExpensesVchWise>False</AllocateExtraExpensesVchWise>
	<EnableParamBCNGeneration>False</EnableParamBCNGeneration>
	<PricingMode>0</PricingMode>
	<MultiplePriceListForPurc>False</MultiplePriceListForPurc>
	<PricingModeForPurc>0</PricingModeForPurc>
	<ShowPartyPrice>False</ShowPartyPrice>
	<ShowPartyPriceForPurc>False</ShowPartyPriceForPurc>
	<ShowItemLastPrice>False</ShowItemLastPrice>
	<ShowItemLastPriceForPurc>False</ShowItemLastPriceForPurc>
	<PartyItemSalePrices>False</PartyItemSalePrices>
	<PartyItemSalePricesForPurc>False</PartyItemSalePricesForPurc>
	<ItemQtyDiscSlab>False</ItemQtyDiscSlab>
	<ItemQtyDiscSlabForPurc>False</ItemQtyDiscSlabForPurc>
	<ItemWiseDiscountType>0</ItemWiseDiscountType>
	<ItemWiseMarkUpType>3</ItemWiseMarkUpType>
	<DateWiseItemPricing>False</DateWiseItemPricing>
	<BankReconciliation>True</BankReconciliation>
	<BillByBillRefGroup>False</BillByBillRefGroup>
	<EnableFullAdjustment>False</EnableFullAdjustment>
	<ShowPendRefsTillDate>False</ShowPendRefsTillDate>
	<BillByBillRefNarration>False</BillByBillRefNarration>
	<BatchMfgDateFormat>0</BatchMfgDateFormat>
	<BatchExpDateFormat>0</BatchExpDateFormat>
	<DisallowCarryNegStockBatch>False</DisallowCarryNegStockBatch>
	<FullQtyAdjToBatchRef>False</FullQtyAdjToBatchRef>
	<InputBatchDateInRoman>False</InputBatchDateInRoman>
	<EnforceFullQtyAllocationParam>False</EnforceFullQtyAllocationParam>
	<EnableParamStockAdjDropdown>True</EnableParamStockAdjDropdown>
	<BCNNegativeStock>0</BCNNegativeStock>
	<BCNGenerationMode>0</BCNGenerationMode>
	<BCNAutoNoChar>6</BCNAutoNoChar>
	<BCNFormat>0</BCNFormat>
	<BCNDuplication>False</BCNDuplication>
	<MaintainAltQtyWithParam>False</MaintainAltQtyWithParam>
	<MaintainItemSNInstallationDet>False</MaintainItemSNInstallationDet>
	<PickSrNoFromAllMC>False</PickSrNoFromAllMC>
	<SrNoAdjWithoutSrNoStock>0</SrNoAdjWithoutSrNoStock>
	<SrNoAdjustmentMode>1</SrNoAdjustmentMode>
	<MaintainSerialNoImage>False</MaintainSerialNoImage>
	<SerialNoImagePath></SerialNoImagePath>
	<SerialNoImageNameType>1</SerialNoImageNameType>
	<EnforceFullQtyAllocationSrNo>False</EnforceFullQtyAllocationSrNo>
	<ConsolidateChallanItems>False</ConsolidateChallanItems>
	<RestrictSalewithoutChallan>False</RestrictSalewithoutChallan>
	<RestrictPurcwithoutChallan>False</RestrictPurcwithoutChallan>
	<RestrictSRwithoutChallan>False</RestrictSRwithoutChallan>
	<RestrictPRwithoutChallan>False</RestrictPRwithoutChallan>
	<SkipDefaultPriceInSaleChallan>False</SkipDefaultPriceInSaleChallan>
	<SkipDefaultPriceInPurcChallan>False</SkipDefaultPriceInPurcChallan>
	<AutoCreateChallanRefInAddMode>True</AutoCreateChallanRefInAddMode>
	<ConsolidateOrderItems>False</ConsolidateOrderItems>
	<RestrictSalewithoutOrder>False</RestrictSalewithoutOrder>
	<RestrictPurcwithoutOrder>False</RestrictPurcwithoutOrder>
	<RestrictSaleOrderModification>False</RestrictSaleOrderModification>
	<RestrictPurcOrderModification>False</RestrictPurcOrderModification>
	<AutoCreateOrderRefInAddMode>True</AutoCreateOrderRefInAddMode>
	<AutoCreateSaleQuotationRefInAddMode>True</AutoCreateSaleQuotationRefInAddMode>
	<AutoCreatePurchaseQuotationRefInAddMode>True</AutoCreatePurchaseQuotationRefInAddMode>
	<BCNPrefix></BCNPrefix>
	<AccountingInMatIssue>False</AccountingInMatIssue>
	<AccountingInMatRcpt>False</AccountingInMatRcpt>
	<AccountingInStkTfr>False</AccountingInStkTfr>
	<EnablePayroll>False</EnablePayroll>
	<EnableJobWork>False</EnableJobWork>
	<EnableJobWorkOutHouse>False</EnableJobWorkOutHouse>
	<EnableJobWorkInHouse>False</EnableJobWorkInHouse>
	<EnablePayrollMonthlySalary>True</EnablePayrollMonthlySalary>
	<EnablePayrollDailyWages>False</EnablePayrollDailyWages>
	<EnablePayrollProduction>False</EnablePayrollProduction>
	<EnablePayrollPF>False</EnablePayrollPF>
	<EnablePayrollESI>False</EnablePayrollESI>
	<EnablePayrollPT>False</EnablePayrollPT>
	<EnablePayrollEmpPassportDet>False</EnablePayrollEmpPassportDet>
	<EnablePayrollTDS>False</EnablePayrollTDS>
	<AdjustmentOfMaterialInPurc>False</AdjustmentOfMaterialInPurc>
	<AdjustmentOfMaterialInSale>False</AdjustmentOfMaterialInSale>
	<PurchaseIndent>False</PurchaseIndent>
	<EnableExecutiveInIndent>True</EnableExecutiveInIndent>
	<EnableScheme>False</EnableScheme>
	<TrackFinishedGoodsRecvIssuable>False</TrackFinishedGoodsRecvIssuable>
	<ApplicableGSTIndia>True</ApplicableGSTIndia>
	<PackagingUnit>False</PackagingUnit>
	<EnableAddCess>False</EnableAddCess>
</Config>
	<MasterConfiguration>
		<AccMastConfig>
			<AddnInfo0>2</AddnInfo0>
			<AddnInfoLen0>30</AddnInfoLen0>
			<AddnInfoBtLines0>Address : &lt;ACC_ADD(2_LINE)_LINE1,80,L&gt;</AddnInfoBtLines0>
			<AddnInfoBtLines1>          &lt;ACC_ADD(2_LINE)_LINE2,80,L&gt;</AddnInfoBtLines1>
			<AddnInfoBtLines2>Contact : &lt;ACC_CONTACT,30,L&gt;/&lt;ACC_MOBILE_NO,40,L&gt;</AddnInfoBtLines2>
			<AddnInfoBtLines3>TIN/CST : &lt;TIN_NO,20,L&gt;/&lt;ACC_CST,20,L&gt;</AddnInfoBtLines3>
			<AddnInfoBtReq>True</AddnInfoBtReq>
			<tmpMastType>2</tmpMastType>
			<tmpStamp>1</tmpStamp>
		</AccMastConfig>
		<ItemMastConfig>
			<AddnInfo0>2</AddnInfo0>
			<AddnInfoLen0>30</AddnInfoLen0>
			<tmpMastType>6</tmpMastType>
			<tmpStamp>1</tmpStamp>
		</ItemMastConfig>
		<MCMastConfig>
			<tmpMastType>11</tmpMastType>
		</MCMastConfig>
	</MasterConfiguration>
	<Version>
		<MajorVer>18</MajorVer>
		<MinorVer>0</MinorVer>
		<RevisionNo>2.4</RevisionNo>
		<SubRevisionNo></SubRevisionNo>
	</Version>
</BusyData>
    """
    xmlStr = xmlStr.replace(searchStr, replaceStr);
    fob = open(fileName, "wb+");
    fob.writelines(xmlStr);
    fob.close();

