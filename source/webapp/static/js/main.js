var digitl = $('#inp1').val();
var digitr = $('#inp2').val();

var data = {"digitl": digitl, "digitr": digitr};
var jsondata = JSON.stringify(data);
var operations = ['add', 'mult', 'div', 'subst'];

for(let i=0; i<operations.length; i++) {
    $(`#${operations[i]}`).click(function () {
        $.ajax({
            url: `http://127.0.0.1:8000/api/v1/${operations[i]/}`,
            method: 'POST',
            dataType: 'json',
            contentType: "application/json",
            data: jsondata,
            success: function (response) {
                console.log(response);
            },
            error: function (response) {
                console.log(response);
            },
        })
    })
}