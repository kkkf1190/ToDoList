/**
 * Created by zhou on 15-11-6.
 */
function add(){
    var item_input = $('#addvalue')[0];
    var text = item_input.value;
    $.post('./add',{item:text},function(data,status){
        alert(data);
    });

    $('.adddiv').removeClass('on');
    $('.adddiv').addClass('hide');
}
function openAdd(){
    $('.adddiv').addClass('on');
    $('.adddiv').removeClass('hide');
    $('#addvalue')[0].focus();
}
function openEditor(id){
    var button = '#Item'+id;
    var selectorItem = $(button)[0].innerHTML;
    var item = selectorItem.split('.');
    var itemid = item[0];
    var itemText = item[1];
    itemText = itemText.replace(' ','');
    $('#itemid')[0].innerHTML=itemid;
    $('#editInput')[0].value = itemText;
    $('.editdiv').addClass('on');
    $('.editdiv').removeClass('hide');
    $('#editInput')[0].focus();
}
function edit(){
    var id_inout = $('#itemid')[0].innerHTML;
    var item_input = $('#editInput')[0];
    var text = item_input.value;
    $.post('./updata',{item:text,id:parseInt(id_inout)},function(data,status){
        alert(data);
    });
}
function deleteItem(id){
    $.post('./delete',{id:parseInt(id)},function(data,status){
        window.location.reload();
    });
}