import { Component, OnInit, AfterViewInit } from '@angular/core';
import * as L from 'leaflet';
import 'leaflet-maskcanvas';
import { HeatmapOverlay } from 'leaflet-heatmap';
import 'leaflet-webgl-heatmap'
import 'leaflet.heat'
import { MapService } from './utils/map.service';

@Component({
  selector: 'app-map',
  templateUrl: './map.page.html',
  styleUrls: ['./map.page.scss'],
})
export class MapPage implements AfterViewInit {

  private map;

  constructor(private mapSerivce: MapService) { }

  ngAfterViewInit(): void {
    this.initMap();
    // this.initHeatmapLayer_MaskCanvas();
    // this.initHeatmapLayer_webGL();
    // this.initHeatmapLayer_heatmapjs();
    this.initHeatmapLayer_leafheat();
  }

  initMap(): void {

    var base = L.tileLayer('http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png',
      { maxZoom: 19 });

    this.map = L.map('map', {

      center: [57.048820, 9.921747],
      zoom: 11
    });

    const tiles = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      // minZoom: 10,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    });
    tiles.addTo(this.map);
  }

  initHeatmapLayer_MaskCanvas() {
    var layer = L.TileLayer.maskCanvas({
      radius: 1000,  // radius in pixels or in meters (see useAbsoluteRadius)
      useAbsoluteRadius: true,  // true: r in meters, false: r in pixels
      color: '#ff99cc',  // the color of the layer
      opacity: 0.7,  // opacity of the not covered area
      noMask: true,  // true results in normal (filled) circled, instead masked circles
      lineColor: '##ff99cc'   // color of the circle outline if noMask is true
    });

    const data = this.mapSerivce.generateLatLngValues(
      [57.050015, 9.869992],
      [57.010171, 10.002284],
      10,
      5000
    );

    layer.setData(data);

    this.map.addLayer(layer);
  }

  initHeatmapLayer_webGL() {
    var layer = new L.webGLHeatmap({
      size: 600, // diameter-in-meters
      units: 'm',
      opacity: 0.5
    });

    const data = [
      [57.048820, 9.921747, 0.2], // lat, lng, intensity
      [57.048830, 9.921750, 0.5]
    ];

    layer.setData(data);

    this.map.addLayer(layer);
  }

  initHeatmapLayer_heatmapjs() {

    var cfg = {
      // radius should be small ONLY if scaleRadius is true (or small radius is intended)
      // if scaleRadius is false it will be the constant radius used in pixels
      "radius": 2,
      "maxOpacity": .8,
      // scales the radius based on map zoom
      "scaleRadius": true,
      // if set to false the heatmap uses the global maximum for colorization
      // if activated: uses the data maximum within the current map boundaries
      //   (there will always be a red spot with useLocalExtremas true)
      "useLocalExtrema": true,
      // which field name in your data represents the latitude - default "lat"
      latField: 'lat',
      // which field name in your data represents the longitude - default "lng"
      lngField: 'lng',
      // which field name in your data represents the data value - default "value"
      valueField: 'count'
    };

    var data = {
      max: 8,
      data: [
        { lat: 24.6408, lng: 46.7728, count: 3 },
        { lat: 50.75, lng: -1.55, count: 1 }
      ]
    };

    var layer = new HeatmapOverlay(cfg);

    layer.setData(data);

    this.map.addLayer(layer);
  }

  initHeatmapLayer_leafheat() {
    var heat = L.heatLayer(

      this.mapSerivce.generateLatLngValues(
        [57.050015, 9.869992],     //Aalborg
        [57.010171, 10.002284],
        // [57.429071, 10.431206], //Denmark
        // [55.075196,8.137059],
        // [54.647993, 6.635389],     //Germany
        // [47.653608, 16],

        300,
        5000
      ),
      {
        radius: 7


      }).addTo(this.map);
  }

}
