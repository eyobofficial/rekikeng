$(function() {
	// Team Accordion
	$( "#team-accordion" ).accordion({
	    icons: false,
	    heightStyle: "content",
	});

	$('#team-accordion .ui-accordion-header-active .action-icon').html('<i class="fa fa-minus"></i>');

	$('#team-accordion .ui-accordion-header').click(function(){
		    $('#team-accordion .ui-accordion-header .action-icon').html('<i class="fa fa-plus"></i>');
		    $(this).find('.action-icon').html('<i class="fa fa-minus"></i>');
	});

   // Our Service Accordion 
   $( "#service-accordion" ).accordion({
       icons: false,
       collapsible: true,
       active: false,
       heightStyle: "content",
   });

   $('#service-accordion .ui-accordion-header').click(function(){
   	   $('#service-accordion i.fa').removeClass('fa-chevron-down').addClass('fa-chevron-right');
   	   $('#service-accordion .ui-accordion-header-active i.fa').removeClass('fa-chevron-right').addClass('fa-chevron-down');
   });

});