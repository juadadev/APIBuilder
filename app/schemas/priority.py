from enum import Enum


class Priority(Enum):
    BAJA = "BAJA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"


class PriorityPush(Enum):
    URGENTE = "URGENTE"
    NORMAL = "NORMAL"
