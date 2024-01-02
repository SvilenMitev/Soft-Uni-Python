/**
 * Welcome to the Stanford Karel IDE.
 * This is a free space for you to 
 * write any Karel program you want.
 **/

// https://stanford.edu/~cpiech/karel/ide.html
function main(){
    putBeeper();
    fiveTimes ();
    
    }
        
    function fiveTimes (){
    diagonal();
    diagonal();
    diagonal();
    diagonal();
    }
    function diagonal(){
        
    move();
    turnLeft();
    move();
    putBeeper();
    turnRight();
    
    }
    