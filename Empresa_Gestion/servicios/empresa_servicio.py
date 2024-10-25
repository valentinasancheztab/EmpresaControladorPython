from modelos.empleado import Empleado
from modelos.empleado_tiempo_completo import EmpleadoTiempoCompleto
from modelos.empleado_por_horas import EmpleadoPorHoras

class EmpresaServicio:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado: Empleado):
        self.empleados.append(empleado)

    def consultar_empleados_por_departamento(self, departamento: str):
        empleados_departamento = [empleado for empleado in self.empleados if empleado.get_departamento() == departamento]
        return empleados_departamento

    def consultar_salarios_mensuales(self):
        salarios_mensuales = []
        for empleado in self.empleados:
            if isinstance(empleado, EmpleadoTiempoCompleto):
                salarios_mensuales.append(empleado.calcular_salario_mensual())
            elif isinstance(empleado, EmpleadoPorHoras):
                salarios_mensuales.append(empleado.calcular_salario_mensual())
        return salarios_mensuales

    def consultar_empleado_mas_antiguo(self):
        mas_antiguo = None
        for empleado in self.empleados:
            if mas_antiguo is None or empleado.calcular_antiguedad() > mas_antiguo.calcular_antiguedad():
                mas_antiguo = empleado
        return mas_antiguo

    def consultar_empleados_por_tipo(self, tipo_empleado: str):
        empleados_por_tipo = []
        if tipo_empleado == "Tiempo Completo":
            empleados_por_tipo = [empleado for empleado in self.empleados if isinstance(empleado, EmpleadoTiempoCompleto)]
        elif tipo_empleado == "Por Horas":
            empleados_por_tipo = [empleado for empleado in self.empleados if isinstance(empleado, EmpleadoPorHoras)]
        return empleados_por_tipo
