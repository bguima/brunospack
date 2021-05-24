from brunospack.pack_funcs import weather_forecast

def test_weather_forecast():
    assert len(weather_forecast()) != 0
