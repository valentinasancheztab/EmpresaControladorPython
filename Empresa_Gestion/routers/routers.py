from fastapi import APIRouter, Request, HTTPException
from modelos.empleado_tiempo_completo import EmpleadoTiempoCompleto
from modelos.empleado_por_horas import EmpleadoPorHoras
from servicios.empresa_servicio import EmpresaServicio

router = APIRouter()


empresa_service = EmpresaServicio()


@router.post('/modelos/empleado_tiempo_completo')
async def agregar_empleado_tiempo_completo(request: Request):
    data = await request.json()
    required_fields = ["nombre", "edad", "departamento", "anio_contratacion", "salario_anual"]
    for field in required_fields:
        if field not in data:
            raise HTTPException(status_code=400, detail=f"Falta el campo: {field}")

    empleado = EmpleadoTiempoCompleto(
        nombre=data["nombre"],
        edad=data["edad"],
        departamento=data["departamento"],
        anio_contratacion=data["anio_contratacion"],
        salario_anual=data["salario_anual"]
    )
    empresa_service.agregar_empleado(empleado)
    return {"message": "Empleado a tiempo completo añadido"}


@router.post('/modelos/empleado_por_horas')
async def agregar_empleado_por_horas(request: Request):
    data = await request.json()
    required_fields = ["nombre", "edad", "departamento", "anio_contratacion", "tarifa_hora", "horas_trabajadas"]
    for field in required_fields:
        if field not in data:
            raise HTTPException(status_code=400, detail=f"Falta el campo: {field}")

    empleado = EmpleadoPorHoras(
        nombre=data["nombre"],
        edad=data["edad"],
        departamento=data["departamento"],
        anio_contratacion=data["anio_contratacion"],
        tarifa_hora=data["tarifa_hora"],
        horas_trabajadas=data["horas_trabajadas"]
    )
    empresa_service.agregar_empleado(empleado)
    return {"message": "Empleado por horas añadido"}



@router.get('/servicios/empresa_servicio/{departamento}')
async def consultar_empleados_por_departamento(departamento: str):
    empleados = empresa_service.consultar_empleados_por_departamento(departamento)
    if not empleados:
        raise HTTPException(status_code=404, detail="No se encontraron empleados en ese departamento.")
    return {"empleados": [empleado.__str__() for empleado in empleados]}


@router.get('/servicios/empresa_servicio/')
async def obtener_empleado_mas_antiguo():
    empleado = empresa_service.consultar_empleado_mas_antiguo()
    if empleado is None:
        raise HTTPException(status_code=404, detail="No hay empleados registrados.")
    return {"empleado": empleado.__str__()}
