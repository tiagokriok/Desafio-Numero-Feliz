class checkHappy():
    """
    PT-BR: Verifica se é um  número feliz.
    Para um número ser considerado feliz, temos que obter o quadrado de cada digito desse número, e fazer a soma desses resultados.
    A seguir realizar o mesmo procedimento novamente com o valor do resultado da soma.
    Se ao repetir o procedimento várias vezes e obtivermos o valor 1, o número é considerado feliz
    EN: Check if is a Happy Number.
    For a number to be considered happy, you get or get the square of each digit of that number and make a sum of those results.
    Then follow the same procedure again with the sum result value.
    If you repeat the procedure several times and get the value 1, the number is considered happy.
    """
    
    def isHappy(self, number):
        """
        PT-BR: Retorna True se o número for feliz e False se o número for triste.
        EN: Returns True if is a happy number and False if is a sad number.
        """
        number = str(number)

        happy = 0

        for num in number:
            happy += int(num)**2

        if happy == 1:
            return True
        elif happy < 10:
            return False
        else:
            happy_obj = checkHappy()
            return happy_obj.isHappy(happy)
