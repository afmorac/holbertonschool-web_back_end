const _cloneCar = Symbol('cloneCar');

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  [_cloneCar]() {
    return new this.constructor();
  }

  cloneCar() {
    return this[_cloneCar]();
  }
}
