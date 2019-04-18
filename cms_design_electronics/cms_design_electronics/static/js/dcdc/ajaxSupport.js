(function($) {
    $.fn.genComponents = function() {
        this.submit(function(event) {
            event.preventDefault();
            var form = $(this);

            //Remove "submission-invalid" class from previously 
            //invalid submissions.
            for(let i = 0; i < form[0].length; i++){
                let input = form[0][i]
                if (input.id){
                    $("#".concat(input.id)).removeClass("submission-invalid");
                }
            }
            $.ajax({
                type: form.attr('method'),
                url: form.attr('action'),
                data: form.serialize(),
                success: function(json){
                    //Update recommended components with recommended values
                    //for design.
                    for (let key in json){
                        document.getElementById(key).value = json[key];
                    }
                    $("#recommendedComponents").addClass("success-indication");
                    setTimeout(function(){
                        $("#recommendedComponents").removeClass("success-indication");
                    }, 1000);
                },
                error: function(json){
                    let jsonErrors = $.parseJSON(json.responseText)

                    for (let key in jsonErrors){
                        $("#".concat(key)).addClass("submission-invalid");
                    }
                }
            });
        });
        return this;
    }
})(jQuery)

$(function() {
    $('#generateRecommendedComponents').genComponents();
});

(function($) {
    $.fn.genAnalysis = function() {
        this.submit(function(event) {
            event.preventDefault();
            var form = $(this);

            //Remove "submission-invalid" class from previously 
            //invalid submissions.
            for(let i = 0; i < form[0].length; i++){
                let input = form[0][i]
                if (input.id){
                    $("#".concat(input.id)).removeClass("submission-invalid");
                }
            }
            $("#generateOpenLoopTransfers").removeClass("submission-invalid")

            $.ajax({
                type: form.attr('method'),
                url: form.attr('action'),
                data: form.serialize(),
                success: function(json){
                    //Update design equations with analysis results.
                    for (let key in json){
                        document.getElementById(key).value = json[key];
                    }
                    $("#generateOpenLoopTransfers").addClass("success-indication");
                    setTimeout(function(){
                        $("#generateOpenLoopTransfers").removeClass("success-indication");
                    }, 1000);
                },
                error: function(json){
                    let jsonErrors = $.parseJSON(json.responseText)

                    for (let key in jsonErrors){
                        $("#".concat(key)).addClass("submission-invalid");
                    }
                }
            });
        });
        return this;
    }
})(jQuery)

$(function() {
    $('#generateConverterAnalysis').genAnalysis();
});

(function($) {
    $.fn.genOpenLoop = function() {
        this.submit(function(event) {
            event.preventDefault();
            var form = $(this);

            $("#generateOpenLoopButton").removeClass("submission-invalid")

            $.ajax({
                type: form.attr('method'),
                url: form.attr('action'),
                data: form.serialize(),
                success: function(json){
                    graphs.forEach(function(graph){
                        for(let div in json){
                            if (graph.mag_plot_div == div){
                                graph.mags = json[div][0];
                                //graph.mags_max = Math.max(json[div][0]);
                                //graph.mags_min = Math.min(json[div][0]);
                                graph.phases = json[div][1];
                                //graph.phases_max = Math.max(json[div][1]);
                                //graph.phases_min = Math.min(json[div][1]);
                                graph.redraw();
                            }
                        }
                    });
                },
                error: function(json){
                    let jsonErrors = $.parseJSON(json.responseText)

                    for (let key in jsonErrors){
                        $("#".concat(key)).addClass("submission-invalid");
                    }
                }
            });
        });
        return this;
    }
})(jQuery)

$(function() {
    $('#generateOpenLoopTransfers').genOpenLoop();
});
