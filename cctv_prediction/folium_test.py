import pandas as pd
import folium


folium_Map = folium.Map(location=[40, -95], zoom_start=4)

print(folium_Map)

url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)
state_geo = "./data/us-states.json"
state_unemployment = "./data/US_Unemployment_Oct2012.csv"
state_data = pd.read_csv(state_unemployment)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name="Unemployment Rate (%)",
).add_to(folium_Map)

folium.LayerControl().add_to(folium_Map)

folium_Map.save("./saved_data/US_Unemployment_Oct2012.html")
