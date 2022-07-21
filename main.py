


#draw id generator for OPAP KINO DRAWS
    #author GPS
    #date 2022 07 10

#log 2022 07 21 
    # added file output
    # modify the code
    # to able to do the task
    

#log 2022 07 20
    # Fixing code readibility
    # prior to port to github
    # use greek KINO string for OPAP files
#log 2022 07 10
    # PESOS added for excel functionality

'''
ABOUT PESOS AkA DOLLAR SIGN

the PESOS AKA DOLLAR SIGN IS NEEDED FOR EXCEL FILESYSTEMS TO 
LOCK THE ABSOLUTE REFERENCE TO THE ADDRESS OF THE CELL 
AND PREVENT THE RELATIVE SHIFTING OF THE REFERENCE IN QUENSION

'''

#variables

c1 = 61 # = equal sign for excel functions

c2 = 97 # is char a start of abs function 
c3 = 98 # is char b 
c4 = 115 # is char s  

c5 = 40 # is char with intent open abs function or ( )

#c6 = 75 # is char K 
# USING greek KINO string for OPAP files
c61 = (922) # K
c62 = (921) # I 
c63 = (925) # N 
c64 = (927) # O 

c7 = 33 # is char !
#REMARK PESOS here
c8 = 65 # Letter A 

#REMARK PESOS here
c9 = 4 # first row 

c10 = 41 # end abs excel function or ( )

#special variables

PESOS = 36 # dollarsign
x = 20 # use in range for 1 to 20 rows

firstrow = (4) # say to excel the first row is 4
lastrow = (5124)

# split the range


full = (5124)
half = (full / 2)
quart = (full / 4)

#  edit the start and end of generator

startrow = (firstrow)
endrow = (full)


f = open("drawiD.csv",'w')


for c9 in range(int(startrow),int(endrow)):
    
    for x in range(20):
        # REMARK PLACEMENT FOR CHR(PESOS) NEAR CHR(C8)
        
        
        f.write(chr(c1))
        f.write(chr(c2))
        f.write(chr(c3))
        f.write(chr(c4))
        f.write(chr(c5))
        f.write(chr(c61))
        f.write(chr(c62))
        f.write(chr(c63))
        f.write(chr(c64))
        f.write(chr(c7))
        f.write(chr(PESOS))
        f.write(chr(c8))
        f.write(chr(PESOS))
        f.write(str(c9))
        f.write(chr(c10))
        f.write(chr(10)) # new line
        
        #print(chr(c1),chr(c2),chr(c3),chr(c4),chr(c5),chr(c61),chr(c62),chr(c63),chr(c64),chr(c7),chr(PESOS),chr(c8),chr(PESOS), c9 , chr(c10), sep = '' )
        
        c8 = c8 + 0  # Stay in Alfa Column or freezze c8 value
        
    c9 = c9 + 1 # NEXT draW ID
    


    




