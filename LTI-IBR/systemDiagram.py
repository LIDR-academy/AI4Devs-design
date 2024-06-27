from diagrams import Diagram, Cluster
from diagrams.onprem.queue import Kafka
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.client import User
from diagrams.generic.device import Mobile
from diagrams.generic.place import Datacenter
from diagrams.onprem.compute import Server
from diagrams.saas.chat import Slack
from diagrams.programming.framework import Spring
from diagrams.programming.language import Python
from diagrams.programming.language import NodeJS
from diagrams.custom import Custom

with Diagram("Microservicios de Venta", show=False):
    usuario = User("usuario")

    with Cluster("Core API"):
        core_api = Spring("servicio de core")

    with Cluster("Cola de Mensajes"):
        cola_redis = Redis("cola en Redis")

    with Cluster("Microservicios"):
        servicio_ventas = Spring("servicio de ventas")
        servicio_productos = Spring("servicio de productos")
        servicio_movimientos = Spring("servicio de movimientos")

    usuario >> core_api >> cola_redis >> servicio_ventas
    servicio_ventas >> servicio_productos
    servicio_productos >> servicio_ventas >> servicio_movimientos