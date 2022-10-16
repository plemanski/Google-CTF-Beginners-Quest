
function controlCar(scanArray) {
    let bigD = 0;
    let tempD = 0;
    let bestIndex;
    let count = 0 ;
    for (let i = 0; i < scanArray.length; i++){
       count = scanArray[i] == tempD ? count + 1 : 1;
        if (tempD < scanArray[i]){
            tempD = scanArray[i];
            count = 1;
        }
        if (bigD < tempD && count >= 2){
            bigD = tempD;
            bestIndex = i;
        }
      }
    return bestIndex > 8 ? bestIndex - 8 : bestIndex - 8;
}