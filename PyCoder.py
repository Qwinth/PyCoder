from PySide import QtCore, QtGui
import sys
from UI import Ui_MainWindow
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
num = 0
letter = []
decode_word = ''
code_table = {"А":1,
              "а":2,
              "Б":3,
              "б":4,
              "В":5,
              "в":6,
              "Г":7,
              "г":8,
              "Д":9,
              "д":10,
              "Е":11,
              "е":12,
              "Ё":13,
              "ё":14,
              "Ж":15,
              "ж":16,
              "З":17,
              "з":18,
              "И":19,
              "и":20,
              "Й":21,
              "й":22,
              "К":23,
              "к":24,
              "Л":25,
              "л":26,
              "М":27,
              "м":28,
              "Н":29,
              "н":30,
              "О":31,
              "о":32,
              "П":33,
              "п":34,
              "Р":35,
              "р":36,
              "С":37,
              "с":38,
              "Т":39,
              "т":40,
              "У":41,
              "у":42,
              "Ф":43,
              "ф":44,
              "Х":45,
              "х":46,
              "Ц":47,
              "ц":48,
              "Ч":49,
              "ч":50,
              "Ш":51,
              "ш":52,
              "Щ":53,
              "щ":54,
              "Ъ":55,
              "ъ":56,
              "Ы":57,
              "ы":58,
              "Ь":59,
              "ь":60,
              "Э":61,
              "э":62,
              "Ю":63,
              "ю":64,
              "Я":65,
              "я":66,
              "І":67,
              "і":68,
              "Є":69,
              "є":70,}

decode_table = {1:"А",
              2:"а",
              3:"Б",
              4:"б",
              5:"В",
              6:"в",
              7:"Г",
              8:"г",
              9:"Д",
              10:"д",
              11:"Е",
              12:"е",
              13:"Ё",
              14:"ё",
              15:"Ж",
              16:"ж",
              17:"З",
              18:"з",
              19:"И",
              20:"и",
              21:"Й",
              22:"й",
              23:"К",
              24:"к",
              25:"Л",
              26:"л",
              27:"М",
              28:"м",
              29:"Н",
              30:"н",
              31:"О",
              32:"о",
              33:"П",
              34:"п",
              35:"Р",
              36:"р",
              37:"С",
              38:"с",
              39:"Т",
              40:"т",
              41:"У",
              42:"у",
              43:"Ф",
              44:"ф",
              45:"Х",
              46:"х",
              47:"Ц",
              48:"ц",
              49:"Ч",
              50:"ч",
              51:"Ш",
              52:"ш",
              53:"Щ",
              54:"щ",
              55:"Ъ",
              56:"ъ",
              57:"Ы",
              58:"ы",
              59:"Ь",
              60:"ь",
              61:"Э",
              62:"э",
              63:"Ю",
              64:"ю",
              65:"Я",
              66:"я",
              67:"І",
              68:"і",
              69:"Є",
              70:"є",}
def GetCodingText(text):
    global letter_list
    letter_list = list(text)
    global num
    global decode_word
    num = 0
    decode_word = ''
    print(letter_list)
ui.lineEdit.textChanged.connect(GetCodingText)

def Coding():
        while True:
            
            try:
                global num
                num_text = code_table[letter_list[num]]
                global decode_word
                num = num + 1
                num_letter = 71 - num_text
                decode_letter = decode_table[num_letter]
                decode_word = decode_word + decode_letter
            except IndexError:
                print(decode_word)
                ui.lineEdit_2.setText(decode_word)
                break
            except KeyError:
             	coding = ord(letter_list[num])
             	num = num + 1
             	coding = 158 - coding
             	coded = chr(coding)
             	decode_word = str(decode_word) + coded
ui.pushButton.clicked.connect(Coding)

sys.exit(app.exec_())
