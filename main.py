# imports
import re
import time
from validate_docbr import CPF


class Matricula:

    def __init__(self, nome, telefone, cpf, email):
        self.nome = nome

        if self.valida_tel(telefone):
            self.telefone = telefone
        else:
            raise ValueError('Número inválido')

        if self.valida_cpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError('Cpf inválido')

        if self.valida_email(email):
            self.email = email
        else:
            raise ValueError('Email inválido')

    def __str__(self):
        return self.__format__(Matricula)

    # Validação email
    def valida_email(self, email):
        padrao = '(\w{3,50})(@)(\w{5,10})(.\w{2,3})(.\w{2,3})?'
        modelo = re.search(padrao, email)
        return modelo

    # Validação cpf
    def valida_cpf(self, cpf):
        doc_cpf = CPF()
        return doc_cpf.validate(cpf)

    # Validação telefone
    def valida_tel(self, tel):
        padrao = '([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        modelo = re.search(padrao, tel)
        return modelo

    def __format__(self, format_spec):
        # mask/CPF
        doc_cpf = CPF()
        documento = doc_cpf.mask(self.cpf)

        # Regex Telefone
        padrao = '([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        modelo = re.search(padrao, self.telefone)

        # Exibição
        if len(self.telefone) <= 11:
            format_tel = '({}){}-{}'.format(modelo.group(2), modelo.group(3), modelo.group(4))
            format_spec = f'Nome: {self.nome}, Tel: {format_tel}, CPF:{documento}, Email:{self.email}'
        else:
            format_tel = '+{} ({}){}-{}'.format(modelo.group(1), modelo.group(2), modelo.group(3), modelo.group(4))
            format_spec = f'Nome: {self.nome}, Tel: {format_tel}, CPF:{documento}, Email:{self.email}'
        return format_spec


# Programa
nome = input('Insira seu nome: ')
telefone = input('Insira seu telefone: ')
cpf = input('Insira seu cpf: ')
email = input('Insira seu email: ')
mat = Matricula(nome, telefone, cpf, email)
time.sleep(1.5)
print('-' * 110)
print(mat)
print('-' * 110)
