function VehicleConstructor(name, wheels, passengers, speed){
    
    var distance_travelled = 0;   //private var  
    var updateDistanceTravelled = function(){   //private method
        this.distance_travelled += this.speed;
        console.log(this.distance_travelled);   
    };

    this.name = name;
    this.wheels = wheels;
    this.passengers = passengers;
    this.speed = speed;
    this.distance_travelled = distance_travelled;
    this.updateDistanceTravelled = updateDistanceTravelled;
    

    this.makeNoise = function(){
        console.log("squawk");
    }

    this.move = function(){
        console.log(this.updateDistanceTravelled());
        this.makeNoise();
    }

    this.checkMiles = function(){
        console.log(this.distance_travelled);
    }

    if(!(this instanceof VehicleConstructor)){
        return new VehicleConstructor(name, wheels, passengers, speed);
    }
}


//bike instance
var bike = new VehicleConstructor("bike", 2, 1);

console.log(bike);
bike.makeNoise = function(){
    console.log("ring ring!");
}

bike.makeNoise();


//sedan instance
var sedan = new VehicleConstructor("sedan", 4, 4);

console.log(sedan);
sedan.makeNoise = function(){
    console.log("honk honk!");
}
sedan.makeNoise();


//bus instance
var bus = new VehicleConstructor("bus", 6, 1);

console.log(bus);

bus.pickup = function(passengers){
    bus.passengers += passengers;
};


bus.pickup(10);
console.log(bus.passengers);

bus.speed = 25;
console.log(bus.distance_travelled);
bus.updateDistanceTravelled();
console.log(bus);
bus.move();
bus.checkMiles();