import unittest
from gerenciador_tarefas import Tarefa, GerenciadorTarefas

class TestGerenciadorTarefas(unittest.TestCase):
    
    def setUp(self):
        """Configuração inicial para os testes."""
        self.gerenciador = GerenciadorTarefas()

    def test_adicionar_tarefa_valida(self):
        """Testa se uma tarefa válida pode ser adicionada."""
        tarefa = self.gerenciador.adicionar_tarefa(
            titulo="Comprar pão",
            descricao="Ir à padaria",
            prioridade="alta"
        )
        self.assertEqual(tarefa.titulo, "Comprar pão")
        self.assertEqual(tarefa.prioridade, "alta")
        self.assertEqual(tarefa.status, "pendente")
    
    def test_adicionar_tarefa_sem_titulo(self):
        """Testa se adicionar uma tarefa sem título levanta uma exceção."""
        with self.assertRaises(ValueError):
            self.gerenciador.adicionar_tarefa(
                titulo="",
                descricao="Sem título",
                prioridade="média"
            )

    def test_listar_tarefas(self):
        """Testa se todas as tarefas são listadas corretamente."""
        self.gerenciador.adicionar_tarefa("Tarefa 1", "Descrição 1", "baixa")
        self.gerenciador.adicionar_tarefa("Tarefa 2", "Descrição 2", "alta")
        tarefas = self.gerenciador.listar_tarefas()
        self.assertEqual(len(tarefas), 2)

    def test_filtrar_tarefas_por_prioridade(self):
        """Testa o filtro de tarefas por prioridade."""
        self.gerenciador.adicionar_tarefa("Tarefa 1", "Descrição 1", "baixa")
        self.gerenciador.adicionar_tarefa("Tarefa 2", "Descrição 2", "alta")
        tarefas_filtradas = self.gerenciador.listar_tarefas(prioridade="alta")
        self.assertEqual(len(tarefas_filtradas), 1)
        self.assertEqual(tarefas_filtradas[0].prioridade, "alta")

    def test_atualizar_status_tarefa(self):
        """Testa a atualização do status de uma tarefa."""
        tarefa = self.gerenciador.adicionar_tarefa("Tarefa 1", "Descrição 1", "média")
        self.gerenciador.atualizar_status(tarefa.id, "concluído")
        self.assertEqual(tarefa.status, "concluído")

    def test_remover_tarefa(self):
        """Testa a remoção de uma tarefa."""
        tarefa = self.gerenciador.adicionar_tarefa("Tarefa 1", "Descrição 1", "baixa")
        self.gerenciador.remover_tarefa(tarefa.id)
        tarefas = self.gerenciador.listar_tarefas()
        self.assertEqual(len(tarefas), 0)

if __name__ == "__main__":
    unittest.main()
