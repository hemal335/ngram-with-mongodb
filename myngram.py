def ngram_hemal1(s1):
    import operator
    s3 = s1.title()
    s2 = s3.split()
    len1 = len(s2)
    list4 = []
    li3=()
    list5={}
    list3 = {'Java': 1,
        '.Net': 2,
        'Python': 3,
        'Css': 4,
        'Object Oriented': 5,
        'C#': 6,
        'C++':7,
        'Ruby':8,
        'Oracle Database':9,
        'Nosql':10,
        'Hadoop':11,
        'HTML':12,
        'Perl':13,
        'Angularjs':14}
    i = 0
    # list4 = [i for i, j in zip(s2, list3) if i == j]
    for i in range(1, len1):
        if len1 >= 0:
            s4 = s2[i - 1] + ' ' + s2[i]
            s2.append(s4)
            # print s2

  
    for (key, value) in list3.items():
             if key in s2:
                li3= key, value
                list4.append(li3)
                
    list5 = dict(list4)                
    sorted_list4 = sorted(list5.iteritems(), key=operator.itemgetter(1))          
    return '\n'.join('{}:{}'.format(v,k) for k,v in sorted_list4)