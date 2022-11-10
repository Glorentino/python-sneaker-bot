
def UrlGenwithSize(size, model, name):
    base = 530
    mySize = (size-4) * 20
    finalSize = base+mySize
    Url=""+name+"/"+model+".html?" +model+"_"+str(finalSize)
    print(Url)

def UrlGenProduct(name, model):
    url =""+name+"/"+model+".html"
    print(url)

UrlGenProduct("Name","Model")
UrlGenProduct(8.5, "Model", "Name") #if 8.5 not available, it will fail

