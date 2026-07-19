# Fotos del equipo

Guarda aquí una foto por persona con **exactamente** este nombre:

| Fichero | Persona | Rol |
|---|---|---|
| `rogelio-alcaraz.jpg` | Rogelio Alcaraz | Director |
| `andrew-schwartz.jpg` | Andrew Schwartz | Project Manager |
| `luis-paloma.jpg` | Luis Paloma | AI Specialist |
| `massimo-angelini.jpg` | Massimo Angelini | AI Specialist |
| `paula-camprecios.jpg` | Paula Campreciós | AI Specialist |
| `alvaro-entrena.jpg` | Álvaro Entrena | Trainee |

No hace falta que las recortes: sirve cualquier foto (JPG o PNG, mejor si es de 400 px para arriba).

Luego ejecuta desde la raíz del proyecto:

```bash
python3 equipo/procesar.py
```

El script recorta cada foto a cuadrado centrado en la cara, la optimiza a 320×320 y actualiza las tarjetas del equipo en todas las páginas. Quien no tenga foto se queda con su monograma de iniciales.
