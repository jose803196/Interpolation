import numpy as np
import math
from numpy.linalg import solve, inv
from numpy import transpose
from numpy import matmul

def orden():
    pass
    s = True
    while(s == True):
        n_1 = input("Numeros de puntos: ")
        try:
            n = int(n_1)
            if n >1:
                return(n)
                s = False
            else:
                pass
        except ValueError:
            print("Debe ingresar numeros.")

def data(n):
    data = []
    for i in range(2):
        lista_aux = []
        for j in range(n):
            if i == 0:
                s = True
                while(s == True):
                    x_1 = input("Valor de X[{}]: ".format(j+1))
                    try:
                        x = float(x_1)
                        lista_aux.append(x)
                        s = False
                    except ValueError:
                        print("Debe ingresar numeros.")
            else:
                s = True
                while(s == True):
                    y_1 = input("Valor de Y[{}]: ".format(j+1))
                    try:
                        y = float(y_1)
                        lista_aux.append(y)
                        s = False
                    except ValueError:
                        print("Debe ingresar numeros.")
        data.append(lista_aux)
    return(data)

class RLineal:
    def __init__(self, n, x_data, y_data):
        self.n = n
        self.x_data = x_data
        self.y_data = y_data
        self.R = []
        self.acumulacion = 0

    def resultado(self):
        var_1 = 0
        var_2 = 0
        var_3 = 0
        var_4 = 0
        for i in range(self.n):
            var_1 += self.x_data[i]
            var_2 += (self.x_data[i])**(2)
            var_3 += self.y_data[i]
            var_4 += (self.x_data[i])*(self.y_data[i])
        pen_diente = (((var_1)*(var_3))-((self.n)*(var_4)))/((var_1)**(2)-((self.n)*(var_2)))
        self.R.append(pen_diente)
        corte_ordenada = (((var_1)*(var_4))-((var_2)*(var_3)))/((var_1)**(2)-((self.n)*(var_2)))
        self.R.append(corte_ordenada)
        return(self.R)

    def error_est_regre(self):
        for i in range(self.n):
            y_prima = ((self.R[0])*(self.x_data[i]))+(self.R[1])
            self.acumulacion += math.fabs((self.y_data[i] - y_prima)/(self.y_data[i]))*(100)
        A_prima = (1/self.n)*(self.acumulacion)
        return(A_prima)

class RExponencial:
    def __init__(self, n, x_data, y_data):
        self.n = n
        self.x_data = x_data
        self.y_data = y_data
        self.A = []
        self.y_data_ln = []
        self.acumulacion = 0

    def matrix_a(self):
        for i in range(self.n):
            lista_aux = []
            for j in range(2):
                if j == 0:
                    lista_aux.append(1)
                else:
                    lista_aux.append(int(self.x_data[i]))
            self.A.append(lista_aux)
        return(np.array(self.A))
    
    def ydata_ln(self):
        for i in range(self.n):
            y_ln = math.log(self.y_data[i])
            self.y_data_ln.append(y_ln)
        return(self.y_data_ln)
    
    def resultado(self):
        self.A_t = transpose(self.A)
        u = matmul(self.A_t, self.A)
        u_inv = inv(u)
        w = matmul(self.A_t, self.y_data_ln)
        self.V = matmul(u_inv, w)
        return(self.V)
    
    def error_est_regre(self):
        for i in range(self.n):
            y_prima = math.exp(self.V[0]+((self.V[1])*(self.x_data[i])))
            self.acumulacion += math.fabs((self.y_data[i] - y_prima)/(self.y_data[i]))*(100)
        A_prima = (1/self.n)*(self.acumulacion)
        return(A_prima)
    
class RCuadratica:
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
        self.resultado = solve(self.A, self.x)
        return(self.resultado)
    
    def error_est_regre(self):
        for i in range(self.n):
            y_prima = (self.resultado[0])*((self.x_data[i])**(2)) + (self.resultado[1])*(self.x_data[i]) + self.resultado[2]
            self.acumulacion += math.fabs((self.y_data[i] - y_prima)/(self.y_data[i]))*(100)
        A_prima = (1/self.n)*(self.acumulacion)
        return(A_prima)

class RCubica:
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

"""class RPotencia:
    def __init__(self, n, x_data, y_data):
        self.n = n
        self.x_data = x_data
        self.y_data = y_data
        self.acumulacion = 0"""