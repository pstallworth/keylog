$(document).ready(function() {
	$('#keytable').dataTable({
            "bServerSide": true,
            "sAjaxSource": "/keylog/source"
    }).makeEditable({
		    sUpdateURL: "/keylog/update",
		    sAddURL: "/keylog/add",
		    sDeleteURL: "/keylog/delete"
	} );
} );
