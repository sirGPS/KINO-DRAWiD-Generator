


#draw id generator for OPAP KINO DRAWS
    #author GPS
    #date 2022 07 10


#log 2022 07 20
    # Fixing code readibility
    # prior to port to github
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
c6 = 75 # is char K 
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

# split the range

full = (5124)
half = (full / 2)
quart = (full / 4)






for c9 in range(int(firstrow),int(quart)):
    
    for x in range(20):
        # REMARK PLACEMENT FOR CHR(PESOS) NEAR CHR(C8)
        print(chr(c1),chr(c2),chr(c3),chr(c4),chr(c5),chr(c6),chr(c7),chr(PESOS),chr(c8),chr(PESOS), c9 , chr(c10), sep = '' )
        
        c8 = c8 + 0  # Stay in Alfa Column or freezze c8 value
        
    c9 = c9 + 1 # NEXT draW ID
    


    

