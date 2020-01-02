var productCard = document.getElementById('product-card')
var htmlTag = document.getElementById('invoice-div')

productCard.addEventListener('click', function(){
    var dataRequest = new XMLHttpRequest();
    dataRequest.open('GET',  'https://learnwebcode.github.io/json-example/animals-1.json')
    dataRequest.onload = function(){
        productData = JSON.parse(dataRequest.responseText);
        renderHTML(productData)
    };
    dataRequest.send();
})

function renderHTML(data){
    var htmlItem = "";
    for (i = 0; i < data.length; i++) {
        htmlItem += "<p>" + data[i].name + "is a " + data[i].species + "</p>"
    }
    htmlTag.insertAdjacentHTML('beforeend', htmlItem)
}