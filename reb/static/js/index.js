
var indicators = {
    0: {abbr: 'PAYEMS', description: "All Employees: Total Nonfarm Payrolls"},
    1: {abbr: 'AWHNONAG', description: ""},
    2: {abbr: 'CES9091000001', description: ""},
    3: {abbr: 'USGOVT', description: ""},
    4: {abbr: 'UNEMPLOY', description: ""},
    5: {abbr: 'LNS13023706', description: ""},
    6: {abbr: 'MVPHGFD027MNFRBDAL', description: ""},
    7: {abbr: 'MNFCTRIRSA', description: ""},
    8: {abbr: 'MNFCTRMPCIMSA', description: ""},
    9: {abbr: 'MORTGAGE30US', description: ""},
    10: {abbr: 'MORTGAGE15US', description: ""},
    11: {abbr: 'DGS10', description: ""},
    12: {abbr: 'INDPRO', description: "Industrial Production Index"},
    13: {abbr: 'CMRMTSPL', description: "Real Manufacturing and Trade Industries Sales"},
    14: {abbr: 'W875RX1', description: "Real personal income excluding current transfer receipts"}
};


var $indictorSelectInput = document.getElementById("select-indicator");
var $targetSelectInput = document.getElementById("select-target")
var $runButton = document.getElementById("run-button");


function predict(selectedFeatures, selectedTargets) {
    let requestUrl = `/predict/${selectedFeatures.toString()}/${selectedTargets.toString()}`

    d3.json(requestUrl).then(function (rows) {
        console.log(rows)

        render_tsplot(rows);
    });


    // update card header
    let $cardHeader = document.getElementById("target-tsplot-header");
    $cardHeader.innerHTML = '<i class="fas fa-chart-line"></i> ' +
        indicators[selectedTargets].description;

    // update card footer
    let elems = document.getElementsByClassName("card-footer");
    let current_date = new Date();
    for (let i=0; i<elems.length; i++) {
        elems[i].innerText = "Updated at " +
            (current_date.getMonth()+1)  + " " +
            current_date.getDate() + "/" +
            current_date.getFullYear() + " @ " +
            current_date.getHours() + ":" +
            current_date.getMinutes() + ":"
            + current_date.getSeconds();
}
}

function predictPAYEMS(selectedFeatures, selectedTargets) {
    let requestUrl = `/predict/PAYEMS/${selectedFeatures.toString()}/${selectedTargets.toString()}`

    d3.json(requestUrl).then(function (data) {
        console.log(data)
    })
}

function predictW875RX1(selectedFeatures, selectedTargets) {
    let requestUrl = `/predict/W875RX1/${selectedFeatures.toString()}/${selectedTargets.toString()}`

    d3.json(requestUrl).then(function (data) {
        console.log(data)
    })
}

function predictINDPRO(selectedFeatures, selectedTargets) {
    let requestUrl = `/predict/INDPRO/${selectedFeatures.toString()}/${selectedTargets.toString()}`

    d3.json(requestUrl).then(function (data) {
        console.log(data)
    })
}

function predictCMRMTSPL(selectedFeatures, selectedTargets) {
    let requestUrl = `/predict/CMRMTSPL/${selectedFeatures.toString()}/${selectedTargets.toString()}`

    d3.json(requestUrl).then(function (data) {
        console.log(data)
    })
}



window.addEventListener("load", function () {
    selectedFeatures = [].slice.call($indictorSelectInput.selectedOptions).map(a => a.value);
    selectedTargets = [].slice.call($targetSelectInput.selectedOptions).map(a => a.value);

    predict(selectedFeatures, selectedTargets);

});


$runButton.addEventListener("click", function () {
    selectedFeatures = [].slice.call($indictorSelectInput.selectedOptions).map(a => a.value);
    selectedTargets = [].slice.call($targetSelectInput.selectedOptions).map(a => a.value);
    predict(selectedFeatures, selectedTargets);

});