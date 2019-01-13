import pydicom
ds = pydicom.read_file("ttfm.dcm")
bs = pydicom.read_file("bmode.dcm")
f = open("dicomtag.txt", "a")
f.write('****ttfm docom tags:Value*****\n')
for i in ds.dir():
   f.write(f'{i:30} : {ds.data_element(i).repval:100}'+'\n')
g = open("bicomtag.txt", "a")
g.write('****bmode dicom tags: Value*****\n')
for j in bs.dir():
    g.write(f'{j:30} : {bs.data_element(j).repval:100}'+'\n')