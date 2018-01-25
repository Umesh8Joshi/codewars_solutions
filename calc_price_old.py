def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    i = 1
    while startPriceNew > savingperMonth:
        savingperMonth += 1000
        startPriceNew *= float(percentLossByMonth/100)
        startPriceOld *= float(percentLossByMonth/100)
        if i%2 == 0:    percentLossByMonth += 0.5
        i += 1
    return [i , int(savingperMonth - startPriceNew)]
if __name__ == "__main__":
    print(nbMonths(12000,8000,1000,1.5))