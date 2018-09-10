#99% of the time, it works all the time.

def parse_int(string):
    num_dic = {
        "zero":0,
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9,
        "ten":10,
        "eleven":11,
        "twelve":12,
        "thirteen":13,
        "forteen":14,
        "fifteen":15,
        "sixteen":16,
        "seventeen":17,
        "eighteen":18,
        "nineteen":19,
        "twenty":20,
        "thirty":30,
        "forty":40,
        "fifty":50,
        "sixty":60,
        "seventy":70,
        "eighty":80,
        "ninety":90,
    }
    mult_dic = {
        "hundred":100,
        "thousand":1000,
        "million":1000000,
    }
    string = string.lower()
    l = string.split(' ')
    if len(l)==0 and string.find('-')==-1:
        return num_dic[string]
        
    l = [x for x in l if x != 'and']
    
    total = 0
    t = []
    for i, num in enumerate(l):
        if num in mult_dic:
            t[-1].append(mult_dic[num])
        else:
            if "-" in num:
                hyph = num.find('-')
                t.append([num_dic[num[:hyph]]+num_dic[num[hyph+1:]]])
            else:
                t.append([num_dic[num]])

    skip = False
    for i, v in enumerate(t):
        if skip == False:
            if len(v)==1:
                total += v[0]
            elif i != len(t)-1:
                if len(t[i+1])==2:
                    if v[1] < t[i+1][1]:
                        total += ((v[0]*v[1]) + t[i+1][0]) * t[i+1][1]
                    else:
                        total += v[0]*v[1] + t[i+1][0] * t[1+1][1]
                    skip = True
                else:
                    total += v[0] * v[1]
        else:
            skip = False
            
    return total
