var angle = 0;
var moonImg,earthImg;

function preload(){
    moonImg = loadImage('moon.jpg');
    earthImg = loadImage('earthmap.jpg');
}

function setup(){
    createCanvas(1200,600,WEBGL);
}

function draw(){
    clear();
    noStroke();
    texture(earthImg);
    rotateY(angle);
    sphere(60,24,24);

    translate(400,0);
    texture(moonImg);
    rotateY(angle);
    sphere(30,24,24);
    angle+=0.007;
}