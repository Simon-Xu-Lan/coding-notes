// @TODO: YOUR CODE HERE!

var chart = new ChartX("scatter")
// chart.setAxisX(["simon", "hl", "lp"])
// chart.setAxisY([30, 80, 40])
// chart.buildBars([{x:"simon", y:30}, {x:"hl", y: 80}, {x:"lp", y:40}])
// console.log(chart)
d3.csv("./assets/data/data.csv")
    .then(data => {
        console.log(data)
        // Parse data / cast as numbers
        data.forEach( data => {
            data.poverty = +data.poverty
            data.healthcare = +data.healthcare
            data.age = +data.age
            data.smokes = +data.smokes
            data.income = +data.income
            data.obesity = +data.obesity
        })
        
        chart.bindData(data)
        chart.setAxisX({x: "poverty", min: true, padding: 0.2})
        chart.setAxisY({y: "healthcare"})
        chart.addCircles({
            x: "poverty", 
            y: "healthcare",
            r: "age",
            color: "lightblue",
            opacity: 0.8
        })






        
    })
    .catch(error => console.log(error))