
#find the largest number value sub-string within a given string
#letter and digit
#abc123gh45pl => 123

def find_largest_number(s):
    biggest_number = "";
    temp = "";
    for i in s:
        if i.isdigit():
            temp = temp + i;
            if compare(temp,biggest_number):
                biggest_number = temp;
        else:
            temp = "";
    return biggest_number;

def compare(a,b):
    if len(a) > len(b):
        i = len(a) - len(b); 
        while i:
            b = "0" + b;
            i = i - 1
    elif len(b) > len(a):
        i = len(b) - len(a); 
        while i:
            a = "0" + a;
            i = i - 1;
    i = 0
    while i < len(a):
        if int(a[i]) > int(b[i]):
            return True;
        elif int(a[i]) < int(b[i]):
            return False;
        i = i +1;
                

a = "bc23200000gh00456pl8888888888888"
print find_largest_number(a);
