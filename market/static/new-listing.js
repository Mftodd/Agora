let id = Math.floor(Math.random()* 25000) + 1;

let runescapeAPI = `https://api.weirdgloop.org/runescape/tms`

function getAPI(apiURL) {
    axios.get(apiURL, {
        params: {
            action: 'query',
            format: 'json',
        }
    })
    .then(function(response) {
        console.log(response)
    })
    .catch(function(err){
        console.info(err)
    })
}