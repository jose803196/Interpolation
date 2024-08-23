from interpolate import interpolate
import numpy as np
n = interpolate.orden()
data = interpolate.data(n)
x_data = data[0]
y_data = data[1]

if __name__ == '__main__':
    lineal = interpolate.RLineal(n,x_data,y_data)
    resul_lineal = lineal.resultado()
    error_lineal = lineal.error_est_regre()
    print(resul_lineal)
    print(error_lineal)