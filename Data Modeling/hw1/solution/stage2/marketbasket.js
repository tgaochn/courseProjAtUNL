function a_priori(items, baskets, s) {
    var result = [];
    var basket_count = 0;
    // s = 3;
    
    // pass 1: construct the C1 table
    var C1 = [];
    
    // pass 2: construct the F1 table
    var F1 = [];

    var indexC1 = 0;
    var indexF1 = 0;
    for (var i = 0; i < items.length; i++) {
        basket_count = 0
        for (var b = 0; b < baskets.length; b++) {
            if (baskets[b].items.indexOf(items[i]) != -1) {
                basket_count++;
            }
        }
        if (basket_count >= s) {
            F1[indexF1] = items[i];
            indexF1++;
        }
    }

    // pass 3: construct the C2 table  
    var C2 = [];

    // pass 4: construct the F2 table
    var F2 = [];

    var indexF2 = 0;
    for (var i = 0; i < F1.length; i++) {
        for (var j = i + 1; j < F1.length; j++){
            basket_count = 0
            for (var b = 0; b < baskets.length; b++) {
                if (baskets[b].items.indexOf(F1[i]) != -1 &&
                    baskets[b].items.indexOf(F1[j]) != -1) {
                    basket_count++;
                }
            }
            if (basket_count >= s) {
                F2[indexF2] = [F1[i], F1[j]];
                indexF2++;
            }
        }
    }

	// pass 5: construct the C3 table  
    var C3 = [];

    // pass 6: construct the F3 table
    var F3 = [];

    var indexF3 = 0;
    var union = [];
    var visitedTupleSet = new Set([])

    for (var i = 0; i < F2.length; i++) {
        for (var j = i + 1; j < F2.length; j++) {
            basket_count = 0
            union = F2[i].concat(F2[j].filter(v => !F2[i].includes(v)))
            if (union.length == 3) {
                union.sort();
                tupleStr = union[0] + union[1] + union[2];
                if (!visitedTupleSet.has(tupleStr)){
                    visitedTupleSet.add(tupleStr);
                    for (var b = 0; b < baskets.length; b++) {
                        if (baskets[b].items.indexOf(union[0]) != -1 &&
                            baskets[b].items.indexOf(union[1]) != -1 &&
                            baskets[b].items.indexOf(union[2]) != -1) {
                            basket_count++;
                        }
                    }
                    if (basket_count >= s) {
                        F3[indexF3] = [union[0], union[1], union[2], basket_count];
                        indexF3++;
                    }  
                }
            }
        }
    }

    result = F3;
    return result;
}

window.onload = function init()
{
    var m = document.getElementById("search_button");
    m.addEventListener("click", function() { 
        //get the start time
        var start = performance.now();

        //get the support threshold from user input
        var support_threshold = document.getElementById('support_threshold').value;
       
        var result = [];
        result = a_priori(total_items_2, total_baskets_2, support_threshold);
        
        var format_result = [];
        for (var m = 0; m < result.length; m++) 
        {
            format_result += "(" + result[m].slice(0, result[m].length - 1) + ") " + result[m][result[m].length - 1] + "<br>";
        }

        //get the end time
        var end = performance.now();
        var time = end - start;
        
        document.getElementById('result').innerHTML = "Search Result:<br>" + format_result;

        //output the timing
        document.getElementById('time').innerHTML = "Time: " + time + " ms";
    });
}