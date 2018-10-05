var $indictorSelectInput = document.getElementById("select-indicator");


values = [].slice.call($indictorSelectInput.selectedOptions).map(a => a.value)
console.log(values);