var endpoint='{% url "Get_Data"  %}';
var DefaultData =[]
var labels= []
$.ajax( {
    method: "GET",
    url: endpoint,
    success: function(data) {
        // bug features count chart
        labels= databugfeatures.labels
        DefaultData = databugfeatures.bugfeatures
        var ctx=document.getElementById('myChart').getContext('2d');
        var myChart=new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [ {
                    label: 'Ammount of paid and unpaid features',
                    data: DefaultData,
                    backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',],
                     borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',]
                }]
            }
        })
    },
        error: function(error_data) {
            console.log("error");
            console.log(error_data);
        }
    }) 
