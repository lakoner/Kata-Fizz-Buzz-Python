class Fizzbuzz():


    def calculador(self, number: int):
        
            if (number % 15==0):
                return 'fizzbuzz'
            if (number % 3==0):
                return 'Fizz'
            if (number % 5==0):
                return 'Buzz'


            return number


