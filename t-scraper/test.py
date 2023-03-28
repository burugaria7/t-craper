import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

driver = webdriver.Chrome()  # WEBブラウザの起動
driver.set_window_size(1200, 1000)


def abc_login(id, pk):
    driver.get('https://app.abceed.com/login')  # 特定のURLへ移動
    # ログインする
    driver.find_element(By.NAME, "email").send_keys(id)
    driver.find_element(By.NAME, "password").send_keys(pk)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[1]/form/div[4]/button").click()
    time.sleep(2)


def abc_deru1000():
    driver.get(
        'https://app.abceed.com/libraries/detail/ask_deru1000/voice/list?'
        'idAlbums=ask_deru1000_test_1_album_1&idAlbums='
        'ask_deru1000_test_2_album_1&from=find-text')  # 特定のURLへ移動

    # ここの移動結構かかる
    time.sleep(4)

    # 文字化け対策
    # 参考URL: https://akiyoko.hatenablog.jp/entry/2017/12/09/010411
    with open('./daru1000.csv', 'w', newline='', encoding='utf-16') as f:
        writer = csv.writer(f, dialect='excel', delimiter='\t', quoting=csv.QUOTE_ALL)
        writer.writerow(
            ['No', 'Title', 'Category', 'Question', 'Option_A', 'Option_B', 'Option_C', 'Option_D', 'Answer',
             'Image_URL'])

    # 1049問分のループ
    for i in range(1049):
        # n問目を読み取る
        driver.find_element(By.ID, "audio-card_" + str(i)).click()
        time.sleep(1)

        title = driver.find_element(By.CLASS_NAME, "question-info_title").text
        category = driver.find_element(By.CLASS_NAME, "question-category").text
        question = driver.find_element(By.CSS_SELECTOR,
                                       "#app > div > div > div.voice-list-wrapper > div.voice-list_commentary > div.voice-list-commentary-component.commentary_content > div > div > div.commentary_body > div > p").text
        option_a = driver.find_element(By.CSS_SELECTOR,
                                       "#app > div > div > div.voice-list-wrapper > div.voice-list_commentary > div.voice-list-commentary-component.commentary_content > div > div > div.commentary_body > div > div:nth-child(3) > div > span").text
        option_b = driver.find_element(By.CSS_SELECTOR,
                                       "#app > div > div > div.voice-list-wrapper > div.voice-list_commentary > div.voice-list-commentary-component.commentary_content > div > div > div.commentary_body > div > div:nth-child(4) > div > span").text
        option_c = driver.find_element(By.CSS_SELECTOR,
                                       "#app > div > div > div.voice-list-wrapper > div.voice-list_commentary > div.voice-list-commentary-component.commentary_content > div > div > div.commentary_body > div > div:nth-child(5) > div > span").text
        option_d = driver.find_element(By.CSS_SELECTOR,
                                       "#app > div > div > div.voice-list-wrapper > div.voice-list_commentary > div.voice-list-commentary-component.commentary_content > div > div > div.commentary_body > div > div:nth-child(6) > div > span").text

        a_class = driver.find_element(By.CSS_SELECTOR,
                                      "#app > div > div > div.voice-list-wrapper > div.voice-list_commentary > div.voice-list-commentary-component.commentary_content > div > div > div.commentary_body > div > div:nth-child(3) > div").get_attribute(
            "class")

        answer = "None"

        if a_class == "marksheet-answer-body__body is-correct":
            answer = "A"
        b_class = driver.find_element(By.CSS_SELECTOR,
                                      "#app > div > div > div.voice-list-wrapper > div.voice-list_commentary > div.voice-list-commentary-component.commentary_content > div > div > div.commentary_body > div > div:nth-child(4) > div").get_attribute(
            "class")
        if b_class == "marksheet-answer-body__body is-correct":
            answer = "B"
        c_class = driver.find_element(By.CSS_SELECTOR,
                                      "#app > div > div > div.voice-list-wrapper > div.voice-list_commentary > div.voice-list-commentary-component.commentary_content > div > div > div.commentary_body > div > div:nth-child(5) > div").get_attribute(
            "class")
        if c_class == "marksheet-answer-body__body is-correct":
            answer = "C"
        d_class = driver.find_element(By.CSS_SELECTOR,
                                      "#app > div > div > div.voice-list-wrapper > div.voice-list_commentary > div.voice-list-commentary-component.commentary_content > div > div > div.commentary_body > div > div:nth-child(6) > div").get_attribute(
            "class")
        if d_class == "marksheet-answer-body__body is-correct":
            answer = "D"
        img_url = driver.find_element(By.CLASS_NAME, "dummy-img").get_attribute("src")

        with open('./daru1000.csv', mode='a', newline='', encoding='utf-16') as f:
            writer = csv.writer(f, dialect='excel', delimiter='\t', quoting=csv.QUOTE_ALL)
            writer.writerow([i, title, category, question, option_a, option_b, option_c, option_d, answer, img_url])

        print("No.", i)
        print("TITLE", title)
        print("CATEGORY", category)
        print("QUESTION", question)
        print("OPTION_A", option_a)
        print("OPTION_B", option_b)
        print("OPTION_C", option_c)
        print("OPTION_D", option_d)
        print("ANSWER", answer)
        print("IMG_URL", img_url)
        print("--------------------")

    time.sleep(5)


if __name__ == "__main__":
    f = open('env.txt', 'r')
    env = f.readlines()
    id = env[0].rstrip('\n')
    pk = env[1].rstrip('\n')
    f.close()

    abc_login(id, pk)

    # No. / title / category / question / option / answer /
    abc_deru1000()
