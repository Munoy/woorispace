document.getElementById("additional_work_add").onclick = function() {
			var additional_work_select = $("#additional_work_select").val();
			var additional_work_cost = $("#additional_work_cost").val();
			var list_count = document.getElementById("additional_work_list").childElementCount;

			var added_work = '<li id="additional_work_'+list_count+'">' +additional_work_select+ ': <span id="' +additional_work_select+ '">'+ additional_work_cost +'</span>원</li>';
            document.getElementById("additional_work_list").append(added_work);

			const list = document.getElementById("additional_work_list").cloneNode(true);
			list.id = 'additional_work_list_c';
			var list2 = document.getElementById("additional_work_list2");
			while(list2.hasChildNodes()){
				list2.removeChild(list2.childNodes[0]);
			}
			list2.appendChild(list);
			yongdo();
		}


		for ( added_work in document.getElementById("additional_work_list").childNodes) {
		    console.log(added_work.childNodes[0].text();)
		}