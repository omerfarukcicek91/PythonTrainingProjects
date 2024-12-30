import numpy as np

print("hello python")

print(np.zeros((3 , 4)))

# cd change directory

# cd komutundan sonra iligli dosya adını birebir aynı yazman lazım.

# cd .. ile de geri önceki klasöre giderim.

#dir ile de available klasörler ve nerede olduğunu görürüz. Directories

# cls ve clear temizlemek için kullanılır.

#ls ile dir aynı işlevde.


# import OmerModule


#OmerModule.example_func()


from OmerModule import example_func

example_func()
example_func()

#paket içerisinde birden fazla paket olabilir.

#bir paket içerisinde belli kodlar yazacağım, bunları şifrelemek istiyorum. örneğin cryptology paketi tutacağım. Yeni bir paket oluşturabilirim.


from AnimalPackage import info
from AnimalPackage.CatPackage import catinfo
from AnimalPackage.DogPackage import doginfo
info.info()
doginfo.havla()
catinfo.speak_imported()
catinfo.speak_direct()


