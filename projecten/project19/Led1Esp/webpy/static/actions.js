$(document).on("pageinit",function(event){
	
	var JSONret="";
	
	//vernieuwen outputs, inputs
	
	//vernieuwen output_
	$("[id^='output_']").bind("refreshoutput",function(event){
		
		var ID=$(this).attr("id");
		var INDEX=ID.replace("output_","");
		
		//GET REQUEST + JSON ANSWER
			$.getJSON("/output_"+INDEX,function(data){
				JSONret = data;
				var output = JSONret["output_"+INDEX];
				var vals="";
				for(x in output)
				{
					if (x.toString() == "0")
					{
						vals = output;
						break;
					}
					vals+=x+":"+output[x]+",";
				}
				$("#output_"+INDEX).val(vals);
				
				});
		
		});
	
	//vernieuwen toggle_
	$("[id^='toggle_']").bind("refreshtoggle",function(event){
		var ID=$(this).attr("id");
		var INDEX=ID.replace("toggle_","");
		if(JSONret["toggle_"+INDEX]=="1")
		{
			$(this).val("on");
			$(this).slider("refresh");
		}
		else
		{
			$(this).val("off");
			$(this).slider("refresh");
		}
		
	});
	
	//vernieuwen check_
	$("[id^='check_']").bind("refreshcheck",function(event){
		var ID=$(this).attr("id");
		var INDEX=ID.replace("check_","");
		if(JSONret["check_"+INDEX]=="1")
		{
			$(this).prop('checked', true).checkboxradio("refresh");
		}
		else
		{
			$(this).prop('checked', false).checkboxradio("refresh");
		}
		
	});
	
	//vernieuwen select
	$("[id^='select_']").bind("refreshselect",function(event){
		var ID=$(this).attr("id");
		var INDEX=ID.replace("select_","").replace("button","").replace("-","").replace("_","");
		var x=JSONret["select_"+INDEX];
		try
		{
			var arr=x["fill@select"];
			var value=x["value"];
			document.getElementById("select_"+INDEX).options.length = 0; //remove all options, js way
			t=0
			while(t<arr.length)
			{
				$("#select_"+INDEX).append('<option value="'+arr[t]+'">'+arr[t]+'</option>');
				t++;
			}
			$("#select_"+INDEX).val(value).selectmenu("refresh");
		}
		catch(err)
		{
			if(x!="" && x!=undefined)
			{
				$("#output_0").val(x);
			}
		}
		
	});
	
	//vernieuwen radiogroup
	$("[id^='radiogroup_']").bind("refreshradio",function(event){
		var ID=$(this).attr("id");
		var INDEX=ID.replace("radiogroup_","");
		var x = JSONret["radiogroup_"+INDEX];
		try
		{
			var arr=x["fill@radio"];
			var value=x["value"];
			$(this).children().remove();
			var t=0;
			var i=0;
			while(t<arr.length)
			{
				if( arr[t]==value)
				{
					$("#radiogroup_"+INDEX).append('<input type="radio" name="radiogroup_'+INDEX+'_'+(t+1)+'" id="radiogroup_'+INDEX+'_'+(t+1)+'" '+'value="'+arr[t]+'" checked="checked"/><label for="radiogroup_'+INDEX+'_'+(t+1)+'" >'+arr[t]+'</label>');
				}
				else
				{
					$("#radiogroup_"+INDEX).append('<input type="radio" name="radiogroup_'+INDEX+'_'+(t+1)+'" id="radiogroup_'+INDEX+'_'+(t+1)+'" '+'value="'+arr[t]+'"/><label for="radiogroup_'+INDEX+'_'+(t+1)+'" >'+arr[t]+'</label>');
				}
				t++;
			}
			
			//afvangen events op label en vervolgens op radioknop hier afvangen omdat 
			//de radiogroep dynamisch gecreëerd wordt.
			//afvangen label nodig aangezien deze de klik opvangt, deze functie geeft de klik
			//door naar het onderliggende element, nl. de radioknop
			$("label").click(function(){
				var lbID= "";
				lbID = $(this).attr("for");
				$("#"+lbID).trigger("click");
				
				});
			
			//event afvang van de radioknoppen
			$("[id^='radiogroup_"+INDEX+"_']").click(function(){
				var ID=$(this).attr("id");
				var INDEX=ID.replace("radiogroup_","");
				var first_ = INDEX.indexOf("_");
				INDEX = INDEX.substr(0,first_);
				var val=$(this).val();
				//GET REQUEST + JSON ANSWER
				$.getJSON("/radiogroup_"+INDEX+"/"+val,function(data){
					JSONret=data;
				
				});
			});
			
			$(this).trigger("create");
			
			
			
			
		}
		catch(err)
		{
			if(x!="" && x!=undefined)
			{
				$("#output_0").val(x);
			}
		}
	
	});
	
	//vernieuwen slider_
	$("[id^='slider_']").bind("refreshslider",function(event){
		var ID=$(this).attr("id");
		var INDEX=ID.replace("slider_","");
		if (INDEX.indexOf("-range")>0)
		{
			INDEX=INDEX.replace("-range","");
		}
		$("#slider_"+INDEX+"-range").val(JSONret["slider_"+INDEX]).slider("refresh");
		
	});
	
	
	function refreshConn()
	{
		
		$("[id^='output_']").trigger("refreshoutput");
		$("[id^='toggle_']").trigger("refreshtoggle");
		$("[id^='check_']").trigger("refreshcheck");
		$("[id^='slider_']").trigger("refreshslider");
		$("[id^='select_']").trigger("refreshselect");
		$("[id^='radiogroup_']").trigger("refreshradio");
	}
	
	
	
	//timer die om de 800 ms de outputs en inputs triggert
	setInterval(refreshConn,800);
	
	
	//click events op toggle knoppen
	$("[id^='toggle_']").change(function(){
		var val = 0;
		var ID=$(this).attr("id");
		var INDEX=ID.replace("toggle_","");
		if($(this).val() == "on")
		{
			val = 1;
		}
		$.getJSON("/toggle_"+INDEX+"/"+val.toString(),function(data){
				JSONret = data;
		});
		
	});
	
	
	//click event checkbox
	$("[id^='check_']").click(function(){
		var val=0;
		if ($(this).is(":checked"))
		{
			val=1;
		}
		
		var ID=$(this).attr("id");
		var INDEX=ID.replace("check_","");
		//GET REQUEST + JSON ANSWER
		$.getJSON("/check_"+INDEX+"/"+val.toString(),function(data){
			JSONret=data;
				
			});
		
		});
	
	//change event slider
	$("[id^='slider_']").change(function(){
		if (JSONret == "")
		{
			return 0;
		}
		var ID=$(this).attr("id");
		var INDEX=ID.replace("slider_","");
		if (INDEX.indexOf("-range")>0)
		{
			INDEX=INDEX.replace("-range","");
			$.getJSON("slider_"+INDEX+"/"+$(this).val().toString(),function(data){
				JSONret=data;
				});
			}
		});
	
	//change event text(area)box
	
	$("[id^='input_']").change(function(){
		var ID=$(this).attr("id");
		var INDEX=ID.replace("input_","");
		$.getJSON("/input_"+INDEX+"/"+$(this).val(),function(data){
				JSONret = data;
		});
		
	});
	
	//change event select
	
	$("[id^='select_']").change(function(){
		var ID=$(this).attr("id");
		var INDEX=ID.replace("select_","").replace("button","").replace("-","").replace("_","");
		$.getJSON("/select_"+INDEX+"/"+$("#select_"+INDEX).val(),function(data){
				JSONret = data;
		});
		
	});
	
	//click event button
	$("[id^='button_']").click(function(){
		var ID=$(this).attr("id");
		var INDEX=ID.replace("button_","");
		//GET REQUEST + JSON ANSWER
		$.getJSON("/button_"+INDEX,function(data){
			JSONret=data;
				
			});
		
		});
	
	
	});
	
	
