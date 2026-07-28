#KD
kills=input('请输入您的总击杀数')
dies=input('请输入您的总死亡数')
kills=int(kills)
dies=int(dies)
KD=(kills/dies)
print('您的KD为' + str(KD))
if KD<1:
    print('EZ')
else:
    print('这么强')