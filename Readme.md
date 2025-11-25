# 📊 Sistema Gerador de Relatórios (Enterprise Edition)

> Um exemplo prático de Engenharia de Software aplicada, demonstrando o uso de Padrões de Projeto (Design Patterns) para resolver problemas complexos de geração de documentos corporativos.

## 🎯 Sobre o Projeto
Este projeto simula um sistema corporativo (fictício "Tião do Gás & Cia") que coleta dados brutos de vendas e os transforma em relatórios profissionais em múltiplos formatos (**HTML, TXT, CSV**).

O diferencial deste código não é *o que* ele faz, mas **como** ele faz. A arquitetura foi desenhada para seguir os princípios **SOLID** e utilizar padrões **GoF** (Gang of Four) para garantir extensibilidade e manutenção.

## 🛠️ Tecnologias e Conceitos
* **Linguagem:** Python 3.x
* **Paradigma:** Orientação a Objetos (POO)
* **Conceitos Chave:** Herança, Polimorfismo, Encapsulamento, Abstração.

## 🏛️ Arquitetura e Design Patterns Utilizados

O sistema foi dividido em responsabilidades únicas, onde cada classe tem um papel claro, evitando "Classes Deus" (God Classes).

### 1. Singleton (`FilaImpressao`)
**O Problema:** Garantir que todos os setores da empresa enviem documentos para uma única fila de impressão centralizada, evitando conflitos de hardware.
**A Solução:** Implementação do padrão Singleton no Spooler de impressão.
* *Localização:* `class FilaImpressao`

### 2. Builder (`RelatorioBuilder`)
**O Problema:** Um relatório é um objeto complexo (tem título, corpo variável, rodapé opcional). Passar tudo isso num construtor gigante seria confuso.
**A Solução:** O padrão Builder permite a construção passo a passo do objeto, separando a construção da representação.
* *Localização:* `class RelatorioBuilder`

### 3. Factory Method (`ExportadorFactory`)
**O Problema:** O código principal (`main`) não deve saber a lógica complexa de instanciar cada tipo de exportador (HTML, CSV, etc.), nem deve ficar cheio de `if/else`.
**A Solução:** Uma Fábrica que decide qual objeto criar com base em uma string de configuração.
* *Localização:* `class ExportadorFactory`

### 4. Template Method & Polimorfismo (`Exportador`)
**O Problema:** Precisamos adicionar novos formatos (como PDF ou JSON) no futuro sem quebrar o código existente.
**A Solução:** Uso de Herança e Classes Abstratas. O código cliente chama `.exportar()` e o objeto executa sua versão específica (Polimorfismo).
* *Localização:* `class ExportadorHTML`, `ExportadorCSV`, etc.

---

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado.
2. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/sistema-relatorios-oop.git](https://github.com/SEU-USUARIO/sistema-relatorios-oop.git)
