// Write a code which can give grades to students according to theirs scores:
// a. 90-100, A
// b. 70-89, B
// c. 60-69, C
// d. 50-59, D
// e. 0-49, F

let scores = 55;
let grades=null;
if(scores>=90 && scores<=100)
{
    grades="A";
}
else if(scores>=70 && scores<90)
{
    grades="B";
}
else if(scores>=60 && scores<70)
{
    grades="C";
}
else if(scores>=50 && scores<60)
{
    grades="D";
}
else if(scores>=0 && scores<50)
{
    grades="F";
}
else{
    grades="Invalid Score!"
}

console.log("Your grade is ",grades);
