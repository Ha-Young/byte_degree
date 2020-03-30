const footer = document.querySelector("footer");

function myInclude(filePath) {
    const includeJs = document.createElement("script");
    includeJs.type = "text/javascript";
    includeJs.src = filePath;
    footer.appendChild(includeJs);
}

console.log("구르딩딩이 만든 ToDo에 오신걸 환영합니다~!\n연락처 : hayeong28@naver.com");

myInclude("/src/js/clock.js");
myInclude("/src/js/name.js");
myInclude("/src/js/toDo.js");