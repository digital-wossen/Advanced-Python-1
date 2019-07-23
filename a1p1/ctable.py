# JTSK-350112
# a1 1.py
# Wossen Hailemariam
# w.haillemarim@jacobs-university.de


start = int(input('Enter the start:'))
end = int(input('Enter the end:'))
step = int(input('Enter the step size here:'))
print ("inch", "cm")
for i in range(start, end+1, step):
    result = i * 2.54
    print ('%.1f'%i,"" ,'%.1f'%result)
        
 



