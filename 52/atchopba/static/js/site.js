$(document).ready(function(){

	// bouton start
	$("#btnstart").click(function() {

        var eventTime= 1366549200; 
        var currentTime = 1366547700; 
        var diffTime = eventTime - currentTime;
        var duration = moment.duration(diffTime*1000, 'milliseconds');
        var interval = 1000;
        
        setInterval(function(){
          duration = moment.duration(duration - interval, 'milliseconds');
            $('#countdown').text(duration.minutes() + ":" + duration.seconds())
        }, interval);

  	});
  	
  	// bouton reset
  	$("#btnreset").click(function() {
      	
      	location.reload(); 
      	
  	});

});