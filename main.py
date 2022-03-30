from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('kivy', 'keyboard_mode', 'systemanddock')
Config.set('kivy', 'window_icon', 'myicon.ico')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
import requests

#from kivy.core.window import Window
#Window.size = (360, 640)


class Container(FloatLayout):
    def resultat(self):
        try:
            pervoegram = float(self.pg.text)
            vtoroegram = float(self.vg.text)
            pervoe = float(self.pr.text)
            vtoroe = float(self.vr.text)
            res = self.res.text
            res2 = self.res2.text
        except:
            pervoegram = 0
            vtoroegram = 0
            pervoe = 0
            vtoroe = 0
            res = 'Ошибка'
            res2 = 'Ошибка'

        if pervoegram < 10:
            pervoegram = pervoegram * 1000
        if vtoroegram < 10:
            vtoroegram = vtoroegram * 1000
        try:
            a = pervoe / pervoegram
            b = vtoroe / vtoroegram
            if a < b:
                d = a * 0.33
                if (a + d) < b and b / (a + d) > 1.05:
                    c = '%s рублей за %s грамм выгоднее,\nчем %s рублей за %s грамм!\nОчень выгодно!' % (
                    pervoe, pervoegram, vtoroe, vtoroegram)
                    e = 'Первый продукт лучше!'
                else:
                    c = '%s рублей за %s грамм выгоднее,\nчем %s рублей за %s грамм!' % (
                    pervoe, pervoegram, vtoroe, vtoroegram)
                    e = 'Первый продукт лучше!'
            elif a == b:
                c = 'У них одинаковая цена'
                e = ""
            else:
                d = b * 0.33
                if (b + d) < a and a / (b + d) > 1.05:
                    c = '%s рублей за %s грамм выгоднее,\nчем %s рублей за %s грамм!\nОчень выгодно!' % (
                    vtoroe, vtoroegram, pervoe, pervoegram)
                    e = 'Второй продукт лучше!'
                else:
                    c = '%s рублей за %s грамм выгоднее,\nчем %s рублей за %s грамм!' % (
                    vtoroe, vtoroegram, pervoe, pervoegram)
                    e = 'Второй продукт лучше!'
            print(c)
            self.res.text = c
            self.res2.text = e
            self.res.color = (0, 0, 0, .9)
            self.img.source = 'face-blowing-a-kiss_1f618.png'
            self.img.color = (1, 1, 1, 1)
        except:
            self.res.text = 'Ошибка'
            self.res2.text = ''
            self.res.color = (1, 0, 0, 1)
            self.img.color = (1, 1, 1, 1)
            self.img.source = 'sad-but-relieved-face_1f625.png'






    def convert(self):
        class CurrencyConverter():
            def __init__(self, url):
                self.data = requests.get(url).json()
                self.currencies = self.data['rates']

            def convert2(self, from_currency, to_currency, amount):
                initial_amount = amount
                # first convert it into USD if it is not in USD.
                # because our base currency is USD
                if from_currency != 'USD':
                    amount = amount / self.currencies[from_currency]

                    # limiting the precision to 4 decimal places
                amount = round(amount * self.currencies[to_currency], 4)
                return amount
        try:
            url = 'https://api.exchangerate-api.com/v4/latest/RUB'
            converter = CurrencyConverter(url)
            z = converter.convert2('RUB', 'KZT', 1)
            try:
                rub = float(self.ru.text)
                self.kurs.text = 'Курс сейчас: %s тенге за 1 рубль' % (z)
                try:
                    self.con.color = (0, 0, 0, .8)
                    self.con.text = str(round(rub * float(z))) + ' тенге'
                except:
                    self.con.text = 'Ошибка'
                    self.con.color = (1, 0, 0, 1)
                    self.kurs.text = 'Курс сейчас: %s тенге за 1 рубль' % (z)
            except:
                self.con.text = 'Ошибка'
                self.con.color = (1, 0, 0, 1)
                self.kurs.text = 'Курс сейчас: %s тенге за 1 рубль' % (z)
        except:
            self.con.text = 'Ошибка'
            self.con.color = (1, 0, 0, 1)
            self.kurs.text = 'Курс сейчас: %s тенге за 1 рубль' % (z)
class MyApp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    MyApp().run()