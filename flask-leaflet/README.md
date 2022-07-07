# Minimal example use of `Leaflet` with `Flask`

This example It serves as an illustration of how to send geometry from your server to a Leaflet map. It:
1. sends two (hard coded) coordinate pairs from a web page to the server
2. converts them into a GeoJSON `LineString` on the Server
3. returns them to the web page, which draws the resulting `LineString` to the map