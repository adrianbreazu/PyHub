// make sensor data form visible
function AddSensor() {
    document.getElementById("form-edit").style.visibility = "visible";
}

// add sensor function, responsible for adding the form data into the table
function addTableData() {
    var table = document.getElementById("sensorTable");
    var row = table.insertRow(-1);
    var sensorId = row.insertCell(0);
    var sensorName = row.insertCell(1);
    var sensorLocation = row.insertCell(2);
    var sensorBoardType = row.insertCell(3);
    var sensorCommunicationType = row.insertCell(4);
    var sensorType = row.insertCell(5);
    var sensorReadDataInterval = row.insertCell(6);
    var sensorOperations = row.insertCell(7);

    sensorId.innerHTML = document.getElementById("sensorId").value;
    sensorName.innerHTML = document.getElementById("sensorName").value;
    sensorLocation.innerHTML = document.getElementById("sensorLocation").value;
    sensorBoardType.innerHTML = document.getElementById("sensorBoardType").value;
    sensorCommunicationType.innerHTML = document.getElementById("sensorCommunicationType").value;
    sensorType.innerHTML = document.getElementById("sensorType").value;
    sensorReadDataInterval.innerHTML = document.getElementById("sensorReadDataInterval").value;
    sensorOperations.innerHTML = '<a onclick="EditSensor(this)" ><i class="fa fa-edit fa-fw"></i></a> <a onclick="DeleteSensor(this)"><i class="glyphicon glyphicon-trash glyphicon-fw"></i></a>';
}

// delete sensor data from the table
function DeleteSensor(row_clicked) {
    var rowValue = row_clicked.parentNode.parentNode.rowIndex;

    document.getElementById("sensorTable").deleteRow(rowValue);
}

// edit sensor is responsible for filling the form data with the selected row content
function EditSensor(row_clicked) {
    var rowValue = row_clicked.parentNode.parentNode.rowIndex;
    var table = document.getElementById("sensorTable");
    var row = table.rows[rowValue];

    document.getElementById("form-edit").style.visibility = "visible";
    fillData(row.cells[0].innerHTML,
    row.cells[1].innerHTML,
    row.cells[2].innerHTML,
    row.cells[3].innerHTML,
    row.cells[4].innerHTML,
    row.cells[5].innerHTML,
    row.cells[6].innerHTML
    );
}

// general fill function that populate the form inputs with data
function fillData(sensorId, sensorName, sensorLocation, sensorBoardType, sensorCommunicationType, sensorType, sensorReadDataInterval)
{
    document.getElementById("sensorId").value = sensorId;
    document.getElementById("sensorName").value = sensorName;
    document.getElementById("sensorLocation").value = sensorLocation;
    document.getElementById("sensorBoardType").value = sensorBoardType;
    document.getElementById("sensorCommunicationType").value = sensorCommunicationType;
    document.getElementById("sensorType").value = sensorType;
    document.getElementById("sensorReadDataInterval").value = sensorReadDataInterval;
}

// clear form inputs
function clearContent() {
    fillData("","","","","","","");
    document.getElementById("form-edit").style.visibility = "hidden";
}

// validate form data
function ValidateForm() {
    sensor_id = document.getElementById("sensorId").value;
    sensorName = document.getElementById("sensorName").value;
    sensorLocation = document.getElementById("sensorLocation").value;
    sensorBoardType = document.getElementById("sensorBoardType").value;
    sensorCommunicationType = document.getElementById("sensorCommunicationType").value;
    sensorType = document.getElementById("sensorType").value;
    sensorReadDataInterval = document.getElementById("sensorReadDataInterval").value;

    // validate inputs
    // ..here..

    return true;
}

// Save content into Django model and table
function SaveChanges() {
    addTableData();

    // store data
    // ..here..

    clearContent();
}