#for strings
#example
name="siddharth maurya"
#string functions
print(name.capitalize())#output=Siddharth maurya
print(len(name))#output=16
print(name.endswith("maurya"))#output=true but result is true/false
print(name.count("i"))#output=gives the number of occurance of something
print(name.upper())#output=SIDDHARTH MAURYA
print(name.replace("siddharth","darthsid"))#output=darthsid maurya; replaces oldword with a new word 
#string slicing
print(name[0:10])#prints characters from indexing 0 to (n-1),hence "siddharth"