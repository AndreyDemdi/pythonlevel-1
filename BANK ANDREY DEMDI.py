#The code Bank system
#author AndeyDemdi
#version 12.12.2021


otv = input('Видите ваш пин код.')
if otv == '1234':
      print ('сколько снять с вашей карты варианты:150,10,100,50')
k = str(input());
if k == '150' :
    print ('С вашей карты снято 150руб')
 
elif k == '50':
    print ('С вашей карты снято 50руб')
 
elif k == '10':
    print ('С вашей карты снято 10руб')
 
elif k == '100руб':
    print ('С вашей карты снято 100 руб')
    
else:
    print('Не верный пин код ')
   


