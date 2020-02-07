# Dupla Marcela Beduschi e Renan Berti

# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de bordo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python

Fortwo = []
Embarcado = []
Terminal = ['Piloto', 'Oficial 1', 'Oficial 2', 'Chefe de Serviço', 'Comissária 1', 'Comissária 2', 'Policial',
            'Prisioneiro']


def viagens():
    print(f'Terminal:{Terminal}\n')
    Fortwo.append(Terminal[0])
    Fortwo.append(Terminal[3])
    print(f'Fortwo:{Fortwo}')
    del Terminal[0]
    del Terminal[2]
    print(f'Terminal:{Terminal}')
    Embarcado.append(Fortwo[0])
    print(f'Embarcado:{Embarcado}')
    Terminal.append(Fortwo[1])
    print(f'Terminal:{Terminal}\n')
    Fortwo.clear()

    Fortwo.append(Terminal[6])
    Fortwo.append(Terminal[2])
    print(f'Fortwo:{Fortwo}')
    del Terminal[6]
    del Terminal[2]
    print(f'Terminal:{Terminal}')
    Embarcado.append(Fortwo[0])
    Embarcado.append(Fortwo[1])
    Terminal.append(Embarcado[0])
    del Embarcado[0]
    print(f'Embarcado:{Embarcado}')
    print(f'Terminal:{Terminal}\n')
    Fortwo.clear()

    Fortwo.append(Terminal[5])
    Fortwo.append(Terminal[0])
    print(f'Fortwo:{Fortwo}')
    del Terminal[0]
    del Terminal[4]
    print(f'Terminal:{Terminal}')
    Embarcado.append(Fortwo[1])
    print(f'Embarcado:{Embarcado}')
    Terminal.append(Fortwo[0])
    print(f'Terminal:{Terminal}\n')
    Fortwo.clear()

    Fortwo.append(Terminal[2])
    Fortwo.append(Terminal[3])
    print(f'Fortwo:{Fortwo}')
    del Terminal[3]
    del Terminal[2]
    print(f'Terminal:{Terminal}')
    Embarcado.append(Fortwo[0])
    Embarcado.append(Fortwo[1])
    Terminal.append(Embarcado[0])
    del Embarcado[0]
    print(f'Embarcado:{Embarcado}')
    print(f'Terminal:{Terminal}\n')
    Fortwo.clear()

    Fortwo.append(Terminal[2])
    Fortwo.append(Terminal[0])
    print(f'Fortwo:{Fortwo}')
    del Terminal[0]
    del Terminal[1]
    print(f'Terminal:{Terminal}')
    Embarcado.append(Fortwo[1])
    print(f'Embarcado:{Embarcado}')
    Terminal.append(Fortwo[0])
    print(f'Terminal:{Terminal}\n')
    Fortwo.clear()

    Fortwo.append(Terminal[1])
    Fortwo.append(Terminal[0])
    print(f'Fortwo:{Fortwo}')
    del Terminal[0]
    del Terminal[0]
    print(f'Terminal:{Terminal}')
    Embarcado.append(Fortwo[1])
    print(f'Embarcado:{Embarcado}')
    Terminal.append(Fortwo[0])
    print(f'Terminal:{Terminal}\n')
    Fortwo.clear()

    Fortwo.append(Terminal[0])
    Fortwo.append(Terminal[1])
    print(f'Fortwo:{Fortwo}')
    del Terminal[0]
    del Terminal[0]
    print(f'Terminal:{Terminal}')
    Embarcado.append(Fortwo[0])
    Embarcado.append(Fortwo[1])
    print(f'Embarcado:{Embarcado}')
    print(f'Terminal:{Terminal}\n')
    Fortwo.clear()


viagens()
