def maxScore(cardPoints,k):
    n = len(cardPoints)
    if k>=n:
        return sum(cardPoints)
    
    current_sum = sum(cardPoints[:k])
    max_sum = current_sum
    
    for i in range(k):
        current_sum = current_sum - cardPoints[k-i-1] + cardPoints[n-i-1]
        max_sum = max(max_sum,current_sum)
        
    return max_sum

print(maxScore([1,2,3,4,5,6,1],3)) 
print(maxScore([2,2,2],2))
print(maxScore({9,7,7,9,7,7,9],7))
