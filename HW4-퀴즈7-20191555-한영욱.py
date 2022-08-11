#HW4-퀴즈7-20191555-한영욱
for i in range(1,51):
    with open(str(i)+"주차.txt",'w',encoding='utf8') as 보고서:
        보고서.write('-{}주차 보고서-'.format(i))
        보고서.write('\n부서:')
        보고서.write('\n이름:')
        보고서.write('\n업무요약:')
           
        
    
