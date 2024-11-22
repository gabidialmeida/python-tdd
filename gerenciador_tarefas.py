from uuid import uuid4

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, descricao, prioridade):
        if prioridade not in ["baixa", "média", "alta"]:
            raise ValueError("Prioridade inválida. Deve ser 'baixa', 'média' ou 'alta'.")
        id = str(uuid4())
        tarefa = Tarefa(titulo, descricao, prioridade, id)
        self.tarefas.append(tarefa)
        return tarefa

    def listar_tarefas(self, prioridade=None):
        if prioridade:
            return [tarefa for tarefa in self.tarefas if tarefa.prioridade == prioridade]
        return self.tarefas

    def atualizar_status(self, id, status):
        tarefa = next((t for t in self.tarefas if t.id == id), None)
        if tarefa is None:
            raise ValueError("Tarefa com ID não encontrada.")
        tarefa.status = status

    def remover_tarefa(self, id):
        tarefa = next((t for t in self.tarefas if t.id == id), None)
        if tarefa is None:
            raise ValueError("Tarefa com ID não encontrada.")
        self.tarefas.remove(tarefa)


class Tarefa:
    def __init__(self, titulo, descricao, prioridade, id):
        if not titulo:
            raise ValueError("O título da tarefa não pode ser vazio.")
        if prioridade not in ["baixa", "média", "alta"]:
            raise ValueError("Prioridade inválida. Deve ser 'baixa', 'média' ou 'alta'.")
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = "pendente"
        self.id = id
