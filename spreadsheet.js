
jQuery.fn.sheet = function(options){
	var opts = $.extend({}, $.fn.sheet.defaults, options);

	/*private logging function */
	function log(s){
		$('#logging').append(s);
	}

	/* create a cols x rows grid */

	var t = '<table class="sheet ui-helper-reset ui-widget" cellspacing="0">';

	t = t + '<thead class="ui-widget-header"><tr class="ui-helper-reset"><th></th>';

	for (i=0; i <opts.cols; i++){
		t = t + '<th class="ui-helper-reset">'+ String.fromCharCode(65+i)+"</th";
	}
}