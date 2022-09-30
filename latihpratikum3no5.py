q=str(input("apakah anda sebagai member ? y/n : "))
if q == "y":
    x=int(input("berat pakaian laki laki dalam kilo : "))
    z=int(input("berat pakaian wanita dalam kilo : "))
    y=x*7500 + z*8000
    print("total harga : " ,y)
if q == "n":
    x2=int(input("berat pakaian laki laki dalam kilo : "))
    z2=int(input("berat pakaian wanita dalam kilo : "))
    y2=x2*9000 + z2*10000
    print("total harga : " ,y2)