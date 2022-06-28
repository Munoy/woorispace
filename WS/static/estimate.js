$(document).ready(function(){
        $("#area").keyup(function(){
            $(this).val( $(this).val().replace(/[^\.0-9]/g, '') );
            if(!$("#area_other").val() && $("#area_other").val() != "0")
                $("#area_other").val("0");
            yongdo();
        });

        $("#area_other").keyup(function(){
            $(this).val( $(this).val().replace(/[^\.0-9]/g, '') );
            yongdo();
        });

        $('#yongdo_select').change(function(){
            yongdo();
        });

        $('#classification_select').change(function(){
            yongdo();
        });

        function yongdo(){
            var area = $('#area').val();
            var area_other = $('#area_other').val();
            var use = $("#yongdo_select").val();
            var type = $("#classification_select").val();

            $('#cs_tot').text(''); // 적용 요율
            $('#cs_tot2').text('');
            $('.cs_price_la').text(''); // 감리비
            $('#cs_price_la2').text(''); // 감리비 천원단위 절사
            $("#etc_price").text('');
            $("#etc_price2").text('');

            if(area && area_other)
            {
                var totarea = parseFloat(area) + parseFloat(area_other);
                $("#area_tot").val(totarea);
                if(use && type)
                {
                    $.ajax({
                        url:'./ajax_cal.php',
                        type:'POST',
                        dataType:'json',
                        data: {
                            use : use,
                            area : totarea,
                            type : type,
                            mode : "20220204"
                        },
                        success:function(data){
                            $('#area_tot').val(totarea.toLocaleString());
                            $('#expense_construction_price').text(data.use_cost.toLocaleString()); // 단가
                            $('#area_tot_s').text(totarea.toLocaleString()); // 총면적

                            $('#yongdo_price_tot').text(data.cstrt_cost.toLocaleString()); // 적용공사비
                            $('#yongdo_price_tot_s').text(data.cstrt_cost.toLocaleString()); // 적용원가 (적용공사비와 뭐가 다르지?)
                            $('#yongdo_price_tot_ss').text(data.cstrt_cost.toLocaleString());
                            $('#yongdo_price_tot_sss').text(data.cstrt_cost.toLocaleString());

                            $('#expense_construction_min').text(data.cstrt_cost_min.toLocaleString()); // 작은금액
                            $('#expense_construction_min2').text(data.cstrt_cost_min.toLocaleString());
                            $('#expense_construction_min3').text(data.cstrt_cost_min.toLocaleString());

                            $('#expense_construction_max').text(data.cstrt_cost_max.toLocaleString()); // 큰금액
                            $('#expense_construction_max2').text(data.cstrt_cost_max.toLocaleString());

                            $('#supervising_expenses_min').text(data.type_rate_min); // 작은금액 요율
                            $('#supervising_expenses_min2').text(data.type_rate_min);
                            $('#supervising_expenses_min3').text(data.type_rate_min);

                            $('#supervising_expenses_max').text(data.type_rate_max); // 큰금액 요율
                            $('#supervising_expenses_max2').text(data.type_rate_max);

                            $('#cs_tot').text(data.rate_result); // 적용 요율
                            $('#cs_tot2').text(data.rate_result);

                            $('.cs_price_la').text(data.cs_cost.toLocaleString()); // 감리비
                            $('#cs_price_la2').text(data.cs_cost2.toLocaleString()); // 감리비 천원단위 절사

                            // 설계의도구현비
                            var etc_price = Math.round(data.cs_cost * 0.2);
                            var etc_price2 = Math.floor(etc_price / 1000) * 1000; // 천단위 절사
                            $("#etc_price").text(etc_price.toLocaleString());
                            $("#etc_price2").text(etc_price2.toLocaleString());
                        },
                        error:function(xhr,status,error){
                            alert(xhr.status);
                        }
                    });
                }
            }
        }

        // 프린트 시작
        $('#pagePrint').click(function() {
            $('#print_table_01').show();

            $("#yongdo_select_print").text($("#yongdo_select").val());
            $('#classification_select_print').text($("#classification_select option:selected").text());

            $('#area_print').text($('#area').val());
            $('#area_other_print').text($('#area_other').val());
            $('#area_tot_print').text($("#area_tot").val());

            $('#ttitle, #print_table_01, #print_table_02').printThis({
                loadCSS: ["supervision/style.css", "supervision/print.css"]
            });

        });
        //프린트 끝
    });