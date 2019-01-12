import pydicom
ds = pydicom.read_file("ttfm.dcm")
bs = pydicom.read_file("bmode.dcm")
f = open("dicomtag.txt", "a")
f.write('****ttfm docom tags*****\n')
f.write('\n'.join(ds.dir()))
g = open("bicomtag.txt", "a")
g.write('****bmode dicom tags*****\n')
g.write('\n'.join(bs.dir()))
