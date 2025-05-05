import numpy as np
import math
from numpy.linalg import solve, inv
from numpy import transpose
from numpy import matmul
import matplotlib.pyplot as plt

def orden():
    while True:
        n_1 = input("Número de puntos: ")
        try:
            n = int(n_1)
            if n > 1:
                return n
            else:
                print("Debe ingresar un número mayor a 1.")
        except ValueError:
            print("Debe ingresar números.")

def data(n):
    data = [[], []]
    for i in range(2):
        for j in range(n):
            prompt = f"Valor de {'X' if i == 0 else 'Y'}[{j+1}]: "
            while True:
                try:
                    value = float(input(prompt))
                    if i == 1 and value <= 0:  # Para modelos como exponencial/potencia
                        print("Y debe ser positivo.")
                        continue
                    data[i].append(value)
                    break
                except ValueError:
                    print("Debe ingresar números.")
    # Verificar que los valores de x sean únicos
    if len(set(data[0])) != n:
        raise ValueError("Los valores de X deben ser únicos.")
    return data

class RLineal:
    # General form:  y = mx + b
    def __init__(self, n, x_data, y_data):
        self.n = n
        self.x_data = x_data
        self.y_data = y_data
        self.R = []
        self.acumulacion = 0

    def resultado(self):
        var_1 = sum(self.x_data)
        var_2 = sum(x**2 for x in self.x_data)
        var_3 = sum(self.y_data)
        var_4 = sum(x*y for x, y in zip(self.x_data, self.y_data))
        denominator = var_1**2 - self.n * var_2
        if abs(denominator) < 1e-10:  # Evitar división por cero
            raise ValueError("Los datos no permiten calcular una regresión lineal (denominador cercano a cero).")
        pen_diente = (var_1 * var_3 - self.n * var_4) / denominator
        corte_ordenada = (var_1 * var_4 - var_2 * var_3) / denominator
        self.R = [pen_diente, corte_ordenada]
        return self.R

    def plot(self):
        plt.scatter(self.x_data, self.y_data, color='blue', label='Datos')
        x_fit = np.linspace(min(self.x_data), max(self.x_data), 100)
        y_fit = self.R[0] * x_fit + self.R[1]
        plt.plot(x_fit, y_fit, color='red', label='Ajuste lineal')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.show()

    def error_est_regre(self):
        mse = 0
        for i in range(self.n):
            y_prima = self.R[0] * self.x_data[i] + self.R[1]
            mse += (self.y_data[i] - y_prima) ** 2
        return mse / self.n  # Error cuadrático medio

class RExponencial:
    # General form:  y = {e}**{mx+b}
    def __init__(self, n, x_data, y_data):
        if any(y <= 0 for y in y_data):
            raise ValueError("Los valores de Y deben ser positivos para la regresión exponencial.")
        self.n = n
        self.x_data = x_data
        self.y_data = y_data
        self.acumulacion = 0
        self.V = []
    
    def resultado(self,n):
        self.n = n
        b, a = 0, 0
        var_1,var_2,var_3,var_4 = 0,0,0,0
        for i in range(self.n):
            var_1 += (self.x_data[i])*(math.log(self.y_data[i],math.e))
            var_2 += self.x_data[i]
            var_3 += math.log(self.y_data[i],math.e)
            var_4 += (self.x_data[i])**(2)

        b = ((n*var_1)-(var_2)*(var_3))/((n*var_4) - (var_2)**(2))  #Punto de corte con la ordenada
        self.V.append(b)                            
        a = (1/self.n)*((var_3) - (b) * (var_2))                    #Pendiente de la ecuación
        self.V.append(a)            
        return(self.V)
    
    def error_est_regre(self):
        for i in range(self.n):
            y_prima = math.exp(self.V[0]+((self.V[1])*(self.x_data[i])))
            self.acumulacion += math.fabs((self.y_data[i] - y_prima)/(self.y_data[i]))*(100)
        A_prima = (1/self.n)*(self.acumulacion)
        return(A_prima)
    
class RCuadratica:
    # General form:  y = a{x}**{2} + b*x + c
    def __init__(self, n, x_data, y_data):
        if any(y <= 0 for y in y_data):
            raise ValueError("Los valores de Y deben ser positivos para la regresión exponencial.")
        self.n = n
        self.x_data = x_data
        self.y_data = y_data
        self.acumulacion = 0
        self.V = []
    
    def seg_miem(self):
        var_1 = 0
        var_2 = 0
        var_3 = 0
        for i in range(self.n):
            var_1 += self.y_data[i]
            var_2 += (self.x_data[i])*(self.y_data[i])
            var_3 += ((self.x_data[i])**(2))*(self.y_data[i])
        self.x.append(var_1)
        self.x.append(var_2)
        self.x.append(var_3)
        return(np.array(self.x))
    
    def pri_miem(self):
        var_4 = 0
        var_3 = 0
        var_2 = 0
        var_1 = 0
        for i in range(self.n):
            var_1 += self.x_data[i]
            var_2 += (self.x_data[i])**(2)
            var_3 += (self.x_data[i])**(3)
            var_4 += (self.x_data[i])**(4)
        
        self.A = [[var_2, var_1, self.n],[var_3, var_2, var_1],[var_4, var_3, var_2]]
        return(np.array(self.A))
                    
    def resultado(self):
        self.resultado = solve(np.array(self.A), np.array(self.x))
        return(self.resultado)
    
    def error_est_regre(self):
        for i in range(self.n):
            y_prima = (self.resultado[0])*((self.x_data[i])**(2)) + (self.resultado[1])*(self.x_data[i]) + self.resultado[2]
            self.acumulacion += math.fabs((self.y_data[i] - y_prima)/(self.y_data[i]))*(100)
        A_prima = (1/self.n)*(self.acumulacion)
        return(A_prima)

class RCubica:
    # General form:  y = a{x}**{3} + b{x}**{2} + c*x + d
    def __init__(self, n, x_data, y_data):
        self.n = n
        self.x_data = x_data
        self.y_data = y_data
        self.acumulacion = 0
        self.x = []
    
    def seg_miem(self):
        var_1 = 0
        var_2 = 0
        var_3 = 0
        var_4 = 0
        for i in range(self.n):
            var_1 += self.y_data[i]
            var_2 += (self.x_data[i])*(self.y_data[i])
            var_3 += ((self.x_data[i])**(2))*(self.y_data[i])
            var_4 += ((self.x_data[i])**(3))*(self.y_data[i])
        self.x.append(var_1)
        self.x.append(var_2)
        self.x.append(var_3)
        self.x.append(var_4)
        return(np.array(self.x))

    def pri_miem(self):
        var_6 = 0
        var_5 = 0
        var_4 = 0
        var_3 = 0
        var_2 = 0
        var_1 = 0
        for i in range(self.n):
            var_1 += self.x_data[i]
            var_2 += (self.x_data[i])**(2)
            var_3 += (self.x_data[i])**(3)
            var_4 += (self.x_data[i])**(4)
            var_5 += (self.x_data[i])**(5)
            var_6 += (self.x_data[i])**(6)
        
        self.A = [[var_3,var_2,var_1, self.n],[var_4,var_3, var_2,var_1],[var_5,var_4,var_3,var_2],[var_6,var_5,var_4,var_3]]
        return(np.array(self.A))
    
    def resultado(self):
        self.resultado = solve(self.A, self.x)
        return(self.resultado)
    
    def error_est_regre(self):
        for i in range(self.n):
            y_prima = (self.resultado[0])*((self.x_data[i])**(3)) + (self.resultado[1])*((self.x_data[i])**(2)) + (self.resultado[2])*(self.x_data[i]) + self.resultado[3]
            self.acumulacion += math.fabs((self.y_data[i] - y_prima)/(self.y_data[i]))*(100)

        A_prima = (1/self.n)*(self.acumulacion)
        return(A_prima)

class RPotencia:
    # General form:  y = a{x}**{b}
    def __init__(self, n, x_data, y_data):
        self.n = n
        self.x_data = x_data
        self.y_data = y_data
        self.acumulacion = 0
        self.R =[]
    
    def resultado(self):
        a, b = 0,0                              #Parametros para la ecuación
        var_1, var_2, var_3, var_4 = 0,0,0,0
        for i in range(self.n):
            var_1 += (math.log(self.x_data[i],math.e))*(math.log(self.y_data[i],math.e))
            var_2 += math.log(self.x_data[i],math.e)
            var_3 += math.log(self.y_data[i],math.e)
            var_4 += (math.log(self.x_data[i],math.e))**(2)
        b = ((self.n)*(var_1) - (var_2)*(var_3))/((self.n)*(var_4) - (var_2)**(2))  #Parametro b
        self.R.append(b)
        a = math.exp((1/self.n)*((var_3)*(b*var_2)))                                  #Parametro a
        self.R.append(a)
        return (self.R)
    
    def error_est_regre(self):
        for i in range(self.n):
            y_prima = (self.R[1])*((self.x_data[i])**(self.R[0]))
            self.acumulacion += math.fabs((self.y_data[i] - y_prima)/(self.y_data[i]))*(100)
        A_prima = (1/self.n)*(self.acumulacion)
        return(A_prima)

class RHiperbolica:
    #General form: a + \frac{b}{x}
    def __init__(self, n, x_data, y_data):
        self.n = n
        self.x_data = x_data
        self.y_data = y_data
        self.acumulacion = 0
        self.R =[]

    def resultado(self):
        a, b = 0,0
        var_1, var_2, var_3, var_4 = 0,0,0,0
        for i in range(self.n):
            var_1 += (self.y_data[i])/(self.x_data[i])
            var_2 += (1)/(self.x_data[i])
            var_3 += self.y_data[i]
            var_4 += (1)/((self.x_data[i])**(2))

        b = ((self.n)*(var_1) -(var_2)*(var_3))/((self.n)*(var_4)-(var_2)**(2))
        self.R.append(b)
        a = (1/self.n)*(var_3 - (b)*(var_2))
        self.R.append(a)
        return(self.R)
    
    def error_est_regre(self):
        for i in range(self.n):
            y_prima = (self.R[1]) + ((self.R[0])/(self.x_data[i]))
            self.acumulacion += math.fabs((self.y_data[i] - y_prima)/(self.y_data[i]))*(100)
        A_prima = (1/self.n)*(self.acumulacion)
        return(A_prima)
    
class RLogaritmica():
    #General form: a + b* ln(x)
    def __init__(self, n, x_data, y_data):
        self.n = n
        self.x_data = x_data
        self.y_data = y_data
        self.acumulacion = 0
        self.R =[]

    def resultado(self):
        a,b = 0,0
        var_1, var_2, var_3, var_4 = 0,0,0,0
        for i in range(self.n):
            var_1 += (self.y_data[i])*(math.log(self.x_data[i], math.e))
            var_2 += math.log(self.x_data[i], math.e)
            var_3 += self.y_data[i]
            var_4 += (math.log(self.x_data[i], math.e))**(2)

        b = ((self.n)*(var_1) - (var_2)*(var_3))/((self.n)*(var_4) -(var_2)**(2))
        self.R.append(b)
        a = (1/self.n)*(var_3 - (b)*(var_2))
        self.R.append(a)
        return(self.R)
    
    def error_est_regre(self):
        for i in range(self.n):
            y_prima = self.R[1] + (self.R[0])*(math.log(self.x_data[i],math.e))
            self.acumulacion += math.fabs((self.y_data[i] - y_prima)/(self.y_data[i]))*(100)
        A_prima = (1/self.n)*(self.acumulacion)
        return(A_prima)

if __name__ == '__main__':
    n = orden()
    data = data(n)
    x_data = data[0]
    y_data = data[1]
    lineal = RCuadratica(n,x_data,y_data)
    resultado = lineal.resultado()
    error = lineal.error_est_regre()
    print(resultado)
    print(error)