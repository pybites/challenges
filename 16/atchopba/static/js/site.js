$(document).ready(function(){

	// bouton rechercher
	$("#btnsearch").click(function() {

        search_text = $("#search_text").val().trim();

        if (search_text == "" ) {
            alert("Renseigner le libellé et la ville, s'il vous plait !");
            return;
        }

        $("#boxresult").html("recherche en cours ...");

    	$.ajax({
    		url: "/search",
    		type: "POST",
    		data: {
    			q: search_text
    		},
    		success : function(data) {
    			$("#boxresult").html(data);
    		},
    		error: function(result, status, error) {
				alert("Une erreur est survenue. Veuillez ressayer!");
                console.log('=> error : ', error);
			},
    		complete: function() {

    		}
    	});

  	});

});