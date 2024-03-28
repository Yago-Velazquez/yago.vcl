from PIL import Image

# Open the images
image1 = Image.open("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/Control.png")
image2 = Image.open("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/Ampicilina.png")
image3 = Image.open("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/Estreptomicina.png")
image4 = Image.open("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/Conjunto.png")
image5 = Image.open("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/Fases.png")
# Resize the images if needed (optional)
#image1 = image1.resize((720, 288))
#image2 = image2.resize((720, 288))
#image3 = image3.resize((720, 288))
#image4 = image4.resize((432, 288))
#image5 = image5.resize((432, 288))

# Create a blank canvas for the collage
collage_width = max(image1.width + image2.width + image3.width, image4.width * 2 + 10)
collage_height = max(image1.height, image2.height, image3.height, image4.height, image5.height) * 2 + 10

# Create a blank canvas for the collage
collage = Image.new('RGB', (collage_width, collage_height))

# Paste images onto the collage (first row)
x_offset = 0
for img in [image1, image2, image3]:
    collage.paste(img, (x_offset, 0))
    x_offset += img.width + 10  # Add a 10-pixel space between images

# Add a blank space between rows 1 and 2
y_offset = max(image1.height, image2.height, image3.height) + 10  # Add a 10-pixel space
x_offset = 0

# Paste images onto the collage (second row)
for img in [image4]:
    # Resize the image to fit the entire row width
    resized_img = img.resize((collage_width // 2 - 5, img.height))
    collage.paste(resized_img, (x_offset, y_offset))
    x_offset += resized_img.width + 5  # Add a 5-pixel space

# Add a blank space between images 4 and 5
x_offset += 10  # Add a 10-pixel space

for img in [image5]:
    # Resize the image to fit the entire row width
    resized_img = img.resize((collage_width // 2 - 5, img.height))
    collage.paste(resized_img, (x_offset, y_offset))
    x_offset += resized_img.width


# Save the collage
collage.save("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/Figure1.png")


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import linregress

a1 = [0.129, 0.214, 0.346, 0.593, 0.279, 0.109, 0.099, 0.099]
a2 = [0.226, 0.315, 0.534, 0.362, 0.347, 0.291, 0.271, 0.134]
b1 = [0.141, 0.156, 0.373, 0.493, 0.691, 0.856, 1.05, 0.920]
b2 = [0.171, 0.279, 0.377, 0.612, 0.740, 1.003, 1.345, 1.62]
c1 = [0.082, 0.04, 0.004, 0.003, 0.016, 0.015, 0.016, 0.02]
c2 = [0.113, 0.206, 0.34, 0.532, 0.715, 0.914, 1.38, 1.73]
c3 = [0.113, 0.281, 0.445, 0.501, 0.708, 0.932, 1.265, 1.58]
c4 = [0.2, 0.348, 0.462, 0.751, 0.994, 1.865, 1.99, 2.605]
time_standard = [0, 20, 40, 60, 80, 100, 120, 140]
time_special = [20, 40, 60, 80, 108, 120, 140]


def calculate_generation_time(t, a):
# Ajuste de una regresión lineal en escala logarítmica
    log_tiempo = np.log(t)
    log_absorbancia = np.log(a)
    slope, intercept, r_value, p_value, std_err = linregress(log_tiempo, log_absorbancia)
    
    # Calculando el tiempo de generación (duplicación) usando la pendiente de la línea de regresión
    generacion_time = np.log(2) / slope
    
    # Graficando los datos y la línea de regresión
    plt.scatter(t, a, label='Absorbance Data', color="cyan")
    plt.plot(t, np.exp(intercept) * (t ** slope), color='orange', label='Logaritmic Scale Linear Regression')
    
    # Etiquetas y título
    plt.xlabel('Time (minutes)')
    plt.ylabel('Absorbance')
    plt.gcf().set_facecolor('darkgrey')
    plt.legend()
    match len(a):
        case 7:
            plt.title("Generation-Time Regression for Control Groups")
            plt.savefig("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/GenerationTimeControl.png")
        case 6:
            plt.title("Generation-Time Regression for Ampicilin Group 2")
            plt.savefig("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/GenerationTimeAmpicilin2.png")
        case 5:
            if a[0] == 0.612:
                plt.title("Generation-Time Regression for Streptomycin Group 2")
                plt.savefig("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/GenerationTimeStreptomycin2.png")
            else:
                plt.title("Generation-Time Regression for Ampicilin Group 1")
                plt.savefig("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/GenerationTimeAmpicilin1.png")
        case 4:
            plt.title("Generation-Time Regression for Streptomycin Group 1")
            plt.savefig("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/GenerationTimeStreptomycin1.png")
    
    # Mostrar el plot
    plt.show()
    
    return generacion_time
    
c_g = calculate_generation_time(time_standard[1:], list((round((a+b+c+d)/4, 3)) for a, b, c, d in zip(c1[1:], c2[1:], c3[1:], c4[1:])))
a1_g = calculate_generation_time(time_standard[3:], a1[3:])
a2_g = calculate_generation_time(time_standard[2:], a2[2:])
b1_g = calculate_generation_time(time_standard[4:], b1[4:])
b2_g = calculate_generation_time(time_standard[3:], b2[3:])

print(f"Generation time for 'Control' groups: {round(c_g, 3)} minutes")
print(f"Generation time for 'Ampicilin' groups: {round((a1_g + a2_g)/2, 3)} minutes")
print(f"Generation time for 'Streptomycin' groups: {round((b1_g + b2_g)/2, 3)} minutes")


#Tabla mostrando las fases ideales de un cultivo bacteriano
df = pd.read_csv("Microbiology.csv", delimiter=";")
x = df["Time"]
y = df["Number_of_cells"]
plt.plot(x[:37], y[:37], "b-", label="Exponential Phase")
plt.plot(x[36:51], y[36:51], "g-", label="Stationary Phase")
plt.plot(x[50:], y[50:], "r-", label="Death Phase")
plt.title("Bacterial growth")
plt.xlabel("Time (minutes)")
plt.ylabel("Number of cells")
plt.legend(loc="upper left")
plt.gcf().set_facecolor('darkgrey')
plt.savefig("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/Fases.png")
plt.show()


#Tabla de antibiotico A
plt.plot(time_standard, a1, "g--")
plt.plot(time_standard, a2, "g--")
mean_a1_a2 = list((round((x+y)/2, 3)) for x, y in zip(a1, a2))
plt.plot(time_standard, mean_a1_a2, "orange", label="Average: Ampiciln")
plt.xlabel("Time (minutes)")
plt.ylabel("Absorbance")
plt.title("Ampicilin Phases")
plt.scatter(0, 0.129, color='blue', s=25, label="Group 1: Ampiciln")
plt.scatter(0, 0.226, color='red', s=25, label="Group 2: Ampiciln")
plt.scatter(60, 0.593, color='black', s=25, label="Ampicilin application")
plt.scatter(40, 0.534, color='black', s=25)
plt.legend(loc="upper right", fontsize="small")
plt.gcf().set_facecolor('darkgrey')
plt.savefig("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/Ampicilina.png")
plt.show()




#Tabla de antibiotico B
plt.plot(time_standard, b1, "b--")
plt.plot(time_standard, b2, "b--")
mean_b1_b2 = list((round((x+y)/2, 3)) for x, y in zip(b1, b2))
plt.plot(time_standard, mean_b1_b2, "orange", label="Average: Streptomycin")
plt.xlabel("Time (minutes)")
plt.ylabel("Absorbance")
plt.title("Streptomycin Phases")
plt.scatter(0, 0.141, color='blue', s=25, label="Group 1: Streptomycin")
plt.scatter(0, 0.171, color='red', s=25, label="Group 2: Streptomycin")
plt.scatter(80, 0.691, color='black', s=25, label="Streptomycin application")
plt.scatter(60, 0.612, color='black', s=25)
plt.legend(loc="upper left", fontsize="small")
plt.gcf().set_facecolor('darkgrey')
plt.savefig("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/Estreptomicina.png")
plt.show()


#Tabla de control
plt.plot(time_standard, c1, "c--")
plt.plot(time_standard, c2, "c--")
plt.plot(time_standard, c3, "c--")
plt.plot(time_standard, c4, "c--")
mean_control = list((round((a+b+c+d)/4, 3)) for a, b, c, d in zip(c1, c2, c3, c4))
plt.plot(time_standard, mean_control, color="orange", label="Average: Control")
plt.xlabel("Time (minutes)")
plt.ylabel("Absorbance")
plt.title("Control Phases")
plt.scatter(0, 0.082, color='blue', s=25, label="Group 1: Control")
plt.scatter(0, 0.113, color='red', s=25, label="Group 2: Control")
plt.scatter(0, 0.113, color='green', s=25, label="Group 3: Control")
plt.scatter(0, 0.2, color='purple', s=25, label="Group 4: Control")
plt.legend(loc="upper left", fontsize="small")
plt.gcf().set_facecolor('darkgrey')
plt.savefig("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/Control.png")
plt.show()


#Tabla mostrando antibiotico A y B y control
plt.plot(time_standard, c2, "y--", dashes=(5,5), alpha=0.4)
plt.plot(time_standard, c3, "y--", dashes=(5,5), alpha=0.4)
plt.plot(time_standard, c4, "y--", dashes=(5,5), alpha=0.4)
mean_control = list((round((a+b+c)/3, 3)) for a, b, c in zip(c2, c3, c4))
plt.plot(time_standard, mean_control, linewidth=1, color="y", label="Average: Control (minus C1)")
plt.plot(time_standard, b1, "b--", dashes=(5,5), alpha=0.4)
plt.plot(time_standard, b2, "b--", dashes=(5,5), alpha=0.4)
mean_b1_b2 = list((round((x+y)/2, 3)) for x, y in zip(b1, b2))
plt.plot(time_standard, mean_b1_b2, linewidth=1, color="b", label="Average: Streptomycin")
#plt.plot(time_standard, c1, "y--", dashes=(5,5))
plt.plot(time_standard, a1, "r--", dashes=(5,5), alpha=0.4)
plt.plot(time_standard, a2, "r--", dashes=(5,5), alpha=0.4)
mean_a1_a2 = list((round((x+y)/2, 3)) for x, y in zip(a1, a2))
plt.plot(time_standard, mean_a1_a2, linewidth=1, color="red", label="Average: Ampiciln")
plt.xlabel("Time (minutes)")
plt.ylabel("Absorbance")
plt.title("General Overview of Phases")
plt.legend(loc="upper left", fontsize="small")
plt.gcf().set_facecolor('darkgrey')
plt.savefig("/Users/yago.velazquez/Library/CloudStorage/OneDrive-UFV/Universidad/Experimental_Methods_I/Microbiology/Photos/Conjunto.png")
plt.show()