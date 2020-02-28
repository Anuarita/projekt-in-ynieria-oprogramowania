def get_functions_names_from_file(path):
    res=[]
    with open(path, 'r') as fr:
         for number, line in enumerate(fr):
             if re.match(r"^\s*?def",line) :
                 res.append(line.split(" ")[1].split("(")[0])
    return res

def count_method(path, method, otherMethod):
    count = 0
    t = 0
    str = 'def ' + method
    f = open(path,"r")
    for x in f:
        if t == 1:
            if 'def ' in x:
                t = 0
                f.close()
                return count
            if otherMethod in x:
                count=count+1
        elif str in x:
            t = 1
    f.close()
    return count

def count_method_size(path, method): #returns function line count
    count = 0
    t = 0
    str = 'def ' + method
    f = open(path,"r")
    for x in f:
        if t == 1:
           if 'def ' in x:
                t = 0
                return count
           count=count+1
        elif str in x:
            t = 1
    f.close()
    return count

def count_method1(path, method):
    count = 0
    f = open(path,"r")
    for x in f:
        if method in x:
            count = count + 1
    f.close()
    return count
