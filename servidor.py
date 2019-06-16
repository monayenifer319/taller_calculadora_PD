import Pyro4
@Pyro4.expose
class Calculadora(object):
    def somar(self, entrada1, entrada2):
        resultado = entrada1 + entrada2
        return resultado

    def subtrair(self, entrada1, entrada2):
        resultado = entrada1 - entrada2
        return resultado

    def multiplicar(self, entrada1, entrada2):
        resultado = entrada1 * entrada2
        return resultado

    def dividir(self, entrada1, entrada2):
        try:
            resultado = entrada1 / entrada2
            return resultado
        except ZeroDivisionError:
            return "Divisão Inválida"


daemon = Pyro4.Daemon()  # make a Pyro daemon
ns = Pyro4.locateNS()  # find the name server
uri = daemon.register(Calculadora)  # register the greeting maker as a Pyro object
ns.register("juanfe.com", uri)  # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()  # start the event loop of the server to wait for calls