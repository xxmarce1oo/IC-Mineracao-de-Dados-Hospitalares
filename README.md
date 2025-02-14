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
