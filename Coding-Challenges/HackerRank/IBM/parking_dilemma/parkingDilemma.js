function carParkingRoof(cars, k) {
  // Write your code here
  let sortedSpots = cars.sort((a, b) => a - b); // nlogn
  let minRoofLength = Infinity;
  // go up k spots from each parking spot until at last car
  for (let i = 0; i <= sortedSpots.length - k; i++) {
    console.log(sortedSpots[i]);
    let currentLength = sortedSpots[i + k - 1] - sortedSpots[i] + 1;
    if (currentLength < minRoofLength) minRoofLength = currentLength;
  }
  return minRoofLength;
}
