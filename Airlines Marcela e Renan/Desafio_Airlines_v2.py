Fortwo = []
Embarcado = []
# Terminal = ['Piloto','Oficial 1','Oficial 2','Chefe de Serviço','Comissária 1','Comissária 2','Policial',
# 'Prisioneiro']


def viagens(Terminal, i):
    if 'Policial' in Terminal[1] and 'Prisioneiro' in Terminal[2]:
        Fortwo.insert(1, Terminal.pop(2))
        Fortwo.insert(0, Terminal.pop(1))
        atualizar_arquivo(Terminal, i)
        print(f'Fortwo:{Fortwo}\nTerminal:{Terminal}')
        Embarcado.append(Fortwo.pop(1))
        atualizar_embarcado(Embarcado, i)
        Embarcado.append(Fortwo.pop(0))
        atualizar_embarcado(Embarcado, i)
        Terminal.insert(1, Embarcado.pop(2))
        atualizar_arquivo(Terminal, i)
        print(f'Embarcado:{Embarcado}\nTerminal:{Terminal}\n')
    else:
        Fortwo.append(Terminal.pop(0))
        Fortwo.append(Terminal.pop(0))
        atualizar_arquivo(Terminal, i)
        if 'Chefe de Servico' in Fortwo[1]:
            Fortwo.insert(0, Fortwo.pop(1))
        print(f'Fortwo:{Fortwo}\nTerminal:{Terminal}')
        Embarcado.append(Fortwo.pop(1))
        atualizar_embarcado(Embarcado, i)
        Terminal.insert(0, Fortwo.pop(0))
        if len(Terminal) == 1:
            Embarcado.append(Terminal.pop(0))
            atualizar_embarcado(Embarcado, i)
        atualizar_arquivo(Terminal, i)
        print(f'Embarcado:{Embarcado}\nTerminal:{Terminal}\n')


def ler_arquivo():
    """Carregamos as pessoas do Terminal para uma lista que sera atualizada constantemente..."""
    Terminal = []
    arq = open('Terminal.txt', 'r')
    for i in arq:
        i.strip()
        Terminal.append(i)
    arq.close()
    return Terminal


def atualizar_arquivo(Terminal, i):
    """Todo retorno de passageiro será marcado nesse txt"""
    arq = open('Em espera.txt', 'w')
    arq.write(''.join(Terminal))
    arq.write(f'--------Viagem {i}--------' + '\n')



def atualizar_embarcado(Embarcado, i):
    """Todo embarque de passageiros sera marcado nesse txt"""
    arq = open('Embarcado.txt', 'w')
    arq.write(''.join(Embarcado))
    arq.write(f'--------Viagem {i}--------' + '\n')


Terminal = ler_arquivo()
print(f'Terminal:{Terminal}\n')

# -- Usar Debug para fazer verificacoes nos txt
for i in range(1, 8):
    print(f'--------Viagem {i}--------')
    viagens(Terminal, i)
