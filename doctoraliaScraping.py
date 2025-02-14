import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from openpyxl import Workbook

# Início do rastreamento do tempo de execução
start_time = time.time()

# Função para configurar o driver do Selenium
def setup_driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    return driver

# Função para fechar o pop-up de cookies
def close_cookie_popup(driver):
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'floating-cookie-info-btn'))
        )
        cookie_button.click()
        print("Pop-up de cookies fechado.")
    except TimeoutException:
        print("Nenhum pop-up de cookies encontrado.")

# Função para carregar todas as avaliações
def load_all_reviews(driver):
    close_cookie_popup(driver)  # Tentar fechar o pop-up de cookies uma vez no início

    while True:
        try:
            see_more_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-id="load-more-opinions"]'))
            )
            driver.execute_script("arguments[0].click();", see_more_button)
            print("Botão 'Veja mais' clicado para carregar mais avaliações.")
            time.sleep(2)  # Espera para o carregamento de novas avaliações

        except (TimeoutException, ElementClickInterceptedException):
            print("Final da página alcançado ou botão 'Veja mais' não encontrado.")
            break

# Função para extrair informações de cada avaliação
def extract_review_data(avaliacao):
    data = {
        "nome": 'Nome não encontrado',
        "nota": 'Nota não encontrada',
        "comentario": 'Comentário não encontrado',
        "resposta_medico": 'Resposta do médico não encontrada',
        "data_comentario": 'Data não encontrada',
        "nome_doutor": 'Nome do doutor não encontrado',
        "especialidade": 'Especialidade não encontrada'
    }

    try:
        nome_tag = avaliacao.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]')
        data["nome"] = nome_tag.text.strip()
    except NoSuchElementException:
        pass

    try:
        nota_tag = avaliacao.find_element(By.CSS_SELECTOR, '[data-score]')
        data["nota"] = nota_tag.get_attribute("data-score")
    except NoSuchElementException:
        pass

    try:
        comentario_tag = avaliacao.find_element(By.CSS_SELECTOR, 'p[itemprop="reviewBody"]')
        data["comentario"] = comentario_tag.text.strip()
        ##print(f"Comentário encontrado: {data['comentario']}")  # Depuração
    except NoSuchElementException:
        ##print("Comentário não encontrado.")  # Depuração
        pass

    try:
        data_tag = avaliacao.find_element(By.CSS_SELECTOR, 'time[itemprop="datePublished"]')
        data["data_comentario"] = data_tag.get_attribute("datetime")
    except NoSuchElementException:
        pass

    try:
        doutor_tag = avaliacao.find_element(By.CSS_SELECTOR, 'span.small.text-muted')
        doutor_info = doutor_tag.text.strip().split(' • ')
        data["nome_doutor"] = doutor_info[0]
        data["especialidade"] = doutor_info[1] if len(doutor_info) > 1 else 'Especialidade não encontrada'
    except NoSuchElementException:
        pass

    try:
        resposta_medico_div = avaliacao.find_element(By.CLASS_NAME, 'card-body.pb-1')
        resposta_medico_tag = resposta_medico_div.find_element(By.XPATH, "./p[not(@class)]")
        data["resposta_medico"] = resposta_medico_tag.text.strip()
    except NoSuchElementException:
        pass

    return data


# Função para salvar as avaliações no Excel
def save_reviews_to_excel(reviews):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Avaliações"

    # Adicionar cabeçalhos
    sheet.append(["Nome", "Nota", "Comentário", "Resposta do Médico", "Data do Comentário", "Nome do Doutor", "Especialidade"])

    # Adicionar avaliações
    for review in reviews:
        sheet.append([review["nome"], review["nota"], review["comentario"], review["resposta_medico"],
                      review["data_comentario"], review["nome_doutor"], review["especialidade"]])

    # Salvar o arquivo Excel na área de trabalho com timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", f"avaliacoes_{timestamp}.xlsx")
    workbook.save(desktop_path)
    print(f"Arquivo Excel salvo com sucesso em: {desktop_path}")

# Função principal para o scraping e exportação
def main():
    driver = setup_driver()
    url = 'https://www.doctoralia.com.br/clinicas/hospital-erasto-gaertner'
    driver.get(url)

    # Aguardar o carregamento inicial da página
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'floating-cookie-info-btn')))

    # Carregar todas as avaliações
    load_all_reviews(driver)

    # Localizar os elementos de avaliação
    avaliacoes = driver.find_elements(By.CLASS_NAME, 'media.text-break')

    # Verificar se há avaliações para exportar
    if avaliacoes:
        reviews = []
        for avaliacao in avaliacoes:
            review_data = extract_review_data(avaliacao)
            reviews.append(review_data)

        save_reviews_to_excel(reviews)
    else:
        print("Nenhuma avaliação encontrada.")

    # Fechar o driver
    driver.quit()

    # Fim do rastreamento do tempo de execução
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tempo total de execução: {execution_time:.2f} segundos")

# Executar o processo principal
if __name__ == "__main__":
    main()
