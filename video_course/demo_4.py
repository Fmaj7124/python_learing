#结合input 字典 if判断 做一个查询国家首都的查询程序
Country_Capital={'中国' : '北京'  , '印度' : '新德里'}
Country_Capital['日本']='东京'
Country_Capital['朝鲜']='平壤'
Country_Capital['韩国']='首尔'
Country_Capital['法国']='巴黎'
Country_Capital['美国']='华盛顿'
Country_Capital['英国']='伦敦'
Country_Capital['俄罗斯']='莫斯科'
Country_Capital['德国']='柏林'
Country_Capital['瑞典']='斯德哥尔摩'

query=input('请输入您要查询的国家首都')
if query in Country_Capital:
    print('您查询的' + query + '的首都是'+Country_Capital[query])
else:
    print('您查询的国家首都暂未收入')
    print('当前收入的国家首都数为'+ str(len(Country_Capital)))