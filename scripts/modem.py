import numpy as np
import matplotlib.pyplot as plt

def start():
    archivo = "BLOCK2_NLCG_036.rho"

    with open(archivo, "r") as f:
        lineas = f.readlines()

    nx, ny, nz, _, escala = lineas[1].split()
    nx, ny, nz = int(nx), int(ny), int(nz)

    dx = np.fromstring(lineas[2], sep=" ")
    dy = np.fromstring(lineas[3], sep=" ")
    dz = np.fromstring(lineas[4], sep=" ")

    x = np.concatenate(([0], np.cumsum(dx)))
    y = np.concatenate(([0], np.cumsum(dy)))
    z = np.concatenate(([0], np.cumsum(dz)))

    valores = np.fromstring(" ".join(lineas[5:]), sep=" ")
    if len(valores) == nx * ny * nz + 4 and np.all(valores[-4:] == 0):
        valores = valores[:-4]

    print("Dimensiones:", nx, ny, nz)
    print("Valores leídos:", len(valores))
    print("Valores esperados:", nx * ny * nz)
    print("Últimos 10 valores:", valores[-10:])

    modelo = valores.reshape((nz, ny, nx))

    if escala == "LOGE":
        modelo = np.exp(modelo)

    print("Dimensiones:", nx, ny, nz)
    print("Resistividad mínima:", modelo.min(), "ohm·m")
    print("Resistividad máxima:", modelo.max(), "ohm·m")

    perfil = modelo[:, ny // 2, :]

    plt.figure(figsize=(10, 6))

    plt.pcolormesh(
        x, z,
        perfil,
        shading="flat",
        cmap="turbo",
        norm=plt.matplotlib.colors.LogNorm()
    )
    plt.gca().invert_yaxis()
    plt.xlabel("Distancia X (m)")
    plt.ylabel("Profundidad (m)")

    plt.colorbar(label="Resistividad (ohm·m)")
    plt.xlabel("Celda X")
    plt.ylabel("Capa de profundidad")
    plt.title("ModEM: perfil vertical central")
    plt.tight_layout()
    plt.savefig("perfil_modem.png", dpi=200)
    plt.show()

    plt.figure(figsize=(9, 7))
    plt.pcolormesh(
        x, y,
        modelo[0, :, :],
        shading="flat",
        cmap="turbo",
        norm=plt.matplotlib.colors.LogNorm()
    )
    plt.xlabel("Distancia X (m)")
    plt.ylabel("Distancia Y (m)")

    plt.colorbar(label="Resistividad (ohm·m)")
    plt.xlabel("Celda X")
    plt.ylabel("Celda Y")
    plt.title("ModEM: mapa horizontal de la primera capa")
    plt.tight_layout()
    plt.savefig("mapa_modem.png", dpi=200)
    plt.show()

