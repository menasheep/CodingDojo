function print1To255(){
  
  for(x=1; x<=255; x++){
    console.log(x);
  }

}

print1To255();



function printOdds1To255(){
  
  for(x=1; x<=255; x=x+2){
    console.log(x);
  }

}

printOdds1To255();


var runningTotal=0;
function printIntsSum0To255()
{
  for(x=0; x<=255; x++)
  {
    runningTotal=runningTotal+x;
    console.log(x);
    console.log(runningTotal);
  }
}

printIntsSum0To255();


var arr=[1,2,3,4]

function iteratePrintArray(arr)
{
  for(x=arr[0]; x<arr.length; x++);
  {
    console.log(x);
  }
}

iteratePrintArray(arr)
