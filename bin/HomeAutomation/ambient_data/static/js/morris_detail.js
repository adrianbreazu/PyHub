var data_array = [];
for (var i=0; i < jsonDataList.length; i++) {
    var obj = jsonDataList[i];
    console.log(obj.fields.value);
    if (obj.fields.type == 'temperature')
        data_array.push({date:obj.fields.read_datetime, temperature:obj.fields.value});
    else
        data_array.push({date:obj.fields.read_datetime, humidity:obj.fields.value});
};

console.log(data_array);

$(Morris.Line({
    element: 'morris-sensor-chart',

    data: data_array,

    xkey: 'date',

    ykeys: ['temperature', 'humidity'],

    labels: ['Temperature', 'Humidity']
}));