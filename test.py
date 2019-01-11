i = 3
while i < 4 and i >0 :
    a = input('請輸入密碼:')   
    if a == 'a123456':
    	break
    	print('登入成功')
    elif a != 'a123456':
    	print('密碼錯誤,還有',i - 1,'次機會')
    i = i - 1   
