from modelos.empleado import Empleado #sacamos del "model" sacamos la forma de "empleado"

#self:deja que cada instancia de una "clase" tener sus propios datos
class EmpleadoTiempoCompleto(Empleado): #inicia clase de empleado, en "class" creamos un "modelo" o figura
    def __init__(self, nombre, edad, departamento, anio_contratacion, salario_anual): #puedes entrar y modificar los atributos de la instancia actual
        super().__init__(nombre, edad, departamento, anio_contratacion) #es un atributo de la instancia de empleado
        self.salario_anual = salario_anual

    def calcular_salario_mensual(self):
        return self.salario_anual / 12 #llamado de la funcion del salario anual

    def toString(self):#toString este método se utiliza para definir la forma de cadena de un objeto
        base_info = super().toString() #la información fundamental o atributos básicos que describen a una clase o a su instancia de la clase
        base_info["salario_mensual"] = self.calcular_salario_mensual()
        return base_info

    def __str__(self):
        return f"{super().__str__()}, Salario mensual={self.calcular_salario_mensual()}" #retorna el modelo completo de de los salarios
