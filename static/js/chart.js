var ctx = document.getElementById('myChart').getContext('2d');
        var chart = new Chart(ctx, {


            type: 'line',


            data: {
                labels: [ {% for i in dates %}'{{ i }}',{% endfor %} ],
                datasets: [
                    {
                        label: 'Deceased',
                        backgroundColor: 'rgb(255,193,7)',
                        borderColor: 'rgb(255,193,7)',
                        data: [ {% for i in data_deceased %}{{ i }},{% endfor %} ],

                    },
                    {
                        label: 'Recovered',
                        backgroundColor: 'rgb(29,42,71)',
                        borderColor: 'rgb(29,42,71)',
                        data: [ {% for i in data_recovered %}{{ i }},{% endfor %} ],

                    },
                    {
                        label: 'Confirmed',
                        backgroundColor: 'rgb(255, 99, 132)',
                        borderColor: 'rgb(255, 99, 132)',
                        data: [ {% for i in data_confirmed %}{{ i }},{% endfor %} ],

                    },
                ]
            },

            options: {}
        });
