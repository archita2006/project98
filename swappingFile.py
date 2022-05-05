def swapFileData():
    
    file1=input("enter file1")
    file2=input("enter file2")
     with open(file1,"r")as a:
        a.write(data_b)
      with open(file2,"r")as b:
        b.write(data_a)

    with open(file1,"w")as a:
        a.write(data_b)
    with open(file2,"w")as b:
        b.write(data_a)

swapFileData()