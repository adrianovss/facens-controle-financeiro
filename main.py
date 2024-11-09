class Initialize():
    def __init__(self):
        self.__transactions = []

    def show_menu(self):
        print(50 * '-')
        print('Bem-vindo ao Controle Financeiro')
        print(50 * '-')
        print('1 - Adicionar transação')
        print('2 - Visualizar transações')
        print('3 - Sair')

    def choose_option(self):
        option = input('\nEscolha uma das opções: ')

        if option not in ['1', '2', '3']:
            print('\nOpção inválida!')

        return option
    
    def to_add(self):
        operation = input('Informar o tipo da operação: ')
        value = input('Informe o valor: ')
        description = input('Informe a descrição: ')

        self.__transactions.append(
            (operation, value, description)
        )

    def to_view(self):
        for transaction in self.__transactions:
            print(f'Operação: {transaction[0]} - \
            Valor: {transaction[1]} - Descrição: {transaction[2]}')

    def to_go_out(self):
        print('\nObrigado, volte sempre!')

if __name__ == '__main__':
    init = Initialize()

    option = ''

    while option != '3':
        init.show_menu()

        option = init.choose_option()

        if option == '1':
            init.to_add()
        elif option == '2':
            init.to_view()
        elif option == '3':
            init.to_go_out()
    