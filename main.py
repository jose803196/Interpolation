from interpolate import interpolate
import numpy as np
n = interpolate.orden()
data = interpolate.data(n)
x_data = data[0]
y_data = data[1]

if __name__ == '__main__':
    """cuadratica = interpolate.RCuadratica(n,x_data,y_data)
    resul_cuadratica = cuadratica.resultado()
    #error_cuadratica = cuadratica.seg_miem()
    print(cuadratica)
    #print(error_cuadratica)"""
    lineal = interpolate.RLineal(n,x_data,y_data)
    resultado = lineal.resultado()
    error = lineal.error_est_regre()
    print(resultado)
    print(error)
