from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

class YandexRegister:
    def __init__(self, login, password):
        self.browser = webdriver.Edge('')
        self.login = login
        self.password = password

    def _input(self, string, id_param):
        time.sleep(8)
        
        auto_input = self.browser.find_element(By.ID, id_param)
        auto_input.clear()
        auto_input.send_keys(string)
        auto_input.send_keys(Keys.ENTER)


    def register(self):
        try:
            id_list = ['passp-field-login', 'passp-field-passwd']
            user_info = [self.login, self.password]

            self.browser.get('https://passport.yandex.ru/auth/add')
            time.sleep(random.randrange(5,7))
            

            for column in zip(user_info, id_list):
                self._input(column[0], column[1])
           
            time.sleep(random.randrange(15,17))
            self.browser.close()
            self.browser.quit()

        except Exception as ex:
            print(ex)
            self.browser.close()
            self.browser.quit()


    

if __name__ == '__main__':
    test = YandexRegister(input('Введите логин: '), input('Введите пароль: '))
    test.register()