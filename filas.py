class MaxHeap:
    def __init__(self):
        self.heap = [0]

    def input_paciente(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)

    def get_paciente(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        return False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        bigger = index
        if len(self.heap) > left and self.heap[bigger] < self.heap[left]:
            bigger = left
        if len(self.heap) > right and self.heap[bigger] < self.heap[right]:
            bigger = right

        if bigger != index:
            self.__swap(index, bigger)
            self.__bubbleDown(bigger)

class Paciente:
    def __init__(self, nome, tipoSanguineo, dataNasc):
        self.paciente = (nome, tipoSanguineo, dataNasc)
    
    def returnPaciente(self):
        return self.paciente

h = MaxHeap()
filaPrioridade = True
token = 999
listAtendidos = []
while filaPrioridade:
    print("="*60)
    print("Bem-vindo a Fila de Prioridade".center(60))
    print("="*60)
    print("Escolha uma Opção:\n1 - Adicionar novo paciente",
    "\n2 - Chamar próximo paciente",
    "\n3 - Mostrar próximo paciente",
    "\n4 - Listar os 5 últimos chamados\n")
    resp = int(input())
    if (resp == 1):
        nomeCompl = input("\nDigite o nome: ")
        tipoSang = input("\nDigite o tipo sanguíneo: ")
        dataNasc = input("\nDigite a data de nascimento: ")
        Paciente = Paciente(nomeCompl, tipoSang, dataNasc).returnPaciente()
        (nome, sangue, nasc) = Paciente
        urgency = int(input("\nDigite a urgência do caso (1 a 10): "))
        h.input_paciente((urgency, token, nome, sangue, nasc))
        token -= 1
    elif (resp == 2):
        try:
            Paciente = h.get_paciente()
            print("Nome: "+Paciente[2]+"\nSangue: "+Paciente[3]+"\nData de Nascimento: "+Paciente[4]+"\nUrgência: "+str(Paciente[0])+"\nFicha: "+str(Paciente[1])+"\n\n")
            listAtendidos.append(Paciente)
        except:
            print("Sem pacientes a ser chamados")
    elif (resp == 3):
        try:
            Paciente = h.peek()
            print("Nome: "+Paciente[2]+"\nSangue: "+Paciente[3]+"\nData de Nascimento: "+Paciente[4]+"\nUrgência: "+str(Paciente[0])+"\nFicha: "+str(Paciente[1])+"\n\n")
        except:
            print("Sem pacientes a ser mostrados")
    elif (resp == 4):
        print("\n--- Pacientes Atendidos ({}) ---".format(len(listAtendidos)))
        if (len(listAtendidos)>5):
            for item in range(len(listAtendidos)-1,len(listAtendidos)-5,-1):
                print(item)
                Paciente = listAtendidos[item]
                print("Nome: "+Paciente[2]+"\nSangue: "+Paciente[3]+"\nData de Nascimento: "+Paciente[4]+"\nUrgência: "+str(Paciente[0])+"\nFicha: "+str(Paciente[1])+"\n\n")
        else:
            for Paciente in listAtendidos:
                print("Nome: "+Paciente[2]+"\nSangue: "+Paciente[3]+"\nData de Nascimento: "+Paciente[4]+"\nUrgência: "+str(Paciente[0])+"\nFicha: "+str(Paciente[1])+"\n\n")
    else:
        print()