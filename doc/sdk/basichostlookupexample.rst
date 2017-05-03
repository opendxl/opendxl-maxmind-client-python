Basic Host Lookup Example
=========================

This sample invokes and displays the results of a MaxMind database host lookup via DXL.

For more information see:
    https://www.maxmind.com/en/geoip2-services-and-databases

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The MaxMind DXL service is running and available on the DXL fabric (see `MaxMind DXL Service <https://github.com/opendxl/opendxl-maxmind-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_host_lookup_example.py`` script as follows:

    .. parsed-literal::

        python sample/basic/basic_host_lookup_example.py

The output should appear similar to the following:

    .. code-block:: python

        Response:
        {
            "city": {
                "geoname_id": 5375480,
                "names": {
                    "de": "Mountain View",
                    "en": "Mountain View",
                    "fr": "Mountain View",
                    "ja": "\u30de\u30a6\u30f3\u30c6\u30f3\u30d3\u30e5\u30fc",
                    "ru": "\u041c\u0430\u0443\u043d\u0442\u0438\u043d-\u0412\u044c\u044e",
                    "zh-CN": "\u8292\u5ef7\u7ef4\u5c24"
                }
            },
            "continent": {
                "code": "NA",
                "geoname_id": 6255149,
                "names": {
                    "de": "Nordamerika",
                    "en": "North America",
                    "es": "Norteam\u00e9rica",
                    "fr": "Am\u00e9rique du Nord",
                    "ja": "\u5317\u30a2\u30e1\u30ea\u30ab",
                    "pt-BR": "Am\u00e9rica do Norte",
                    "ru": "\u0421\u0435\u0432\u0435\u0440\u043d\u0430\u044f \u0410\u043c\u0435\u0440\u0438\u043a\u0430",
                    "zh-CN": "\u5317\u7f8e\u6d32"
                }
            },
            "country": {
                "geoname_id": 6252001,
                "iso_code": "US",
                "names": {
                    "de": "USA",
                    "en": "United States",
                    "es": "Estados Unidos",
                    "fr": "\u00c9tats-Unis",
                    "ja": "\u30a2\u30e1\u30ea\u30ab\u5408\u8846\u56fd",
                    "pt-BR": "Estados Unidos",
                    "ru": "\u0421\u0428\u0410",
                    "zh-CN": "\u7f8e\u56fd"
                }
            },
            "location": {
                "accuracy_radius": 1000,
                "latitude": 37.419200000000004,
                "longitude": -122.0574,
                "metro_code": 807,
                "time_zone": "America/Los_Angeles"
            },
            "postal": {
                "code": "94043"
            },
            "registered_country": {
                "geoname_id": 6252001,
                "iso_code": "US",
                "names": {
                    "de": "USA",
                    "en": "United States",
                    "es": "Estados Unidos",
                    "fr": "\u00c9tats-Unis",
                    "ja": "\u30a2\u30e1\u30ea\u30ab\u5408\u8846\u56fd",
                    "pt-BR": "Estados Unidos",
                    "ru": "\u0421\u0428\u0410",
                    "zh-CN": "\u7f8e\u56fd"
                }
            },
            "subdivisions": [
                {
                    "geoname_id": 5332921,
                    "iso_code": "CA",
                    "names": {
                        "de": "Kalifornien",
                        "en": "California",
                        "es": "California",
                        "fr": "Californie",
                        "ja": "\u30ab\u30ea\u30d5\u30a9\u30eb\u30cb\u30a2\u5dde",
                        "pt-BR": "Calif\u00f3rnia",
                        "ru": "\u041a\u0430\u043b\u0438\u0444\u043e\u0440\u043d\u0438\u044f",
                        "zh-CN": "\u52a0\u5229\u798f\u5c3c\u4e9a\u5dde"
                    }
                }
            ]
        }



The received results are displayed.

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        # Create the client
        with DxlClient(config) as dxl_client:

            # Connect to the fabric
            dxl_client.connect()

            logger.info("Connected to DXL fabric.")

            # Create client wrapper
            client = MaxMindGeolocationClient(dxl_client)

            # Lookup a host
            resp_dict = client.lookup_host("www.google.com")

            # Print out the response (convert dictionary to JSON for pretty printing)
            print "Response:\n{0}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True))


Once a connection is established to the DXL fabric, a :class:`dxlmaxmindclient.client.MaxMindGeolocationClient` instance is
created which will be used to invoke remote commands on the MaxMind DXL service.

Next, the :func:`dxlmaxmindclient.client.MaxMindGeolocationClient.lookup_host` method is invoked with the host to receive geolocation information about.

The final step is to display the contents of the returned dictionary (``dict``) which contains the results of the host lookup.

