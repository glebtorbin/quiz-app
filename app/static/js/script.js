window.onload = initall;
var saveAnsButton;

function initall(){
    saveAnsButton = document.getElementById('save_ans');
    saveAnsButton.onclick =  saveans
}

function saveans(){
    var ans = $("input:radio[name=ansans]:checked").val()
    alert("Ответ сохранен, нажмите далее")

    var req = new XMLHttpRequest();

    var url = '/saveans?ans='+ ans

    req.open("GET", url, true)
    req.send()
}