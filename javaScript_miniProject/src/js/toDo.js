const toDoContainer = document.querySelector(".toDoInputContainer");
const toDoInputForm = document.getElementById("jsToDoInput");
const toDoInput = toDoInputForm.querySelector("input");
const toDoList = toDoContainer.querySelector(".jsToDoList > ul");
const completeList = toDoContainer.querySelector(".jsCompleteList > ul");

const toDoList_LS = "toDoList";
const completeList_LS = "completeList";

let toDoListMem = [];
let completeListMem = [];

function genId() {
    return new Date().getTime();
}

function saveToLSCOMPLETE() {
    localStorage.setItem(completeList_LS, JSON.stringify(completeListMem));
}

function handleDeleteBtn(event) {
    const completeLi = event.target.parentNode;
    const deletedComplete = completeLi.querySelector("span").innerHTML;
    console.log("delete : ", deletedComplete);
    completeList.removeChild(completeLi);
    completeListMem = completeListMem.filter((obj) => obj.id !== parseInt(completeLi.id));
    saveToLSCOMPLETE();
}

function saveComplete(complete, id) {
    const completeObj = {
        id: id,
        value : complete
    }

    completeListMem.push(completeObj);
    console.log("add completeListMem : ", completeObj);
    console.log("stringfy : ", JSON.stringify(completeListMem));
    saveToLSCOMPLETE();
}

function paintComplete(completeToDo, id) {
    const newCompleteLi = document.createElement("li");
    const completeText = document.createElement("span");
    const deleteBtn = document.createElement("button");
    completeText.innerHTML = completeToDo;
    deleteBtn.className = "btn";
    deleteBtn.innerHTML = "❌";
    deleteBtn.addEventListener("click", handleDeleteBtn);
    newCompleteLi.id = id;
    newCompleteLi.appendChild(completeText);
    newCompleteLi.appendChild(deleteBtn);
    completeList.appendChild(newCompleteLi);
}

function addCompleteList(completeToDo, id) {
    paintComplete(completeToDo, id);
    saveComplete(completeToDo, id);
}

function saveToLSTODO() {
    localStorage.setItem(toDoList_LS, JSON.stringify(toDoListMem));
}

function handleCompleteBtn(event) {
    const toDoLi = event.target.parentNode;
    const completedToDo = toDoLi.querySelector("span").innerHTML;
    toDoList.removeChild(toDoLi);
    toDoListMem = toDoListMem.filter((obj) => {
        console.log(obj);
        return obj.id !== parseInt(toDoLi.id)}
        );
    saveToLSTODO();
    console.log("complete : ", completedToDo);
    const newId = genId();
    addCompleteList(completedToDo, newId);
}

function saveToDo(toDo, id) {
    const toDoObj = {
        id: id,
        value : toDo
    }

    toDoListMem.push(toDoObj);
    console.log("add toDoListMem : ", toDoObj);
    console.log("stringfy : ", JSON.stringify(toDoListMem));
    saveToLSTODO();
}

function paintToDo(toDo, id) {
    const newToDoLi = document.createElement("li");
    const toDoText = document.createElement("span");
    const completeBtn = document.createElement("button");
    toDoText.innerHTML = toDo;
    completeBtn.className = "btn";
    completeBtn.innerHTML = "✅";
    completeBtn.addEventListener("click", handleCompleteBtn);
    newToDoLi.id = id;
    newToDoLi.appendChild(toDoText);
    newToDoLi.appendChild(completeBtn);
    toDoList.appendChild(newToDoLi);
}

function addToDoList(toDo, id) {
    if (toDo !== "") {
        saveToDo(toDo, id);
        paintToDo(toDo, id);
    }
}

function handleToDoInput(event) {
    event.preventDefault();
    const toDo = toDoInput.value;
    toDoInput.value = "";
    const newId = genId();
    addToDoList(toDo, newId);
}

function init() {
    toDoInputForm.addEventListener("submit", handleToDoInput);

    const toDoListStr = localStorage.getItem(toDoList_LS);
    const completeListStr = localStorage.getItem(completeList_LS);

    if (toDoListStr) {
        const toDoListArr = JSON.parse(toDoListStr);
        console.log(toDoListArr);
        toDoListMem = toDoListArr;

        toDoListMem.forEach((toDoObj) => {
            paintToDo(toDoObj.value, toDoObj.id);
        });
    }

    if (completeListStr) {
        const completeListArr = JSON.parse(completeListStr);
        console.log(completeListArr);
        completeListMem = completeListArr;

        completeListMem.forEach((completeObj) => {
            paintComplete(completeObj.value, completeObj.id);
        })
    }
}

if (toDoContainer) {
    init();
}