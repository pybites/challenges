var pomodoroTimer;


function countDown(){
  var timer = document.getElementById("timer")
  timer.disabled = true;
  var cancelTimer = document.getElementById("cancelTimer")
  cancelTimer.style.display = "inline";

  var now = new Date().getTime();
  var end = new Date(now)
  // test
  // var countDownDate = end.setSeconds(end.getSeconds() + 3);
  var countDownDate = end.setMinutes(end.getMinutes() + 25);

  console.log(countDownDate);

  pomodoroTimer = setInterval(function() {

      now = new Date().getTime();
      var distance = countDownDate - now;

      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);

      timer.innerHTML = "Time left: " + minutes + "m " + seconds + "s ";

      if (distance < 0) {
        cancelPomodoro();
        logPomodoro();
      }
  }, 1000);
}


function cancelPomodoro(){
  clearInterval(pomodoroTimer);
  var timer = document.getElementById("timer")
  timer.innerHTML = "Start Pomodoro";
  timer.disabled = false;
  var cancelTimer = document.getElementById("cancelTimer")
  cancelTimer.style.display = "none";
}


function logPomodoro(){
  document.getElementById("addPomo").submit();
}
