# a = [1, 3, 7, 13, 21,....]
# 1+0, 1+2, 3+4, 7+6

months = {"Apr": [1], "May": [1], "June": [1], "July": [1], "Aug": [1], "Sept": [1]}
months_list = list(months.keys())
__30 = ["Apr", "June", "Sept"]

for i in range(0, len(months)):
    num = 2
    if months_list[i] in __30:
        for j in range(1, 30):
            months[months_list[i]].append(months[months_list[i]][j - 1] + num)
            num += 2
    else:
        for j in range(1, 31):
            months[months_list[i]].append(months[months_list[i]][j - 1] + num)
            num += 2


def NoOfVehiclesSoldEachMonth():
    print("Month : Sold Count")
    for month in months:
        print(month, ":", sum(months[month]))


def SoldToRetailCus():
    total = 0
    print("\nRetail Customer Sales:")
    for month in months:
        for j in range(len(months[month])):
            if (j + 1) % 5 == 0:
                continue
            total += months[month][j]
    print("Total sold to retail customers:", total)
    return total


def SoldToCoporateCus():
    total = 0
    print("\nCoporate Customer Sales:")
    for month in months:
        for j in range(len(months[month])):
            if (j + 1) % 5 == 0:
                total += months[month][j]
    print("Total sold to coporate customers:", total)
    return total


def TotalSales():
    total = 0
    print("\nTotal Customer Sales:")
    for month in months:
        for j in range(len(months[month])):
            total += months[month][j]
    print("Total sold to customers:", total)
    return total


def TotalSoldAug15ToSept15():
    aug_sales = 0
    for i in range(14, len(months["Aug"])):
        aug_sales += months["Aug"][i]

    sept_sales = 0
    for i in range(0, 15):
        sept_sales += months["Sept"][i]

    total = aug_sales + sept_sales
    print("\nTotal vehicles sold from Aug 15th to Sept 15th:", total)
    return total


if __name__ == "__main__":
    NoOfVehiclesSoldEachMonth()
    SoldToRetailCus()
    SoldToCoporateCus()
    TotalSales()
    TotalSoldAug15ToSept15()
