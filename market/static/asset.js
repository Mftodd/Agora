function getOrderBook(assetId) {
    const url = `/api/order-book/${assetId}`
    return fetch(url).then(response => response.json())
}