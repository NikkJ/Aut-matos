import random


class Carro:
    def __init__(self, tipo, cor, modelo,proxima_etapa):
        self.tipo = tipo
        self.cor = cor
        self.modelo = modelo
        self.proxima_etapa = proxima_etapa

    def avancar_estado(self):
        return self.proxima_etapa(self)


class Estados2:
    tempo_total = 0
    erros = 0
    carros = 0

    def __init__(self):
        self.tempo = 0
        self.erros = 0
        self.carros = 0

    def tipo(self, carro: Carro):
        self.tempo_total = 0
        print("Encaminhando para linha de produção do tipo: ", carro.tipo)
        carro.proxima_etapa = self.modelo
        return 0

    def modelo(self, carro: Carro):
        print("Iniciando a produção do modelo: ", carro.modelo)
        print("Encaminhando para a produção do chassi do modelo: ", carro.modelo)
        carro.proxima_etapa = self.chassi
        return 0

    def chassi(self, carro: Carro):
        print("Montando o chassi...")
        print("Definindo o número do chassi...")
        chassi = f"{modelo}{i}"
        print("Número do chassi: ", chassi)
        print("Encaminhando para a instalação das rodas...")
        carro.proxima_etapa = self.rodas
        return 0

    def rodas(self, carro: Carro):
        lista_rodas = ["correta","torta"]
        estado = random.choice(lista_rodas)
        erros = 0
        if estado == "correta":
            print("Roda montada com sucesso")
            print("Encaminhando para a montagem da lataria...")
            self.tempo_total += 3
        elif estado == "torta":
            erros += 1
            self.tempo_total += 1
            print("Roda se encontra torta")
            print("Encaminhando-a para o conserto...")
            a = random.randrange(0, 10)
            if a < 5:
                print("Roda continua torta")
                print("Buscando outro quarteto de rodas...")
                self.rodas
            else:
                print("Roda consertada, encaminhando para montagem da lataria")
        carro.proxima_etapa = self.lataria
        return erros

    def lataria(self, carro: Carro):
        lista_lataria = ["correta", "amassada", "solda fraca"]
        estado = random.choice(lista_lataria)
        modelo = carro.modelo
        erros = 0
        if estado == "correta":
            if modelo[2] == '1' or modelo[2] == '2':
                print("Identificado modelo de número: ",
                      modelo[2], ", iniciando a implantação do alumínio...")
                self.tempo_total += 4
                lista = ["solda fraca", "correta"]
                s = random.choice(lista)
                if s == "solda fraca":
                    erros+=1
                    print(
                        "Solda aparenta estar fraca, iniciando a resolda do alumínio...")
                    print("Solda correta...")

                    self.tempo_total += 0.5
            if modelo[2] == '3' or modelo[2] == '4':
                print("Identificado modelo de número: ",
                      modelo[2], ", iniciando a implantação do aço...")
                self.tempo_total += 5
                lista = ["solda fraca", "correta"]
                s = random.choice(lista)
                if s == "solda fraca":
                    erros+=1
                    print("Solda aparenta estar fraca, iniciando a resolda do aço...")
                    self.tempo_total += 0.7
                    print("Solda correta...")
            print("Lataria correta.")
            print("Encaminhando para a implementação do sistema elétrico...")
        elif estado == "amassada":
            erros += 1
            erro = random.uniform(4, 16)
            print("Lataria amassada com erro de: ", erro, "cm")
            print("Inciando o processo de desamasso...")
            i = 0
            for i in range(0, 6):
                erro -= random.uniform(0, erro)
                if erro < 0:
                    return False
                print("Erro dimininuido para: ", erro, "cm")
            self.tempo_total += 1.2
            print("Erro diminuido para: ", erro**3)
            print("Processo de desamasso realizado com sucesso, encaminhando para implementação do sistema elétrico...")
        elif estado == "solda fraca":
            erros += 1
            self.tempo_total += 1.4
            forca = random.randrange(10, 20)
            print(
                "Solda não passou nos testes de resistência, apresentou fragilidade a uma força de: ", forca, "N")
            print("Encaminhando para resolda...")
            forca = 0
            i = 0
            while forca < 20:
                forca = random.uniform(10, 25)
                print("Força atual: ", forca)
            print("Teste passado!")
            print("Encaminhando para implementação do sistema elétrico...")
        carro.proxima_etapa = self.sisElet
        return erros

    def sisElet(self, carro: Carro):
        lista_fio = ["correto", "partido"]
        fio = random.choice(lista_fio)
        erros = 0
        if fio == "correto":
            print("Sistema elétrico sendo implantado...")
            print("Implantação elétrica na carroceria: OK!")
            print("Implantação elétrica nas portas: OK!")
            self.tempo_total += 1.2
        elif fio == "partido":
            erros += 1
            self.tempo_total += 1.6
            print("Fio se apresenta partido")
            print("Iniciando conserto...")
            print("Refazendo cabeamento...")
            print("Processo completo!")
        print("Encaminhando para montagem do motor...")
        carro.proxima_etapa = self.mecanica
        return erros

    def mecanica(self, carro: Carro):
        print("Iniciando montagem do motor...")
        modelo = carro.modelo
        if modelo[2] == '1' or modelo[2] == '2':
            velocidade = 300
            self.tempo_total += 2
        if modelo[2] == '3' or modelo[2] == '4':
            velocidade = 350
            self.tempo_total += 2.2
        print("Motor para o modelo: ",
              modelo[2], ", buscando uma velocidade de: ", velocidade, "km/h")
        print("Motor montado corretamente!")
        print("Iniciando a implantação dos dois sistemas hidráulicos obrigatórios...")
        print("Implantando nas rodas dianteiras...")
        print("Implantando como modo de segurança nos traseiros...")
        print("Encaminhando para a montagem do radiador...")
        carro.proxima_etapa = self.radiador
        return 0

    def radiador(self, carro: Carro):
        print("Implantando o radiador...")
        self.tempo_total += 1.1
        carro.proxima_etapa = self.vidros
        return 0

    def vidros(self, carro: Carro):
        print("Iniciando a montagem da vidraçaria...")
        lista = ["quebrado", "arranhado", "correto"]
        s = random.choice(lista)
        erros = 0
        if s == "quebrado":
            erros += 1
            self.tempo_total += 1.2
            print("Vidro quebrou no processo, iniciando busca de outro...")
            self.vidros
        elif s == "arranhado":
            erros += 1
            self.tempo_total += 1
            print("Vidro se encontra arranhado")
            print("Iniciando processo de polimento...")
            print("Processo realizado com sucesso, encaminhando para pintura...")
        elif s == "correto":
            print("Vidro implantado com sucesso, encaminhando para pintura...")
            self.tempo_total += 0.8
        carro.proxima_etapa = self.pintura
        return erros

    def pintura(self, carro: Carro):
        print("Iniciando processo de pintura da cor: ", cor)
        print("Passando pelo polimento...")
        print("Processo completo!")
        print("Iniciando processo de secagem!")
        print("Encaminhando para o estoque...")
        self.tempo_total += 3
        self.carros += 1
        carro.proxima_etapa = None
        return 0


def verifica(producao):
    offset = 8
    begin = -8
    if len(producao)%8 == 0:
        while begin < len(producao):
            begin += offset
            info = producao[begin: begin + offset]
            tipo, modelo, cor = info[0: 2], info[2: 5], info[5: 8]
            num_tipo = int(tipo[1])
            num_cor = int(cor[2])
            if 1 <= num_tipo and num_tipo <= 8:
                if modelo[1] == tipo[1] and (modelo[2] in ('1', '2')):
                    if cor[1] == tipo[1] and 1 <= num_cor and num_cor <= 4:
                        return True
                    else:
                        print("Fita de produção errada!")

producao = input("Insira a produção: ")
if(verifica(producao)):
    offset = 8
    begin = 0
    Estados = Estados2()
    tempo = 0
    i = 0
    tam_producao = int(len(producao))
    carros = list()
    while begin < len(producao) - 1 and (Estados.erros <= 7):

        info = producao[begin: begin + offset]
        tipo, modelo, cor = info[0: 2], info[2: 5], info[5: 8]
        carros.append(Carro(tipo, cor, modelo, Estados.tipo))
        i = +1
        begin += offset

    a_ser_prod = carros
    tipos = [[] for x in range(8)]
    for car in carros:
        if car.tipo[1] == '1':
            tipos[0].append(car)
        elif car.tipo[1] == '2':
            tipos[1].append(car)
        elif car.tipo[1] == '3':
            tipos[2].append(car)
        elif car.tipo[1] == '4':
            tipos[3].append(car)
        elif car.tipo[1] == '5':
            tipos[4].append(car)
        elif car.tipo[1] == '5':
            tipos[5].append(car)
        elif car.tipo[1] == '7':
            tipos[6].append(car)
        elif car.tipo[1] == '8':
            tipos[7].append(car)

    linhas= [
        [True, 0, tipos[0], list()],
        [True, 0, tipos[1], list()],
        [True, 0, tipos[2], list()],
        [True, 0, tipos[3], list()],
        [True, 0, tipos[4], list()],
        [True, 0, tipos[5], list()],
        [True, 0, tipos[6], list()],
        [True, 0, tipos[7], list()],
    ]
    #linhas[0] = carros a serem produzidos ainda
    #linhas[1] = erros
    #linhas[2] = 
    #linhas[3] = quantidade de carros da mesma linha
    produzidos = list()
    while True:
        g = False
        for linha in linhas:
            #linha[0] = carros a serem produzidos ainda
            #linha[1] = erros
            #linha[2] = 
            #linha[3] = carros da mesma linha
            if linha[0] and linha[1] <= 7:
                if linha[2]:
                    linha[3].append(linha[2].pop(0))
                for carro in linha[3]:
                    linha[1] += carro.avancar_estado()
                    if carro.proxima_etapa == None:
                        produzidos.append(linha[3].pop(0))
                if not linha[3]:
                    linha[0] = False
                else:
                    g = True

        if not g:
            break

# t1m11c11
