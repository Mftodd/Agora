

// welcome
let getWallet = document.querySelector("#get-wallet")


getWallet.addEventListener("click", function() {
    ethereum.request({ method: 'eth_requestAccounts' })
})