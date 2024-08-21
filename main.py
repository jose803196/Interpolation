from package import interpolate
import numpy as np


if __name__ == '__main__':
    n = interpolate.orden()
    data = interpolate.data(n)
    x_data = data[0]
    y_data = np.array(data[1])
    #################### Aproximación de la forma y = ax+b ####################
    Aprox_lineal = interpolate.RLineal(n, x_data, y_data)
    print(interpolate.Aprox_lineal.resultado())
    print(interpolate.Aprox_lineal.error_est_regre())
    #################### Aproximación de la forma y = e^{a+bx} ####################
    """Aprox_exponencial = RExponencial(n, x_data, y_data)
    Aprox_exponencial.matrix_a()
    Aprox_exponencial.ydata_ln()
    print(Aprox_exponencial.resultado())
    print(Aprox_exponencial.error_est_regre())"""
    #################### Aproximación de la forma y = ax^{2} + bx + c ####################
    """Aprox_cuadratica = RCuadratica(n,x_data, y_data)
    Aprox_cuadratica.seg_miem()
    Aprox_cuadratica.pri_miem()
    print(Aprox_cuadratica.resultado())
    print(Aprox_cuadratica.error_est_regre())"""
    #################### Aproximación de la forma y = ax^{3} + bx^{2} + cx + d ####################
    """Aprox_cubica = RCubica(n, x_data, y_data)
    Aprox_cubica.seg_miem()
    Aprox_cubica.pri_miem()
    print(Aprox_cubica.resultado())
    print(Aprox_cubica.error_est_regre())"""
    #################### Aproximación de la forma y = ax^{b} ####################