# Python program to convert celsius to fahrenheit and vice versa
def c_to_f(cvalue):
    fahvalue = cvalue * 1.8 + 32
    print(f'The fahrenheit value for the given celsius value {cvalue} is {fahvalue}')
def f_to_c(fvalue):
    celvalue = (fvalue - 32) / 1.8
    print(f'The celsius value for the given fahrenheit value {fvalue} is {round(celvalue)}')
c_to_f(100)
f_to_c(212)

# output: 
# The fahrenheit value for the given celsius value 100 is 212.0
# The celsius value for the given fahrenheit value 212 is 100
