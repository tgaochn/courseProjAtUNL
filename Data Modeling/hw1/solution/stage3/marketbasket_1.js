function marketbasket(items, baskets, s) {
	var frequent_itemsets = [];
	var index = 0;
	
	//check each pair (i, j)
	for (var i = 0; i < items.length; i++) 
	{
		for (var j = i+1; j < items.length; j++) 
		{
			for (var k = i + 1; k < items.length; k++) {
				var basket_count = 0;

				//go through each basket
				for (var b = 0; b < baskets.length; b++) {
					// check if the basket contains both ith and jth items)
					if (baskets[b].items.indexOf(items[i]) != -1 &&
						baskets[b].items.indexOf(items[j]) != -1 &&
						baskets[b].items.indexOf(items[k]) != -1) {
						//if the basket contains both, then add the count 
						basket_count++;
					}
				}

				if (basket_count >= s) {
					frequent_itemsets[index] = [items[i], items[j], items[k]];
					index++;
				}
			}
		}
	}
	
    return frequent_itemsets;
}


window.onload = function init()
{
    var m = document.getElementById("search_button");
    m.addEventListener("click", function() {
		
		//get the start time
		var start = performance.now();

        //get the search value from user input
        var support_threshold = document.getElementById('support_threshold').value;
       
		var result = marketbasket(total_items_2, total_baskets_2, support_threshold);
		
		var format_result = [];
		for (var m = 0; m < result.length; m++) 
		{
		    format_result += "(" + result[m] + ")<br>";
		}

		//get the end time
		var end = performance.now();
		var time = end - start;

		//output the result
		document.getElementById('result').innerHTML = "Search Result:<br>" + format_result;

		//output the timing
		document.getElementById('time').innerHTML = "Time: " + time + " ms";

    });
}