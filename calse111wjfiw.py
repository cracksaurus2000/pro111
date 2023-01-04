from matplotlib import pyplot
from matplotlib.image import imread

training_infected_image = "./infected/image_1.png"

# cargar los pixeles de la imagen
image = imread(training_infected_image)

pyplot.title("Infectedo: Imagen 1")

# graficar los datos sin procesar de los pixeles
pyplot.imshow(image)

# mostrar la figura
