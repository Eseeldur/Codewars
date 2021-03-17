"""
eng version
of popular song '99 bottles'
"""


word = "bottles"
for beer_num in range (99, 0, -1):
    if beer_num==1:
        word="bottle"
    print(beer_num, word, " of beer on the wall")
    print (beer_num, word, "  of beer! ")
    print ("Take one down, pass it around")
    print (beer_num-1, word, " of beer on the wall! \n")


"""
rus version
"""
"""
for beer_num in range (9, 0, -1):
    
    word = "бутылок"
    if beer_num%10==1 and beer_num!=11:
        word="бутылка"
    elif beer_num==14 or beer_num==13 or beer_num==12 or beer_num==0:
        word = "бутылок"
    elif beer_num%10==2 or beer_num%10==3 or beer_num%10==4:
        word="бутылки"
        
    print(beer_num, word, " пива на стене")
    print (beer_num, word, " пива! ")
    print ("Возьми одну, пусти по кругу")

    
    if (beer_num-1)%10==1 and (beer_num-1)!=11:
        word="бутылка"
    elif (beer_num-1)==14 or (beer_num-1)==13 or (beer_num-1)==12 or (beer_num-1)==0:
        word = "бутылок"
    elif (beer_num-1)%10==2 or (beer_num-1)%10==3 or (beer_num-1)%10==4:
        word="бутылки"
        
    print (beer_num-1, word, " пива на стене! \n")
"""
