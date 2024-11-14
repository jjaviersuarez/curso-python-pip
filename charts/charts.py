import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A','B','C']
    values = [200, 34, 120]
    
    fig, ax = plt.subplots() #aquí se obtiene la figura y las coordenadas
    ax.pie(values, labels=labels) #generamos un gráfico Pie, enviamos los valores y los labels
    plt.savefig('pie.png') #guardar una figura como imagen
    plt.close() #cerramos
    