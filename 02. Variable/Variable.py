# VARIABLES 
# GLOBAL VARIABLE VS LOCAL VARIABLE
# GLOBAL VARIABLE- DECLARED(CREATED) OUTSIDE ALL BLOCKS AND
#                   ACCESSABLE FROM ANYWHERE IN THE FILE 
# LOCAL VARIABLE- DECLARED(CREATED) INSIDE THE FUNCATION AND 
#                 ONLY ACCESSABLE INSIDE THE FUNCATION

var0=" Global variable"           # 0 INDENTATION (SPACE FOR RIGHT SID EOF SCREEN)
def f1():
    var0=" Nonlocal variable" 
    def local1():
        global var0
        print("Global :",var0)    # Access variable declare outside funcation
    local1()
    def local2():
        nonlocal var0
        print("Nonlocal :",var0)  # Access variable declare in parent block(f1())
    local2()
    def local3():
        var0="Local variable"     # Firstly pefer local var if present
        print("Local :",var0)           
    local3()
f1()

