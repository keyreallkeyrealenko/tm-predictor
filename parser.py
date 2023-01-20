from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from Bio import SeqIO


def parse(path_to_file: str) -> tuple:
    correct_letters = 'CDSQKIPTFNGHLRWAVEYM'
    url = 'http://tm.life.nthu.edu.tw/index.htm'
    parser = SeqIO.parse(path_to_file, 'fasta')

    categories = {}
    total_tm_index = []
    names_by_categories = {}
    gene_index = {}

    for element in parser:
        sequence = str(element.seq)
        name = str(element.name)
        if not all(map(lambda x: x.upper() in correct_letters, sequence)):
            sequence = ''.join(list(filter(lambda x: x.upper() in correct_letters, sequence)))

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        with webdriver.Chrome(options=chrome_options) as browser:
            browser.get(url)
            browser.find_element(By.ID, "seq").send_keys(sequence)
            button = browser.find_element(By.XPATH, "//input[@type='submit']")
            button.click()
            values = browser.find_elements(By.XPATH,
                                           "//table[@width='700']//tr[@bgcolor='#FFFFFF']//font[@face='Arial, "
                                           "Helvetica, sans-serif']")
            tm_index = float(values[-3].text)
            cat = values[-1].text

        if cat not in names_by_categories:
            names_by_categories[cat] = [name]
        else:
            names_by_categories[cat].append(name)

        gene_index[name] = tm_index
        total_tm_index.append(tm_index)
        categories[cat] = categories.get(cat, 0) + 1

    return names_by_categories, total_tm_index, categories, gene_index
