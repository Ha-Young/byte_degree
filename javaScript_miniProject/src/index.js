const footer = document.querySelector("footer");

function myInclude(filePath) {
    const includeJs = document.createElement("script");
    includeJs.type = "text/javascript";
    includeJs.src = filePath;
    footer.appendChild(includeJs);
}

console.log("구르딩딩이 만든 ToDo에 오신걸 환영합니다~!\n연락처 : hayeong28@naver.com");

myInclude("./js/clock.js");
myInclude("./js/name.js");
myInclude("./js/toDo.js");