import { Injectable } from '@angular/core';


@Injectable({
  providedIn: 'root'
})
export class MapService {


  constructor() { }

  public generateLatLngValues(
    minLatLng: [number, number],
    maxLatLng: [number, number],
    numberOfDataPoints: number,
    intensity: number
  ): number[][] {

    let randomData: number[][] = [];

    let latRange = Math.abs(minLatLng[0] - maxLatLng[0]);
    let lngRange = Math.abs(minLatLng[1] - maxLatLng[1]);

    for (let i = 0; i < numberOfDataPoints; i++) {

      let randomLat = Math.random() * latRange + this.getSmallerValue(minLatLng[0], maxLatLng[0]);
      let randomLng = Math.random() * lngRange + this.getSmallerValue(minLatLng[1], maxLatLng[1]);

      randomData.push([randomLat, randomLng, intensity]);
    }

    return randomData;
  }

  private getSmallerValue(val1: number, val2: number): number {
    if (val1 > val2) {
      return val2;
    }
    return val1;
  };
}
