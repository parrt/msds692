# XML

http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree/

The simplest way to handle XML is with [untangle lib](https://github.com/stchris/untangle); see [untangle doc](https://untangle.readthedocs.io/en/latest/).

```python
import untangle
testxml = """<?xml version="1.0"?>
<TruliaWebServices>
    <response>
        <LocationInfo>
            <city>
                <cityId>86930</cityId>
                <name>Yountville</name>
                <longitude>-122.367593491246</longitude>
                <latitude>38.3938834972556</latitude>
            </city>
        </LocationInfo>
    </response>
</TruliaWebServices>
"""

xml = untangle.parse(testxml)
for city in xml.TruliaWebServices.response.LocationInfo.city:
    print city.cityId.cdata, city.name.cdata, city.longitude.cdata, city.latitude.cdata
```
