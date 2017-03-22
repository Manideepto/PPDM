from BPHospital1 import BPHospital1
from BPHospital2 import BPHospital2
from BPHospital3 import BPHospital3
from BPHospital4 import BPHospital4
from BPHospital5 import BPHospital5
from BPHospital6 import BPHospital6
from BPHospital7 import BPHospital7
from BPHospital8 import BPHospital8
from Thirdparty import Thirdparty

e=list()
bp1=BPHospital1();
e=bp1.EncryptBPCategory(e)
bp2=BPHospital2();
e=bp2.EncryptBPCategory(e)
bp3=BPHospital3();
e=bp3.EncryptBPCategory(e)
bp4=BPHospital4();
e=bp4.EncryptBPCategory(e)
bp5=BPHospital5();
e=bp5.EncryptBPCategory(e)
bp6=BPHospital6();
e=bp6.EncryptBPCategory(e)
bp7=BPHospital7();
e=bp7.EncryptBPCategory(e)
bp8=BPHospital8();
e=bp8.EncryptBPCategory(e)

d=list()
tp=Thirdparty()
d=tp.DecryptSum(e)

"""
for i in range(d):
	d[i]=d[i]/8
"""
	

bp1.PlotwithMean(d)
bp2.PlotwithMean(d)
bp3.PlotwithMean(d)
bp4.PlotwithMean(d)
bp5.PlotwithMean(d)
bp6.PlotwithMean(d)
bp7.PlotwithMean(d)
bp8.PlotwithMean(d)