import mekha.open_meteo as om

BANGKOK_LAT, BANGKOK_LON = 13.7563, 100.5018


def test_location_to_coordinates():
    location = "Bangkok"
    coords = om.location_to_coordinates(location)

    assert len(coords) == 2

    assert abs(BANGKOK_LAT - coords[0]) ** 2 + abs(BANGKOK_LON - coords[1]) ** 2 < 20
