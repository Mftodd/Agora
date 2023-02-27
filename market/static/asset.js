let dropBtns = document.querySelectorAll("#drop-btn")
let dropContents = document.querySelectorAll("#drop-content")


function getOrderBook(assetId) {
    const url = `/api/order-book/${assetId}`
    return fetch(url).then(response => response.json())
}

function showItems(dropBtn, dropContent) {
    dropContent.classList.toggle("hidden")
    dropContent.classList.toggle("flex")

    dropBtn.textContent = dropContent.classList.contains("hidden") ? "+" : "–";
}

dropBtns.forEach((dropBtn, index) => {
    dropBtn.addEventListener("click", ()=>{
        showItems(dropBtn, dropContents[index])
    })
})
