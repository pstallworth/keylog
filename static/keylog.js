$(document).ready(function() {
	$('#keytable').dataTable({
            "bServerSide": true,
            "sAjaxSource": "/keylog/source"
    }).makeEditable({
		    sUpdateURL: "/UpdateData",
		    sAddURL: "/keylog/add",
		    sDeleteURL: "DeleteData.py"
	} );
} );
