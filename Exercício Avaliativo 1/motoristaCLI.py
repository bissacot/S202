from corrida import Corrida
from motorista import Motorista
from passageiro import Passageiro


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        #Motorista
        motoristaNota = int(input("Entre com a nota do Motorista: "))

        #Corrida
        corridaNota = int(input("Entre com a nota da Corrida: "))
        corridaDistancia = int(input("Entre com a distancia da Corrida: "))
        corridaValor = int(input("Entre com o valor da Corrida: "))

        #Passageiro
        passageiroNome = input("Entre com o nome do Passageiro: ")
        passageiroDocumento = int(input("Entre com o documento do Passageiro: "))
        
        #Objetos
        passageiroObjeto = Passageiro(passageiroNome, passageiroDocumento)
        corridaObjeto = Corrida(corridaNota, corridaDistancia, corridaValor, passageiroObjeto)
        motoristaObjeto = Motorista(corridaObjeto, motoristaNota)

        #Enviando
        self.motorista_model.create_motorista(corridaObjeto, motoristaNota)

    def read_motorista(self):
        id = input("Enter the id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)
        if motorista:
            print(f"Name: {motorista['name']}")
            print(f"Age: {motorista['age']}")

    def update_motorista(self):
        id = input("Enter the id: ")
        name = input("Enter the new name: ")
        age = int(input("Enter the new age: "))
        self.motorista_model.update_motorista(id, name, age)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motorista_model.delete_motorista(id)
        
    def run(self):
        print("Welcome to the motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()