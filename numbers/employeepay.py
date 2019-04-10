# emplyee pay
# Kiran Pandey April 8, 2019

# read in input data into dictionary
emp = { '001':["Mary",15,40],
            '002':["John",22,25],
            '003':["Bob",35,4],
            '004':["Mel",43,62],
            '005':["Jen",17,33],
            '006':["Sue",29,45],
            '007':["Ken",40,36],
            '008':["Dave",20,17],
            '009':["Beth",37,37],
            '010':["Ray",16.5,80]
          }

# print header
print ('Id  ','Name ', 'Salary')

# compute employee salary and print
for id, empval in emp.items():
    empval.append(empval[1]*empval[2])
    if empval[2]>40:
        empval[3] = empval[3] + empval[1]*0.5*(empval[2]-40)
    print(id, empval[0], "    $ ", empval[3])
