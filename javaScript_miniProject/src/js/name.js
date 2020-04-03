const USRNAME_LS = "name";
const nameForm = document.getElementById("jsName");
const inputName = nameForm.querySelector("input");

function viewToDoList(name) {
    const hello = nameForm.querySelector("h3");
    const toDoInputContainer = document.querySelector(".toDoInputContainer");
    const body = document.querySelector("body");

    hello.innerHTML = `Hello ${name}, How about today?`;
    inputName.style.display = "none";

    toDoInputContainer.style.display = "flex";

    body.style.paddingTop = "15vh";
}

function saveLSName(name) {
    localStorage.setItem(USRNAME_LS, name);
}

function setNameEvent () {
    console.log(inputName);
    nameForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const name = inputName.value;
        inputName.value = "";
        saveLSName(name);
        viewToDoList(name);
    });
}

function init() {
    const username_ls = localStorage.getItem(USRNAME_LS);
    console.log("usrname", username_ls);
    if (username_ls) {
        viewToDoList(username_ls);
    }else {
        setNameEvent();
    }
}

if (nameForm)
    init();