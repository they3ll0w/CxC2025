"use client"

import { useEffect } from "react"
import MainLayout from "@/app/main/layout"
import * as am5 from "@amcharts/amcharts5"
import * as am5map from "@amcharts/amcharts5/map"
import am5geodata_worldLow from "@amcharts/amcharts5-geodata/worldLow"
import am5index from "@amcharts/amcharts5/index";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";

const mapData = [
    { 'city': 'Alexandria', 'latitude': 31.2001, 'longitude': 29.9187, 'count': 26 },
    { 'city': 'Ashburn', 'latitude': 39.0438, 'longitude': -77.4875, 'count': 1358 },
    { 'city': 'Atlanta', 'latitude': 33.749, 'longitude': -84.388, 'count': 27 },
    { 'city': 'Birmingham', 'latitude': 33.5186, 'longitude': -86.8104, 'count': 21 },
    { 'city': 'Boardman', 'latitude': 41.0244, 'longitude': -80.6534, 'count': 1318 },
    { 'city': 'Boca Raton', 'latitude': 26.3587, 'longitude': -80.0831, 'count': 12 },
    { 'city': 'Boydton', 'latitude': 36.6509, 'longitude': -78.3959, 'count': 119 },
    { 'city': 'Carlsbad', 'latitude': 33.1581, 'longitude': -117.3506, 'count': 16 },
    { 'city': 'Chicago', 'latitude': 41.8781, 'longitude': -87.6298, 'count': 93 },
    { 'city': 'Columbus', 'latitude': 39.9612, 'longitude': -82.9988, 'count': 1348 },
    { 'city': 'Dallas', 'latitude': 32.7767, 'longitude': -96.797, 'count': 12 },
    { 'city': 'Des Moines', 'latitude': 41.5868, 'longitude': -93.625, 'count': 19 },
    { 'city': 'Fort Lauderdale', 'latitude': 26.1223, 'longitude': -80.1434, 'count': 16 },
    { 'city': 'Gmina ??wiebodzin', 'latitude': 52.1722, 'longitude': 15.7031, 'count': 12 },
    { 'city': 'Greenville', 'latitude': 34.8526, 'longitude': -82.394, 'count': 22 },
    { 'city': 'Jacksonville', 'latitude': 30.3322, 'longitude': -81.6556, 'count': 18 },
    { 'city': 'Los Angeles', 'latitude': 34.0522, 'longitude': -118.2437, 'count': 11 },
    { 'city': 'McCalla', 'latitude': 33.3001, 'longitude': -87.0745, 'count': 12 },
    { 'city': 'Miami', 'latitude': 25.7617, 'longitude': -80.1918, 'count': 69 },
    { 'city': 'Mumbai', 'latitude': 19.076, 'longitude': 72.8777, 'count': 50 },
    { 'city': 'Naples', 'latitude': 26.142, 'longitude': -81.7948, 'count': 13 },
    { 'city': 'Nashville', 'latitude': 36.1627, 'longitude': -86.7816, 'count': 117 },
    { 'city': 'New York', 'latitude': 40.7128, 'longitude': -74.006, 'count': 65 },
    { 'city': 'Newnan', 'latitude': 33.371, 'longitude': -84.7912, 'count': 10 },
    { 'city': 'Niceville', 'latitude': 30.524, 'longitude': -86.461, 'count': 11 },
    { 'city': 'Orlando', 'latitude': 28.5383, 'longitude': -81.3792, 'count': 19 },
    { 'city': 'Phoenix', 'latitude': 33.4484, 'longitude': -112.074, 'count': 24 },
    { 'city': 'Richmond', 'latitude': 37.5407, 'longitude': -77.436, 'count': 10 },
    { 'city': 'San Francisco', 'latitude': 37.7749, 'longitude': -122.4194, 'count': 11 },
    { 'city': 'San Jose', 'latitude': 37.7749, 'longitude': -122.4194, 'count': 1318 },
    { 'city': 'Scarborough', 'latitude': 43.7732, 'longitude': -79.2575, 'count': 15 },
    { 'city': 'Simpsonville', 'latitude': 34.7344, 'longitude': -82.263, 'count': 17 },
    { 'city': 'Spring Hill', 'latitude': 28.9832, 'longitude': -82.4545, 'count': 70 },
    { 'city': 'St. Petersburg', 'latitude': 27.7676, 'longitude': -82.6403, 'count': 16 },
    { 'city': 'Stamford', 'latitude': 41.0534, 'longitude': -73.5387, 'count': 21 },
    { 'city': 'Tampa', 'latitude': 27.9506, 'longitude': -82.4572, 'count': 10 },
    { 'city': 'Toronto', 'latitude': 43.6511, 'longitude': -79.347, 'count': 12 },
    { 'city': 'Vancouver', 'latitude': 49.2827, 'longitude': -123.1207, 'count': 10 },
    { 'city': 'Washington', 'latitude': 38.9072, 'longitude': -77.0369, 'count': 1339 },
    { 'city': 'Wa??brzych', 'latitude': 50.7717, 'longitude': 16.2894, 'count': 16 },
    { 'city': 'West Palm Beach', 'latitude': 26.7153, 'longitude': -80.0534, 'count': 10 },
    { 'city': 'Wroclaw', 'latitude': 51.1079, 'longitude': 17.0385, 'count': 14 },
]

export default function UserHeatmap() {
    useEffect(() => {
        const root = am5.Root.new("chartdiv");
        root.setThemes([am5themes_Animated.new(root)]);

        const chart = root.container.children.push(
            am5map.MapChart.new(root, {
                panX: "rotateX",
                panY: "translateY",
            })
        )

        let polygonSeries = chart.series.push(
            am5map.MapPolygonSeries.new(root, {
                geoJSON: am5geodata_worldLow,
                exclude: ["AQ"]
            })
        )

        polygonSeries.mapPolygons.template.setAll({
            tooltipText: "{name}",
            interactive: true
        })

        polygonSeries.mapPolygons.template.states.create("hover", {
            fill: am5.color(0x677935)
        })

        // background
        chart.chartContainer.set("background", am5.Rectangle.new(root, {
            fill: am5.color(0xd4f1f9),
            fillOpacity: 1
        }))

        chart.set("zoomControl", am5map.ZoomControl.new(root, {}))

        let bubbleSeries = chart.series.push(
            am5map.MapPointSeries.new(root, {
                valueField: "count",
                calculateAggregates: true,
                latitudeField: 'latitude',
                longitudeField: 'longitude',
            })
        )

    }, [])

    return (
        <MainLayout>
            <div className="h-full flex flex-col items-center justify-center gap-4 dark:bg-zinc-800 overflow-hidden">
                <h1>Global Platform Usage Map</h1>
                <div className="rounded-lg dark:shadow-[0px_0px_6px_rgba(255,255,255,0.25)] shadow-[0px_0px_6px_rgba(0,0,0,0.1)] border border-zinc-400 overflow-hidden w-[80%] h-[70%]">
                    <div id="chartdiv" className="w-full h-full"></div>
                </div>
            </div>
        </MainLayout >
    )
}