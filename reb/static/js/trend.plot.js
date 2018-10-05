
String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
};


function render_tsplot(rows) {

    function unpack(rows, key) {
        return rows.map(function (row) {
            return row[key];
        });
    }

    let rwosKeys = Object.keys(rows);
    console.log(rows);
    var trace1 = {
        type: "scatter",
        mode: "lines",
        name: rwosKeys[0],
        x: unpack(rows[rwosKeys[0]], 't'),
        y: unpack(rows[rwosKeys[0]], 'x'),
        line: {color: '#17BECF'}
    };

    var trace2 = {
        type: "scatter",
        mode: "lines",
        name: rwosKeys[1],
        x: unpack(rows[rwosKeys[1]], 't'),
        y: unpack(rows[rwosKeys[1]], 'x'),
        line: {color: '#7F7F7F'}
    }

    var data = [trace1, trace2];

    var layout = {
        title: 'Time Series with Rangeslider',
        xaxis: {
            autorange: true,
            // range: ['2015-02-17', '2017-02-16'],
            rangeselector: {
                buttons: [
                    {
                        count: 1,
                        label: '1m',
                        step: 'month',
                        stepmode: 'backward'
                    },
                    {
                        count: 6,
                        label: '6m',
                        step: 'month',
                        stepmode: 'backward'
                    },
                    {step: 'all'}
                ]
            },
            // rangeslider: {range: ['2015-02-17', '2019-02-16']},
            type: 'date'
        },
        yaxis: {
            autorange: true,
            // range: [86.8700008333, 138.870004167],
            type: 'linear'
        }
    };

    Plotly.newPlot('trendPlot', data, layout);
}
