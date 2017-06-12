
    var json = {
        "clientForm": {
            "surname" : "Демо",
            "name" : "Демо",
            "email" : "order_test@level.travel",
            "phone" : "+7(000)000-00-00"

        },
        "tourists_list" : {
            "surname" : "DEMO",
            "name": "DEMO",
            "birthday" : "01.01.1991",
            "doc-number" : "00 0000000",
            "doc-date" : "01.01.2020"
        }

    }

    var form = document.forms.new_order;
    var keys_1 = Object.keys(json.clientForm);
    var i;

    for (i = 0; i < keys_1.length; i++) {
       var val = keys_1[i];
       form.querySelector("#clientForm li."+ val +" input").value = json.clientForm[val];
     }

    var list = form.querySelectorAll(".tourists_list > div");
    var keys_2 = Object.keys(json.tourists_list);

    for (i = 0; i < list.length; i++) {
        var tourist = list[i]
        var a
        for(a = 0; a < keys_2.length; a++) {
            var val_2 = keys_2[a]
            tourist.querySelector("li."+ val_2 +" input").value = json.tourists_list[val_2];
        }
    }


