function getOrderBook(assetId) {
    const url = `/api/order-book/${assetId}`
    return fetch(url).then(response => response.json())
}

let orderBookDiv = document.querySelector('#order-book-div')
orderBookDiv.addEventListener("")

function checkOrderBook(assetId) {

}