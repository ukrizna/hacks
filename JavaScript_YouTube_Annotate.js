

var params = { allowScriptAccess: "always", wmode: 'transparent' };     
var atts = { id: "myytplayer" };     swfobject.embedSWF("http://www.youtube.com/e/0dKmgPMDnCI?enablejsapi=1&playerapiid=ytplayer", "ytapiplayer", "425", "356", "8", null, null, params, atts);

var ytplayer ;


function onYouTubePlayerReady(playerId) {       
    ytplayer = document.getElementById("myytplayer");  
    ytplayer.addEventListener("onStateChange", "onytplayerStateChange");   
}


function onytplayerStateChange(newState) {    
    if(newState == 1){ // playing
         startWatch();
         noShowDiv();
    }
    else if(newState == 2){// paused
         stopWatch(); 
         var time1 = 1; 
        //Math.floor(myytplayer.getCurrentTime());
         showDiv();    
        
    var trigger = document.getElementById("trigger");
    trigger.addEventListener("click", function () {
        var detail = document.getElementById("detail");
        noShowDiv();
    });
    }            
}

function showDiv() {
 
   document.getElementById('annotate').style.display = "block";
 
}

function noShowDiv() {
   document.getElementById('annotate').style.display = "none";
}


var overlays = [
    {text:"text-1",from:1,to:3},
    {text:"text-2",from:8,to:14}]

var watchId;

function startWatch(){
    watchId = setInterval( function(){
        showOrHideOverlay(ytplayer.getCurrentTime());
    },1000)
}

function stopWatch(){
  clearTimeout(watchId);
}

function showOrHideOverlay(time){
    // find overlays which should be visible at "time"
    var shownOverlays = false;
    for(var i=0;i<overlays.length;i++){
        if(overlays[i].from < time && overlays[i].to > time){
            $('#overlay').text(overlays[i].text);
            shownOverlays = true;
        }           
    }
    if(!shownOverlays)
        $('#overlay').text("");    
}
________________________________________________________________________________________________________________

var params = { allowScriptAccess: "always", wmode: 'transparent' };     
var atts = { id: "myytplayer" };     swfobject.embedSWF("http://www.youtube.com/e/0dKmgPMDnCI?enablejsapi=1&playerapiid=ytplayer", "ytapiplayer", "425", "356", "8", null, null, params, atts);

var ytplayer ;


function onYouTubePlayerReady(playerId) {       
    ytplayer = document.getElementById("myytplayer");  
    ytplayer.addEventListener("onStateChange", "onytplayerStateChange");   
}


function onytplayerStateChange(newState) {    
    if(newState == 1){ // playing
         startWatch();
         noShowDiv();
    }
    else if(newState == 2){// paused
         stopWatch(); 
         var time1 = 1; 
        //Math.floor(myytplayer.getCurrentTime());
         showDiv();    
        
    var trigger = document.getElementById("trigger");
    trigger.addEventListener("click", function () {
        var detail = document.getElementById("detail");
        noShowDiv();
    });
    }            
}

function showDiv() {
 
   document.getElementById('annotate').style.display = "block";
 
}

function noShowDiv() {
   document.getElementById('annotate').style.display = "none";
}


var overlays = [
    {text:"text-1",from:1,to:3},
    {text:"text-2",from:8,to:14}]

var watchId;

function startWatch(){
    watchId = setInterval( function(){
        showOrHideOverlay(ytplayer.getCurrentTime());
    },1000)
}

function stopWatch(){
  clearTimeout(watchId);
}

function showOrHideOverlay(time){
    // find overlays which should be visible at "time"
    var shownOverlays = false;
    for(var i=0;i<overlays.length;i++){
        if(overlays[i].from < time && overlays[i].to > time){
            $('#overlay').text(overlays[i].text);
            shownOverlays = true;
        }           
    }
    if(!shownOverlays)
        $('#overlay').text("");    
}

