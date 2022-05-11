from datetime import date
from datetime import timedelta
from datetime import datetime
import sys
import xml.etree.ElementTree as XM

def method_depart_return(x,y):
    Dx = int(x)
    Ry = int(y)
    curr_dt = date.today()
    DEPART = curr_dt + timedelta(days=Dx)
    RETURN = curr_dt + timedelta(days=Ry)

    #modify xml

    basetree = XM.parse("C:\\Users\\SURAJMAYANDE\\OneDrive - Virtusa\\Desktop\\test_payload1.xml")
    myroot = basetree.getroot()

    for depart_date in myroot.iter('DEPART'):
        new_depart_date = DEPART
        depart_date.text = str(new_depart_date)
        
    for return_date in myroot.iter('RETURN'):
        new_return_date = RETURN
        return_date.text = str(new_return_date)
        
    basetree.write('output.xml')

if __name__ == '__main__':
    val1 = input("enter int X for Depart date:")
    val2 = input("enter int y for RETURN date:")
    
    method_depart_return(val1,val2)
    
