

class OpenTokenErrors(BaseException) :
    def __init__(self, *args) :
        if args :
            self.message = args[0]
        else :
            self.message = None

    def __str__(self) :
        if self.message :
            return(f"Sorry, {self.message }")
        else :
            return("Error with yandex")



class YandexErrors(BaseException) :
    def __init__(self, *args) :
        if args :
            self.message = args[0]
        else :
            self.message = None

    def __str__(self) :
        if self.message :
            return(f"Sorry, {self.message }")
        else :
            return("Error with yandex")








