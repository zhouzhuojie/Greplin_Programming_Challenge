import numpy as np

def LCStr(a,b):
    """
    Find the longest substring in string a and b. Using dynamic programming.
    L[i][j] Stores the length of the longest common string which ends at a[i] and b[j]
    We only need to find the max number in L. 
    Time complexity is O(len(a)*len(b))
    """
    L = np.zeros((len(a), len(b)))
    z = 0 # Use to denote the max element in L
    ret = [] # All the common sub-string with longest length will store in ret
    for i in xrange(0,len(a)):
        for j in xrange(0,len(b)):
            if a[i] == b[j]:
                if i==0 or j==0:
                    L[i][j] = 1
                else:
                    L[i][j] = L[i-1][j-1] + 1
                if L[i][j] > z:
                    z = L[i][j]
                    ret = []
                if L[i][j] == z:
                    ret.append(a[int(i-z+1):i+1])
            else:
                L[i][j] = 0
    return ret

if __name__=='__main__':
    a = 'FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'
    b = a[::-1] #Reverse a
    print LCStr(a,b)
