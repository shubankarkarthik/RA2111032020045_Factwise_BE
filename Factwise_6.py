def count_letters(n):
    ones = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
    tens = {10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
    twenties = {20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6}
    hundred = 7
    thousand = 8
    
    total = 0
    
    for i in range(1,n+1):
        if i< 10:
            total += ones[i]
        elif i<20:
            total += tens[i]
        elif i<100:
            total += twenties[i-(i%10)]
            if i % 10 !=0:
                total += ones[i%10]
        else:
            total += ones[i//100]+hundred
            if i % 100 !=0:
                total += 3
                if i % 100<10:
                    total += ones[i%100]
                elif i%100<20:
                    total += tens[i%100]
                else:
                    total += twenties[(i%100)-(i%10)]
                    if i%10 !=0:
                        total += ones[i%10]
    
    if n == 1000:
        total += 3+thousand
        return total
    
result = count_letters(1000)
print(f"the total number of letters used is{result}")