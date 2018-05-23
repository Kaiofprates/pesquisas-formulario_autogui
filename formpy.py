import pyautogui
import sqlite3

def sair():
    cad = pyautogui.confirm(text='Deseja mesmo sair?',title='Formulário',buttons=['sim','não'])
    if (cad == 'sim'):
        pass
    if (cad == 'não'):
        pesq()

def dados(nome,cidade,rua,numero,cep,sex):
    cur = sqlite3.connect('data.db')
    cursor = cur.cursor()
    cursor.execute('create table if not exists users (id integer primary key autoincrement,nome text,cidade text, rua text, numero integer, cep integer, sex text);')
    cursor.execute('insert into users (nome,cidade,rua,numero,cep,sex) values ("{}","{}","{}","{}","{}","{}"); '.format(nome,cidade,rua,numero,cep,sex))
    cur.commit()
    cur.close()

def pesq():
    cad = pyautogui.confirm(text = 'Deseja fazer um novo cadastro?', title = 'formulário',buttons=['sim','não'])
    if (cad == 'não'):
        sair()
    if(cad == 'sim'):
        nome = pyautogui.prompt(text = 'Nome',title = 'Formulário')
        cidade = pyautogui.prompt(text = 'Cidade',title = 'Formulário',default='')
        rua = pyautogui.prompt(text = 'Rua',title = 'Formulário',default='')
        numero = pyautogui.prompt(text = 'Número',title = 'Formulário',default='')
        cep = pyautogui.prompt(text = 'Cep',title = 'Formulário',default='')
        sex = pyautogui.confirm(text='Sexo',title='Formulário',buttons=['Masculino','Feminino'])
        banco = open(nome+'.txt','w')
        banco.write(nome+'\n'+cidade+'\n'+rua+'\n'+numero+'\n'+cep+'\n'+sex+'\n')
        banco.close()
        dados(nome,cidade,rua,numero,cep,sex)
        print('Salvo com sucesso')
pesq()
