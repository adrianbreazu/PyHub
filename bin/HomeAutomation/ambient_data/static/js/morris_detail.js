console.log(humidity_list)
console.log(temperature_list)
console.log(morris_temperature_data)

/*$(Morris.Line({
    element: 'morris-sensor-chart',

    data:[

        {% for sensor_data in readdata_list %}
            { date: '{{ sensor_data.read_datetime }}', temperature: {{ sensore.read.type }} },
        {% endfor %}
    ],

    xkey: 'date',

    ykeys: ['temperature'],

    labels: ['Temperature']
}));*/