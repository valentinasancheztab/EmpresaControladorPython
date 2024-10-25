from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from modelos.empleado_tiempo_completo import EmpleadoTiempoCompleto
from modelos.empleado_por_horas import EmpleadoPorHoras
from servicios.empresa_servicio import EmpresaServicio
from pydantic import BaseModel

app = FastAPI()
router = APIRouter()

#esta instanciando empresa_service a EmpresaServicio
empresa_service = EmpresaServicio()

# se estan instanciando clases con atributos
class EmpleadoTiempoCompletoInput(BaseModel): #el BaseModel se utiliza para la validacion de datos y creacion de modelos
    nombre: str
    edad: int
    departamento: str
    anio_contratacion: int
    salario_anual: float

class EmpleadoPorHorasInput(BaseModel):
    nombre: str
    edad: int
    departamento: str
    anio_contratacion: int
    tarifa_hora: float
    horas_trabajadas: int

class DepartamentoInput(BaseModel):
    departamento: str

class TipoEmpleadoInput(BaseModel):
    tipo_empleado: str


#
@router.post('/modelos/empleado_tiempo_completo') #es para crear o enviar datos al servidor (router=gestiona los endpoids
#async= funcion que permite manejar operacions ya sean entrada  o salida de forma no bloqueantes
async def agregar_empleado_tiempo_completo(empleado_data: EmpleadoTiempoCompletoInput):#maneja la solicitud del endpoint, permite que otras tareas procesen sin bloquear el flujo .
    empleado = EmpleadoTiempoCompleto( #se instancia  un objeto con los datos que nos dio el empleado
        nombre=empleado_data.nombre, #el empleado_data: es un objeto que contiene los datos de entrada que ya fueron validados en empleado
        edad=empleado_data.edad,
        departamento=empleado_data.departamento,
        anio_contratacion=empleado_data.anio_contratacion,
        salario_anual=empleado_data.salario_anual
    )
    empresa_service.agregar_empleado(empleado)#se llama la servicio  para agrgar al empleado creado a la lista
    #JSONResponse: permite enviar datos
    #content= se utiliza para especificar datos que se quieren devolver en el servidor
    #status_code=201: se crea el nuevo recurso (201=created)
    return JSONResponse(content={"message": "Empleado a tiempo completo añadido"}, status_code=201) #devuelve la respuesta en forma json en el postman


#se hace lo mismo solo que ahora con el empleado por horas
@router.post('/modelos/empleado_por_horas')
async def agregar_empleado_por_horas(empleado_data: EmpleadoPorHorasInput):
    empleado = EmpleadoPorHoras(
        nombre=empleado_data.nombre,
        edad=empleado_data.edad,
        departamento=empleado_data.departamento,
        anio_contratacion=empleado_data.anio_contratacion,
        tarifa_hora=empleado_data.tarifa_hora,
        horas_trabajadas=empleado_data.horas_trabajadas,
    )
    empresa_service.agregar_empleado(empleado)
    return JSONResponse(content={"message": "Empleado por horas añadido"}, status_code=201)


#permite que se consulte la lista de empleados que perttnecen a un departamento en especifico
@router.get('/servicios/departamento')#define un post que responde las solicitudes de la ruta que le dimos
async def consultar_empleados_por_departamento(empleado_data: DepartamentoInput):# procesa una solicitud que consulta empleados por departamento, conectandose a un servicio para extraer la informacion de los empleados que pertenecen al departamento
    empleados = empresa_service.consultar_empleados_por_departamento(empleado_data.departamento)#consulta el servicio para obtener uma lista de empleados que pertenecen a un departamento
    return JSONResponse(content=[empleado.toString() for empleado in empleados]) #Esta línea genera una respuesta JSON  la cual contiene una lista de empleados, cada uno convertido a texto mediante toString(), y la envía al cliente que hizo la solicitud.


#devuelve los datos de los salarios mensuales de todos los empleados
@router.get('/servicios/salarios')
async def consultar_salarios_mensuales():
    salarios = empresa_service.consultar_salarios_mensuales()#llama al metodo y  recupera los datos de salarios mensuales de los empleados y los guarda en la variable 'salarios'.
    return JSONResponse(content=salarios) #Crea una respuesta JSON a partir del contenido de 'salarios' y la envía al cliente.



@router.get('/servicios/antiguo') #Cuando se realiza una solicitud GET a esta ruta, se ejecuta la función 'consultar_empleado_mas_antiguo'.
async def consultar_empleado_mas_antiguo():#estiona la solicitud de obtener el empleado con más antigüedad
    empleado = empresa_service.consultar_empleado_mas_antiguo() #obtiene el empleado más antiguo registrado y lo guarda en la variable empleado,consulta la base de datos o API para obtener el empleado
    if empleado is None:#identifica si hay o no empleados y si no los hay ejecuta el raise
        #raise:se utiliza para lanzar excepciones y manejar situaciones de error
        #status_code=404  se utiliza para especificar el código de estado HTTP que se devuelve en una respuesta de la API.
       # HTTPException=  es una clase de excepción para manejar errores relacionados con solicitudes HTTP de manera estructurada. Aquí tienes una descripción más detallada:
        raise HTTPException(status_code=404, detail="No hay empleados registrados.")#esta linea lanza una excepcion que informa que no se encuentran empleados registrados
    return JSONResponse(content=empleado.toString())# Si 'empleado' contiene datos, los convierte a texto, luego envia la respuesta



@router.post('/servicios/por tipo')#define un post que responde las solicitudes de la ruta que le dimos
async def consultar_empleados_por_tipo(empleado_data: TipoEmpleadoInput): #está diseñada para recibir datos sobre un tipo de empleado a través de una solicitud  y procesar esa solicitud para consultar y devolver una lista de empleados
    empleados = empresa_service.consultar_empleados_por_tipo(empleado_data.tipo_empleado) # esta línea busca obtener una lista de empleados que pertenecen  empleado_data, utilizando un método del servicio empresa_service para realizar la consulta.
    return JSONResponse(content=[empleado.toString() for empleado in empleados])#rea una respuesta JSON que contiene una lista de representaciones en texto de los empleados consultados y la envía al cliente que realizó la solicitud.


app.include_router(router) #agrega todas las rutas definidas en el objeto router al objeto app, permitiendo que esas rutas estén disponibles y accesibles en la API de FastAPI.


