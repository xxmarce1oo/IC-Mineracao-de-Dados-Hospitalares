# Coleta de Avaliações de Pacientes e Exportação para PDF e Excel

Este repositório contém dois scripts em Python para coletar avaliações de pacientes de médicos, clínicas e outros estabelecimentos em sites de avaliação como o [Doctoralia](https://www.doctoralia.com) e [Google Maps](https://www.google.com.br/maps/preview). As avaliações extraídas são salvas em dois formatos: **PDF** e **Excel**.

## Funcionalidades

- **Coleta de Avaliações do [Doctoralia](https://www.doctoralia.com):**
    - O primeiro script coleta as avaliações de um médico ou clínica específico no Doctoralia.
    - As avaliações extraídas são salvas em um arquivo Excel, contendo: Nome, Nota, Comentário, Data e Resposta do Médico.

- **Coleta de Avaliações do [Google Maps](https://www.google.com.br/maps/preview):**
    - O segundo script coleta as avaliações de qualquer estabelecimento no Google Maps (não se limita a hospitais).
    - Este script pode ser utilizado para minerar dados de qualquer tipo de lugar registrado no Google Maps, como restaurantes, hotéis, escolas, entre outros.
    - As avaliações são extraídas e salvas em dois formatos: **PDF** e **Excel**, com informações como: Nome do paciente, Nota, Comentário, Resposta da Empresa e Data do comentário.

Ambos os scripts utilizam **Selenium** para automação da navegação e extração de dados, e **openpyxl** e **FPDF** para gerar os arquivos Excel e PDF, respectivamente.

## Pré-requisitos

Antes de rodar os scripts, você precisa instalar as bibliotecas necessárias. Você pode instalá-las usando `pip`:

```bash
pip install selenium fpdf openpyxl webdriver-manager
```
-Selenium: Para automação de navegação no navegador.
-Fpdf: Para gerar arquivos PDF.
-Openpyxl: Para gerar arquivos Excel.
-Webdriver-manager: Para gerenciar o driver do Chrome automaticamente.

Como Funciona
1. Script de Coleta de Avaliações do Doctoralia

Este script coleta as avaliações de um médico ou clínica no Doctoralia e as salva em um arquivo Excel.

Como funciona:

    Acessa a página de avaliações de um médico ou clínica.
    Extrai as avaliações dos pacientes, incluindo o nome, nota, comentário e outros dados relevantes.
    Salva as avaliações em um arquivo Excel com as colunas: Nome, Nota, Comentário, Data, Resposta do Médico.
    O arquivo Excel será salvo com um timestamp no nome do arquivo.

2. Script de Coleta de Avaliações do Google Maps e Exportação para PDF e Excel

Este script coleta as avaliações de qualquer estabelecimento no Google Maps e as salva em dois formatos: PDF e Excel.

Como funciona:

    Acessa a página de avaliações de um hospital ou qualquer estabelecimento no Google Maps.
    Realiza o scroll até carregar todas as avaliações disponíveis.
    Extrai informações detalhadas de cada avaliação, como:
        Nome do paciente
        Nota atribuída
        Comentário
        Resposta da empresa
        Data do comentário
    Salva as avaliações em dois formatos:
        PDF: Cada avaliação será registrada em uma nova página do PDF.
        Excel: As avaliações serão salvas em uma planilha com as colunas: Nome, Nota, Data, Comentário, Resposta da Empresa.

Detalhes importantes:

    safe_text: Função que garante a codificação correta do texto ao salvar no PDF.
    WebDriverWait: O Selenium é utilizado para garantir que a página tenha carregado completamente antes de tentar extrair os dados.
    Scroll automático: O script faz scroll na página até que todas as avaliações sejam carregadas, permitindo coletar o máximo possível de dados.

Limitação de Avaliações no Google Maps

Vale a pena observar que o número de avaliações que o script coleta do Google Maps pode ser limitado. Embora o Google Maps mostre uma quantidade muito maior de avaliações para alguns locais, o script consegue extrair um número limitado de avaliações, geralmente em torno de 400 a 340 avaliações, dependendo do estabelecimento. Isso ocorre porque o Google Maps carrega as avaliações de forma gradual enquanto o usuário faz scroll, e o script coleta até o limite configurado ou até que o scroll alcance o final da página.
Como Personalizar o Script
Alterar a URL

Para alterar a URL que o script irá acessar e coletar as avaliações, basta modificar o valor da variável url no código. Por exemplo, para coletar avaliações de um hospital diferente, você deve substituir a URL que está no código por uma nova URL da página do Google Maps ou Doctoralia.

Exemplo:

url = 'https://www.google.com/maps/place/Outro+Estabelecimento'  # Substitua esta URL pela nova URL desejada

Alterar o Número de Avaliações

O número de avaliações que o script irá coletar pode ser configurado através da variável limite_avaliacoes. O script continuará a coleta até atingir esse número de avaliações.

Exemplo:

limite_avaliacoes = 500  # Defina o limite desejado de avaliações a serem coletadas

Essa variável permite que você controle a quantidade de dados que será extraída. Basta substituir o número para o valor que você deseja.
Execução dos Scripts
Como rodar:

    Script 1 (Doctoralia): Este script coleta as avaliações e salva no formato Excel. Execute o script em sua IDE ou terminal.

    Script 2 (Google Maps): Este script coleta as avaliações e as exporta para dois formatos, PDF e Excel. Execute o script da mesma maneira.

Após a execução, os arquivos avaliacoes.pdf e avaliacoes.xlsx serão gerados na sua pasta Documentos.

Observações:

    Modo Headless: O segundo script permite rodar o navegador em modo headless (sem interface gráfica). Para ativá-lo, altere a variável headless para True.
    Limite de Avaliações: O número de avaliações a ser coletado é configurável através da variável limite_avaliacoes.

Contribuição

Sinta-se à vontade para fazer melhorias ou relatar problemas. Caso tenha sugestões de melhorias ou novos recursos, envie um pull request ou abra uma issue no repositório.
