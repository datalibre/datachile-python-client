from opendata_rest.datachile import DataChile

q = DataChile.get(
    "exports", {
        "drilldowns": [["Date", "Year"],
                       ["Destination Country", "Country", "Continent"]],
        "measures": ["FOB US", "Geo Rank"]
    })

print(q)