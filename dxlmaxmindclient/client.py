from dxlclient.message import Request
from dxlbootstrap.util import MessageUtils
from dxlbootstrap.client import Client


class MaxMindGeolocationClient(Client):
    """
    The "MaxMind Geolocation Client" client wrapper class.
    """

    HOST_LOOKUP_TOPIC = "/opendxl-maxmind/service/geolocation/host_lookup"

    #: The host request parameter
    _PARAM_HOST = "host"

    def __init__(self, dxl_client):
        """
        Constructor parameters:

        :param dxl_client: The DXL client to use for communication with the fabric
        """
        super(MaxMindGeolocationClient, self).__init__(dxl_client)

    def lookup_host(self, host):
        """
        Looks up Geolocation information for the specified host/IP

        :param host: The host/IP to lookup
        :return: A dictionary (``dict``) containing the details of the Geolocation lookup
        """
        # Create the DXL request message
        request = Request(self.HOST_LOOKUP_TOPIC)

        # Set the payload on the request message (Python dictionary to JSON payload)
        MessageUtils.dict_to_json_payload(request, {self._PARAM_HOST: host})
    
        # Perform a synchronous DXL request
        response = self._dxl_sync_request(request)
    
        # Convert the JSON payload in the DXL response message to a Python dictionary
        # and return it.
        return MessageUtils.json_payload_to_dict(response)
