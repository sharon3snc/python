import random

#catalogo de cuentas
banco= {
}

#cliente
class Cliente ():
    cuentas= {}

    def __init__ (self,nombre, apellido, dni):
        self.nombre= nombre
        self.apellido= apellido
        self.dni= dni
        
    def crear_cuenta(self):
       nueva_cuenta = Cuenta()
       self.cuentas[nueva_cuenta.iban] = nueva_cuenta
       banco[nueva_cuenta.iban] = nueva_cuenta
       return nueva_cuenta.iban

    def depositar_dinero(self,dinero, iban):
        if iban in self.cuentas:
            self.cuentas[iban].añadir_dinero(dinero)
    
    def transferencia(self,dinero,iban_origen, iban_destino):
        if iban_origen in self.cuentas:
            self.cuentas[iban_origen].sacar_dinero(dinero)
            banco[iban_destino].añadir_dinero(dinero)

#cuenta
class Cuenta ():
    def __init__ (self):
        self.dinero= 0
        self.iban= random.randint(10000,20000)
    
    def añadir_dinero(self,dinero):
       self.dinero += dinero
    
    def sacar_dinero(self,dinero):
       self.dinero -=dinero

alvaro= Cliente('alvaro', 'sanchez', '0003')
iban_1 = alvaro.crear_cuenta()
alvaro.depositar_dinero(6000,iban_1)
print(alvaro.cuentas[iban_1].dinero)


pablo= Cliente('pablo', 'ortiz', 67770)
iban_2 = alvaro.crear_cuenta()
print(pablo.cuentas[iban_2].dinero)


alvaro.transferencia(3000,iban_1, iban_2)
print(alvaro.cuentas[iban_1].dinero)
print(pablo.cuentas[iban_2].dinero)
