$(document).ready(function(){
    var form = document.getElementById('form'),
    uploadfield = document.getElementById('uploadfield'),
    xmlfield = document.getElementById('xmlfield'),
    errormessage1 = document.getElementById('errorMessage1'),
    errormessage2 = document.getElementById('errormessage2'),
    submiterrormessage = document.getElementById('submiterror');

    var selection = document.getElementsByName("uploadtype");
    var inputvalue = uploadfield.value;

    for(i = 0; i < selection.length; i++){
        if(selection[i].checked == true){
            if(selection[i].value == "xmlreport"){
                if(uploadvalue == ""){
                    errormessage2.style.color = "red";
                    errormessage2.innerText = "Please enter a file location."
                    e.preventDefault();

                }
                else if(!uploadvalue.includes(".xml")){
                    errormessage2.style.color = "red";
                    errormessage2.innerText = "Please enter a file location."
                    e.preventDefault()
                }
                else
                    errormessage2 = ""
            }
            else if(selection[i].value == "neoloadreport"){
                if(inputvalue == "") {
                    errormessage1.style.color = "red";
                    errormessage1.innerText = "Please enter a report name."
                    e.preventDefault()
                }
                else
                    errormessage1.innerText = "";
            }
        }break;
    }





});

function displayaction() {
    var checkboxes = document.getElementsByName("uploadtype")
    var checkbox;
    for (var i = 0; i < checkboxes.length; i++) {
        if(checkboxes[i].checked)
            checkbox = checkboxes[i].value
    };

    var x = document.getElementById('neoloadsection');

    if(checkbox == 'neoloadreport'){
        x.style.display = "block";
    }
    else {
        x.style.display = "none";
    }
};

function isChecked(elements){
    for(var i = 0; i < elements.length; i++){
        if(elements[i].checked == true)
            return selection[i].value
        break;
    }
}

function toggleCheck(check){
    savetoDBelement = document.getElementById('saveDB')
    if(check.checked == true){
        savetoDBelement.checked = true;
        savetoDBelement.value = "true";
    }
    else {
        savetoDBelement.checked = false;
        savetoDBelement.value = "false";
    }
}