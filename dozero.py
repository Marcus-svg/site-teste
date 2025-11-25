from abc import ABC, abstractmethod

class FilaImpressao:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FilaImpressao, cls).__new__(cls)
            cls._instance.fila = []
        return cls._instance

    def adicionar_documento(self, documento):
        print(f" Documento recebido na fila >> {documento[:15]}...")
        self.fila.append(documento)

    def imprimir_todos(self):
        print("\n--- INICIANDO IMPRESSÃO ---")
        if not self.fila:
            print("Fila vazia.")
        for i, doc in enumerate(self.fila, 1):
            print(f"Imprimindo Doc {i}:\n{doc}\n{'-'*30}")
        self.fila = []

class RelatorioDraft:
    def __init__(self):
        self.titulo = ""
        self.corpo = []
        self.rodape = ""

class RelatorioBuilder:
    def __init__(self):
        self.draft = RelatorioDraft()

    def set_titulo(self, texto):
        self.draft.titulo = texto
        return self

    def add_paragrafo(self, texto):
        self.draft.corpo.append(texto)
        return self

    def set_rodape(self, texto):
        self.draft.rodape = texto
        return self

    def build(self):
        return self.draft

class Exportador(ABC):
    @abstractmethod
    def exportar(self, draft: RelatorioDraft):
        pass

class ExportadorHTML(Exportador):
    def exportar(self, draft):
        html = f"<html>\n<h1>{draft.titulo}</h1>\n<body>"
        for p in draft.corpo:
            html += f"\n  <p>{p}</p>"
        html += f"\n  <footer>{draft.rodape}</footer>\n</body>\n</html>"
        return html

class ExportadorTXT(Exportador):
    def exportar(self, draft):
        txt = f"=== {draft.titulo.upper()} ===\n\n"
        for p in draft.corpo:
            txt += f"{p}\n"
        txt += f"\n--- {draft.rodape} ---"
        return txt

class ExportadorFactory:
    def criar_exportador(formato):
        if formato == "html":
            return ExportadorHTML()
        elif formato == "txt":
            return ExportadorTXT()
        else:
            print(f"Formato '{formato}' não suportado. Usando TXT padrão.")
            return ExportadorTXT()

if __name__ == "__main__":
    print("=== SISTEMA GERADOR DE RELATÓRIOS TG_CIA_LTA ===\n")

    dados_relatorio = (RelatorioBuilder()
                       .set_titulo("Relatório Mensal de Vendas")
                       .add_paragrafo("O faturamento subiu 22% em relação a outubro.")
                       .add_paragrafo("O produto mais vendido foi o 'Botijão P13'.")
                       .add_paragrafo("A meta para o próximo mês é dobrar a meta.")
                       .set_rodape("Tião do gás e cia")
                       .build())

    formato_escolhido = "txt"
    
    exportador = ExportadorFactory.criar_exportador(formato_escolhido)

    documento_final = exportador.exportar(dados_relatorio)

    spooler = FilaImpressao()
    spooler.adicionar_documento(documento_final)

    spooler.adicionar_documento("Lembrete: Reunião às 09h.")

    spooler.imprimir_todos()