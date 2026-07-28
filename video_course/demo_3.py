#BMI计算
user_weight=float(input('请输入您的体重(单位:kg):'))
user_height=float(input('请输入您的身高 (单位:m):'))
user_BMI=user_weight/user_height**2
print('您的BMI是'+str(user_BMI))
if user_BMI<18.5:
    print('您的BMI属偏瘦')
elif user_BMI<=24.9:
    print('您的BMI属正常')
elif user_BMI<=29.9:
    print('您的BMI属偏重')
else:
    print('您的BMI属肥胖')