# Coleta de Avaliações de Pacientes e Exportação para PDF e Excel

Este repositório contém dois scripts em Python para coletar avaliações de pacientes de clínicas e médicos em sites de avaliação, como Google Maps. As avaliações são extraídas e salvas em dois formatos: **PDF** e **Excel**.

## Funcionalidades

- O primeiro script coleta as avaliações de uma página específica e as exporta para uma planilha Excel.
- O segundo script coleta as avaliações, incluindo informações sobre o nome do paciente, nota, comentário, data e resposta da empresa, e exporta as avaliações para **PDF** e **Excel**.
- Ambos os scripts utilizam **Selenium** para navegação na página web e extração de dados, e **openpyxl** e **FPDF** para gerar os arquivos Excel e PDF.

## Pré-requisitos

Antes de rodar os scripts, você precisa instalar as bibliotecas necessárias. Você pode instalá-las usando `pip`:

```bash
pip install selenium fpdf openpyxl webdriver-manager
```
- Selenium: Para automação de navegação no navegador.
- Fpdf: Para gerar arquivos PDF.
- Openpyxl: Para gerar arquivos Excel.
- Webdriver-manager: Para gerenciar o driver do Chrome automaticamente.

Scripts
1. Script de Coleta de Avaliações Doctoralia

Este script coleta as avaliações de um site específico e as salva em um arquivo Excel.
Como funciona:

    Acessa a página de avaliações de um médico ou clínica.
    Extrai as avaliações de pacientes, incluindo o nome, nota, comentário, e outros dados.
    Salva as avaliações em um arquivo Excel com as colunas: Nome, Nota, Comentário, Data e Resposta do Médico.
    O arquivo Excel será salvo com um timestamp no nome do arquivo.

2. Script de Coleta de Avaliações e Exportação para PDF e Excel

Este script coleta as avaliações de um hospital no Google Maps, captura as informações de cada avaliação e as salva em dois formatos: PDF e Excel.
Como funciona:

    Acessa a página de avaliações do Google Maps de um hospital.
    Faz o scroll até carregar todas as avaliações disponíveis.
    Extrai informações detalhadas de cada avaliação, como:
        Nome do paciente
        Nota atribuída
        Comentário
        Resposta da empresa
        Data do comentário
    Salva as avaliações em dois formatos:
        PDF: Cada avaliação será registrada em uma página do PDF.
        Excel: As avaliações são salvas em uma planilha com as colunas: Nome, Nota, Data, Comentário, Resposta da Empresa.

Detalhes:

    safe_text: Função que garante a codificação correta do texto ao salvar no PDF.
    WebDriverWait: Utiliza o Selenium para aguardar o carregamento completo das páginas.
    scrolling: O script faz scroll na página até que todas as avaliações sejam carregadas, permitindo coletar o máximo possível de dados.

Execução dos Scripts
Rodando o Script:

    Script 1: O primeiro script coleta as avaliações e salva no formato Excel. Execute o script em sua IDE ou terminal.

    Script 2: O segundo script coleta as avaliações e as exporta para dois formatos, PDF e Excel. Execute o script da mesma maneira.

Após a execução, os arquivos avaliacoes.pdf e avaliacoes.xlsx serão gerados na sua pasta Documentos.
Observações

    Modo headless: O segundo script possui a opção de rodar o navegador sem interface gráfica. Para ativá-lo, altere a variável headless para True.

    Limite de Avaliações: O número de avaliações que o script irá coletar é configurável através da variável limite_avaliacoes.

Contribuição

Sinta-se à vontade para fazer melhorias ou relatar problemas. Caso tenha sugestões de melhorias ou novos recursos, envie um pull request ou abra uma issue no repositório.
