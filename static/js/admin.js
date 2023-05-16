function update_ongoing_anime(){
    $.get("/admin", {Bool: "ONGOING"}, function(response) {
        console.log(response);
       });
}

function update_spot_anime(){
    const inputTextSait = document.getElementById('sait').value;
    const inputTextTitle = document.getElementById('inputField').value;
    const inputTextSeries = document.getElementById('spinbox').value;
    $.get("/admin", {Bool: "SPOT", inputTextSait: inputTextSait, inputTextTitle: inputTextTitle, inputTextSeries: inputTextSeries }, function(response) {
        console.log(response);
       });
}