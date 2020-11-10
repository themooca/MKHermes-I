from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import datetime
import time
import openpyxl as excel

# função pra ler os contatos
def readContacts(fileName):
    lst = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    firstCol = sheet['A']
    for cell in range(len(firstCol)):
        contact = str(firstCol[cell].value)
        contact = "\"" + contact + "\""
        lst.append(contact)
    return lst

targets = readContacts("contatos.xlsx")
print(targets)
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 3.5)
wait5 = WebDriverWait(driver, 1.25)
input("Escaneie o QR code e pressione enter")

msgToSend = [
                [16, 30, 0, "Morte a todos grandes capitalistas" + Keys.SHIFT + Keys.ENTER + Keys.SHIFT + "Isso daqui é um belo e grande teeste, aprenda olhando como funciona os padrões" + Keys.SHIFT + Keys.ENTER + Keys.SHIFT + "https://www.youtube.com/watch?v=zuWwLDZ3x2M" + Keys.ENTER + "Ah, tu em vez de usar o geckodriver (firefox) tu pode usar o chromium, porém eu não recomendo, o chromium trava com emojis (sério)" + Keys.SHIFT + Keys.ENTER + Keys.SHIFT + "https://www.youtube.com/watch?v=8HrMWL2q4vo ENQUANTO O MUNDO EXPLODE O CURUPIRA JÁ TEM SEU TENIS IMPORTADO!"]
            ]

count = 0
while count<len(msgToSend):

    # Identificador de hora (desativado)
    curTime = datetime.datetime.now()
    curHour = curTime.time().hour
    curMin = curTime.time().minute
    curSec = curTime.time().second

    # configuração pra iniciar automaticamente
    if 0 == 0:
        # variaveis de sucesso e fracasso
        success = 0
        sNo = 1
        failList = []

        # Loop para achar o contato e mandar a mensagem
        for target in targets:
            print(sNo, ". O Alvo é: " + target)
            sNo+=1
            try:
                # escolhendo o alvo
                x_arg = '//span[contains(@title,' + target + ')]'
                try:
                    wait5.until(EC.presence_of_element_located((
                        By.XPATH, x_arg
                    )))
                except:
                    print('Espere 0.001 segundo')
                    sleep(0.001)
                    busca = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
                    busca.clear()
                    busca.send_keys(target.replace('"', ''))


                # selecionando o alvo
                print('Espere 7.2 segundos... ')
                sleep(7.2)
                driver.find_element_by_xpath(x_arg).click()
                print("Target Successfully Selected")
                time.sleep(2.5)

                # selecionando a caixa de texto
                inp_xpath = "//div[@spellcheck='true']"
                input_box = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath)))
                time.sleep(1.2)

                # mandando mensagem
                input_box.send_keys(msgToSend[count][3])
                time.sleep(4.1)
                input_box.send_keys(Keys.ENTER)
                print("Enviado com sucesso para: "+ target + '\n')
                success+=1
                time.sleep(0.5)

            except:
                # se falhar, add o nome na lista de falhas
                print("Não foi possivel achar o: " + target)
                failList.append(target)
                pass

        print("\nCorretamente enviado à: ", success)
        print("Houve erro no envio a: ", len(failList))
        print(failList)
        print('\n\n')
        count+=1
driver.quit()
