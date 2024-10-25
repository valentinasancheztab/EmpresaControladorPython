
#puedes entrar y modificar los atributos de la instancia actual
class Empleado:
    def __init__(self, nombre: str, edad: int, departamento: str, anio_contratacion: int): #puedes entrar y modificar los atributos de la instancia actual
        self.nombre = nombre #es un atributo de la instancia de empleado
        self.edad = edad
        self.departamento = departamento
        self.anio_contratacion = anio_contratacion

#métodos de acceso que devuelven los atributos correspondientes del objeto.
    def get_nombre(self) -> str: #le asignamos a nombre un tipo string que esto significa una cadena de caracteres
        return self.nombre #le asignamos a nombre un tipo string que esto significa una cadena de caracteres

    def get_edad(self) -> int: # le asignamos a edad un tipo int que esto son numeros enteros, o sea 0 y no 0.0
        return self.edad #"retornamos" la variable "edad"  esta linea se encarga de dar la edad de "empleado"

    def get_departamento(self) -> str:
        return self.departamento

    def get_anio_contratacion(self) -> int:
        return self.anio_contratacion

    def calcular_antiguedad(self) -> int:
        return 2024 - self.anio_contratacion  #calcula los años que lleva en el trabajo, usa el año actual - el año en que fue contratado

# devuelve un diccionario que representa la información relevante del objeto, incluyendo sus atributos y un cálculo de la antigüedad, facilitando así la visualización y el uso de los datos del objeto en otras partes de la aplicación.
    def toString(self): #toString este método se utiliza para definir la forma de cadena de un objeto
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "departamento": self.departamento,
            "anio_contratacion": self.anio_contratacion,
            "antiguedad": self.calcular_antiguedad()
        }

    def __str__(self):
        return f"Empleado{{nombre='{self.nombre}', edad={self.edad}, departamento='{self.departamento}', antigüedad={self.calcular_antiguedad()}}}"  #retorna el modelo completo de empleado
