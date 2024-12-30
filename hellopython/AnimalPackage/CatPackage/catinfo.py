def speak_direct():
    print("meooov direct")

def speak_imported():
    print("meoooov imported")


if __name__ == "__main__": #eğer main klasörün kendisi çalıştırılırsa neyin çalıştırılacağını tanımlıyorum.
    speak_direct()
else:
    speak_imported()


#main.py de bu paketi çağırdığımda herhangi bir kod yazmasam bile, paket içerisinden şu noktada "meovv imported" dönecek.
#çünkü kodda eğer ana klasörden yani catinfo.py den çalıştırmazsam, bunu dönmesini istedim.
#Yani else:     speak_imported() şeklinde dönmesini istedim.

#Eğer bunu direk catinfo.py şeklinde paketin kendisi çalıştırırsam ise, bana speak_direct() dönecek. Çünkü öyle istedim.



