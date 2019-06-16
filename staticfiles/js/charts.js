$(document).ready(function() {
    var endpoint = "/accounts/chart/data/";
    var DefaultData = []
    var labels = []
    var labels2 = []
    var DefaultData2 = []
    $.ajax({
        method: "GET",
        url: endpoint,
        // ammount of paid features and bugs
        success: function(data) {
            labels = data.labels;
            DefaultData = data.default;
            var ctx = document.getElementById('myChart').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'A count of bugs and features.',
                        data: DefaultData,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                        ],
                        borderWidth: 1
                    }]
                }
            })
            // chart 2 unpaid + paid features
            labels2 = data.labels2;
            DefaultData2 = data.default2;
            var ctx2 = document.getElementById('paidfeatures').getContext('2d');
            var paidfeatures = new Chart(ctx2, {
                type: 'bar',
                options: {
                    legend: {
                        display: false,
                    }
                },
                data: {
                    labels: labels2,
                    datasets: [{
                        label: 'Features',
                        data: DefaultData2,
                        backgroundColor: [
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                        ],
                        borderColor: [
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                        ],
                        borderWidth: 1
                    }]
                }
            })
            // chart 3 most upvotes
            labels3 = data.labels3;
            DefaultData3 = data.default3;
            var ctx3 = document.getElementById('upvotesfeatures').getContext('2d');
            var paidfeatures = new Chart(ctx3, {
                type: 'polarArea',
                data: {
                    labels: labels3,
                    datasets: [{
                        label: 'Most Upvoted',
                        data: DefaultData3,
                        backgroundColor: [
                            'rgba(214, 152, 185, 0.2)',
                            'rgba(174, 221, 205, 0.2)',
                        ],
                        borderColor: [
                            'rgba(223, 117, 153, 1)',
                            'rgba(114, 214, 201, 1)',
                        ],
                        borderWidth: 1
                    }]
                }
            })
            // chart 4 doingdone for bugs
            labels4 = data.labels4;
            DefaultData4 = data.default4;
            var ctx4 = document.getElementById('doingdone').getContext('2d');
            var doingdone = new Chart(ctx4, {
                type: 'pie',
                data: {
                    labels: labels4,
                    datasets: [{
                        label: 'Doing Done and Finished',
                        data: DefaultData4,
                        backgroundColor: [
                            'rgba(255, 199, 133, 0.2)',
                            'rgba(214, 152, 185, 0.2)',
                            'rgba(150, 178, 171, 0.2)',
                        ],
                        borderColor: [
                            'rgba(255, 182, 119, 1)',
                            'rgba(214, 152, 185, 1)',
                            "rgba(97, 192, 191, 1)",
                        ],
                        borderWidth: 1
                    }]
                }
            })
            // chart 5 doingdone for features
            labels5 = data.labels5;
            DefaultData5 = data.default5;
            var ctx5 = document.getElementById('doingdonef').getContext('2d');
            var doingdonef = new Chart(ctx5, {
                type: 'pie',
                data: {
                    labels: labels5,
                    datasets: [{
                        label: 'Doing Done and Finished',
                        data: DefaultData5,
                        backgroundColor: [
                            'rgba(232, 211, 255, 0.2)',
                            'rgba(222, 252, 252, 0.2)',
                            'rgba(150, 178, 171, 0.2)',
                        ],
                        borderColor: [
                            'rgba(105, 119, 155, 1)',
                            'rgba(166, 227, 233, 1)',
                            "rgba(97, 192, 191, 1)",
                        ],
                        borderWidth: 1
                    }]
                }
            })
        },


        error: function(error_data) {
            console.log("error");
            console.log(error_data);
        }
    })
});
