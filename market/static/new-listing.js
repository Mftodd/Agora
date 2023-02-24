function runescapeAsset() {
    fetch('make_rs_asset/')
    .then(response => response.text())
    .catch(error => console.error(error))
}
