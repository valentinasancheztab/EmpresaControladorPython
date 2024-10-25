from modelos.empleado import Empleado

class EmpleadoPorHoras(Empleado): # Define una clase llamada EmpleadoPorHoras que hereda de la clase Empleado.
    def __init__(self, nombre, edad, departamento, anio_contratacion, tarifa_hora, horas_trabajadas):
#esta línea define el constructor de la clase EmpleadoPorHoras, toma varios parámetros para inicializar los atributos de una instancia de la clase.
        super().__init__(nombre, edad, departamento, anio_contratacion) #Llama al constructor de la clase base (Empleado) utilizando 'super()',
#self: permite a las instancias de las clases acceder y manipular sus propios atributos y métodos
        self.tarifa_hora = tarifa_hora #asigna el valor de tarifa_hora al atributo de instancia self.tarifa_hora.
        self.horas_trabajadas = horas_trabajadas # Asigna el valor de horas_trabajadas al atributo de instancia self.horas_trabajadas.


    def calcular_salario_mensual(self): #define un metodo
        return self.tarifa_hora * self.horas_trabajadas #Este método se utiliza para calcular el salario mensual del empleado basado en su tarifa por hora y horas trabajadas.

# toString se utiliza para  representar un objeto como una cadena de texto
    def toString(self):# Define un método llamado toString que devuelve un diccionario con información sobre el empleado.
        base_info = super().toString()#llama al toString y  obteniendo así la información básica del objeto, que luego puede ser extendida o modificada en la clase derivada
        base_info["salario_mensual"] = self.calcular_salario_mensual() # enriquece el diccionario base_info con el salario mensual calculado del empleado
        return base_info #Devuelve el diccionario base_info, que ahora incluye la información básica del empleado y el salario mensual.

    def __str__(self):# Define el método que se utiliza para obtener una representación en cadena del objeto.
        return f"{super().__str__()}, Salario por horas={self.calcular_salario_mensual()}"#esta línea crea y devuelve una cadena que combina la información de la clase base y el salario mensual, proporcionando una vista completa del objeto
