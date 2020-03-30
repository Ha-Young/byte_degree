const timeText = document.getElementById("jsTime");

function setTime() {
    const date = new Date();
    let hours = date.getHours();
    const ampm = hours > 12 ? "PM" : "AM";
    hours = hours > 12 ? hours - 12 : hours;
    const minutes = date.getMinutes();
    const secounds = date.getSeconds();
    
    timeText.innerHTML = `${ampm} 
                            ${hours < 10 ? `0${hours}` : `${hours}`}:
                            ${minutes < 10 ? `0${minutes}` : `${minutes}`}:
                            ${secounds < 10 ? `0${secounds}` : `${secounds}`}`;
}

function init() {
    setTime();
    setInterval(setTime, 1000);
}

if (timeText){
    init();
}

