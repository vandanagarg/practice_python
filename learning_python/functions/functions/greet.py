#calling functions

name = 'A global string'

def greet():

    # name = 'Vandana'

    def hello():

        #name = 'I am local'

        print('Hello ' +  name)
    hello()

greet()

