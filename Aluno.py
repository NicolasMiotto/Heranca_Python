class Aluno():
    def __init__(self, nome, codigo, matricula):
        self.nome = nome
        self.codigo = codigo
        self.matricula = matricula
        self.imprimir()
       
    def imprimir(self):
            print ("Nome: ", self.nome)
            print ("Código: : ", self.codigo)
            print ("Matricula: ", self.matricula)

class AlunoEnsinoMedio(Aluno):
    def __init__ (self, nome, codigo, matricula, ano):
        Aluno.__init__(self,  nome, codigo, matricula)
        self.ano = ano
       
 
class AlunoGraduacao(Aluno):
    def __init__(self, nome, codigo, matricula, semestre):
        Aluno.__init__(self,  nome, codigo, matricula)
        self.semestre = semestre
    

alunog = AlunoGraduacao( "Nicolas Graduado", "0002", "001-1dw3", "06")
a1 = AlunoEnsinoMedio("Nicolas", "0001", "001-123", "01")