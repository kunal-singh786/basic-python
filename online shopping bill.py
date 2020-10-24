print("                         Online shopping bill")
print()
jeans= int(input("Jeans Quantity:-"))
jeans_cost= float(input("cost/item:-"))
c = jeans*jeans_cost
s =c + ((c*18)/100)
print("Total cost of",jeans," jeans is",c,"including 18% of GST is",s)
print()
t_shirt = int(input("T shirt Quantity:-"))
t_shirt_cost= float(input("cost/item:-"))
d = (t_shirt*t_shirt_cost)
t =d + (d*18)/100
print("Total cost of",t_shirt,"piece T shirt is",d,"including 18% of GST is",t)
print()
headphone= int(input("Headphone Quantity:-"))
headphone_cost= float(input("cost/item:-"))
e = headphone*headphone_cost
u = e + (e*18)/100
print("Total cost of",headphone,"piece headphone is",e,"including 18% of GST is",u)
print()
mobile = int(input("Samsung Note 20 Plus Quantity:-"))
mobile_cost= float(input("cost/pack:-"))
f = mobile*mobile_cost
v =f + (f*18)/100
print("Total cost of",mobile," Samsung Note 20 Plus is",f,"including 18% of GST is",v)
total = s+t+u+v
print()
print("Pay",total,"only")