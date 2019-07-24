let radius = 10;
let area = Math.PI * radius * radius;
console.log(area)
radius = radius * 2;
area = Math.PI * Math.pow(radius, 2);
let width = Math.round(Math.random() * 100);
console.log(width)
let height = Math.round(Math.random() * 50);
console.log(height)
let circumference = width * 2 + height * 2;
console.log(circumference)


let n =1;
const increaseNumber = () => {
  n = n + 1;
  console.log(n);
}
setInterval(increaseNumber, 100);
