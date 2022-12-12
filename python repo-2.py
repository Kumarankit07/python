Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
contacts= {
"PRASHANT": 7263738387,
"HARSHIT": 7584737373,
"SHREYA":3256342542,
"ABHINAV":3453646543,
"KARTIKEY":6784536343,
"DEVANSH":6854443334,
"ROHINI":9754463336
}



def single_search():
	name=input(">>>Enter the name of the contact you wish to search for: ").upper()
	if name in contacts:
		print(f"\n{name}: {contacts[name]}")
	else:
	   b=input("\nNo such contact found \nIf you wish to add one, type 'Yes' else type 'No': ").lower()
	   if b=="yes":
	     new_contact(name)
	     print(f"{name}: {contacts[name]}")
	   elif b=="no":
	     	pass
	   else:
	     print("Enter either yes or no nigga")


def multiple_search():
	     result={}
	     s1=[]
	     s=0
	     name1=input(">>>Enter the names of the contacts seperated by commas: ").split(",")
	     for i in name1:
	     			i=i.upper()
	     			if i in contacts:
	     				result[i]=contacts[i]
	     			else:
	     				s1.append(i)
	     				s+=1
	     if s>0:
	     	c=(input(f"\nCouldn't find contacts {s1} . \nDo you wish to add them? Enter Yes or No: ")).lower()
... 	     	if c=="yes":
... 	     		for i in s1:
... 	     			new_contact(i)
... 	     			if i in contacts:
... 	     				result[i]=contacts[i]
... 	     		print()
... 	     		print(result)
... 	     	elif c=="no":
... 	     		print()
... 	     		if result=={}:
... 	     			pass
... 	     	else:
... 	     		print("\nUnpadh")
... 	     else:
... 	     	print()
... 	     	print(result)
... 	     	
... 
... def new_contact(contact_name):
... 	     print()
... 	     contact_number=int(input(">>>Enter their contact number: "))
... 	     contacts[contact_name]=contact_number
... 	     
... choice=int(input("Would you like to: \n\n1. Search for a single contact \n2. List all the contacts \n3. Search for multiple contacts \n \n>>>Enter your choice: "))
... 
... if choice==1:
... 	single_search()
... 	
... elif choice==2:
... 	print()
... 	print(contacts)
... 	
... elif choice==3:
... 	multiple_search()
... 
... else:
