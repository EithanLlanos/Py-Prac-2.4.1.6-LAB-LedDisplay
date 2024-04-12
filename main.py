# Scenario
# You've surely seen a seven-segment display.
# It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.
# Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.
# Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:       

#   # ### ### # # ### ### ### ### ### ### 
#   #   #   # # # #   #     # # # # # # # 
#   # ### ### ### ### ###   # ### ### # # 
#   # #     #   #   # # #   # # #   # # # 
#   # ### ###   # ### ###   # ### ### ###

# Note: the number 8 shows all the LED lights on.
# Your code has to display any non-negative integer number entered by the user.
# Tip: using a list containing patterns of all ten digits may be very helpful.

######################################################################################################################

# Test data
# Sample input:

# 123

# Sample output:

#   # ### ### 
#   #   #   # 
#   # ### ### 
#   # #     # 
#   # ### ### 

# Sample input:

# 9081726354

# Sample output:

# ### ### ###   # ### ### ### ### ### # # 
# # # # # # #   #   #   # #     # #   # # 
# ### # # ###   #   # ### ### ### ### ### 
#   # # # # #   #   # #   # #   #   #   # 
# ### ### ###   #   # ### ### ### ###   # 
######################################################################################################################

arr0=["###","# #","# #","# #","###"]
arr1=["  #","  #","  #","  #","  #"]
arr2=["###","  #","###","#  ","###"]
arr3=["###","  #","###","  #","###"]
arr4=["# #","# #","###","  #","  #"]
arr5=["###","#  ","###","  #","###"]
arr6=["###","#  ","###","# #","###"]
arr7=["###","  #","  #","  #","  #"]
arr8=["###","# #","###","# #","###"]
arr9=["###","# #","###","  #","  #"]
dic={"0":arr0,"1":arr1,"2":arr2,"3":arr3,"4":arr4,"5":arr5,"6":arr6,"7":arr7,"8":arr8,"9":arr9}
def ledfun(nmbr,dit):
    if not nmbr.isdigit():
        return "El número que ha ingresado no es válido"
    
    str=""
    for i in range(5):
        for c in nmbr:
            str+=dit[c][i] + " "
        str+="\n"
    return str

print(ledfun("9081726354",dic))