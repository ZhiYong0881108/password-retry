password = 'a123456'
n = 3
while n > 0:
    enter_your_password = input('Please enter your password:') 
    if enter_your_password == password: 
      print('登入成功!')
      break
    else:
      n -= 1
      print('密碼錯誤!' '還有', n, '次機會!')
