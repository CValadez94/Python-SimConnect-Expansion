from .SimConnectExpansion import SimConnectExpansion, millis, DWORD
from .RequestList import AircraftRequests, Request
from .EventList import AircraftEvents, Event
from .FacilitiesList import FacilitiesRequests, Facilitie


def int_or_str(value):
	try:
		return int(value)
	except TypeError:
		return value


__version__ = "0.1.0"
VERSION = tuple(map(int_or_str, __version__.split(".")))

__all__ = ["SimConnectExpansion", "Request", "Event", "millis", "DWORD", "AircraftRequests", "AircraftEvents", "FacilitiesRequests"]
