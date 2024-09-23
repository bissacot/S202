from database import Database
from motoristaDAO import MotoristaModel
from motoristaCLI import MotoristaCLI

db = Database(database="Exercicio_Avaliativo_1", collection="Motoristas")
motoristaModel = MotoristaModel(database=db)

motoristaCLI = MotoristaCLI(motoristaModel)
motoristaCLI.run()