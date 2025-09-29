import json
import ale
# aqui e imppotacao 

print('---------innicio--------')
while(True):
 with open('pergunta.json','r') as arquivo:
    a=ale.per_ale()
    per=json.load(arquivo)
    por=per[1]['per{}'.format(a)]
    res=per[2]['re{}'.format(a)]
    print(por)
    rere=input('sua resposta ')
    if rere==res:
        print('----voce acerto----')
    else:
        print('------da errado----')
