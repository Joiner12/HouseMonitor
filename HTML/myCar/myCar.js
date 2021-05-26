function totalprice(){
    var price=0;
    var num=0;
    var jifen=0;
    var date_table=document.getElementById("shopping");     //form不行，必须要table;table先画出表格，表格里在加入form
    var tr=date_table.getElementsByTagName("tr"); 
    for (var i=1;i<tr.length ;++i )
    {
            if(tr[i].getElementsByTagName("td").length>2&&
        tr[i].getElementsByTagName("td")[0].getElementsByTagName("input")[0].checked)
                    //tr[i].getElementsByTagName("td")[0].firstChild.checked)
            {
                    jifen1=tr[i].getElementsByTagName("td")[3].innerHTML;
                    price1=tr[i].getElementsByTagName("td")[4].innerHTML;
                    num1=tr[i].getElementsByTagName("td")[5].getElementsByTagName("input")[0].value;
                    jifen+=jifen1*num1;
                    price+=price1*num1;
                    tr[i].getElementsByTagName("td")[6].innerHTML=price1*num1;
            }
    }
    document.getElementById("total").innerHTML=price;
    document.getElementById("integral").innerHTML=jifen;
}
window.οnlοad=totalprice;  //自动调用

function selectAll(){
    var selectall=document.getElementById("allCheckBox");  //这里找的是"allCheckBox",而不是allCheckBox
    var checkbox=document.getElementsByName("checkBox");
    if(true==selectall.checked){
            for(var i=0;i<checkbox.length;++i){
                    checkbox[i].checked=true;
                    totalprice();
            }
    }
    else{
            for(var i=0;i<checkbox.length;++i){
                    if(checkbox[i].checked)
                    {
                            checkbox[i].checked=!(checkbox[i].checked);
                            totalprice();
                    }
            }
    }
}

function slectSingle(){   //注意
    var selected=document.getElementsByName("checkBox");
    totalprice();
    var flag=0;
    for (var i=0;i< selected.length; ++i)
    {
            if(false==selected[i].checked)
            {
                    flag=1;
                    break;
            }
    }
    if(0==flag)
            document.getElementById("allCheckBox").checked=true;
    else
            document.getElementById("allCheckBox").checked=false;
}

function changeNum(num_1,flag){
    var click_obj=document.getElementById(num_1);
    var value=click_obj.value;  //其实得到的是文本1
    if("add"==flag)
    {
            //value+=1;  //这里当做字符串来处理,结果11
            value=parseInt(value)+1;
            click_obj.value=value;
            totalprice();
    }
    else
    {
            if(click_obj.value<=1)
            {
                    alert("products' number can not less than 1");
                    //alert("商品数量不能小于等于1");
                    return;
            }
            else
            {
                    value=parseInt(value)-1;
                    click_obj.value=value;
                    totalprice();
            }
    }
}

function deleteRow(rowId) //重点,网页传参,getElementById就不能引号起来
//不带引号标识变量 ，带引号是一个值;如果是数字，需要var temp=数字，然后test(temp);
//所以网页传ID要加引号，因为我们这边只要那个值，而不要对象；不然这边拿到的是对象；
{
    //var delrow=rowId.rowIndex; //网页不加引号；
    var delrow=document.getElementById(rowId).rowIndex;
    document.getElementById("shopping").deleteRow(delrow);
document.getElementById("shopping").deleteRow(delrow-1)
    totalprice();
}
function deleteSelectRow(){
    var oInput=document.getElementsByName("checkBox");
    var index;
    for (var i= oInput.length-1;i>0;i-- )
    {
            if(oInput[i].checked==true)
            {
                     index=document.getElementById(oInput[i].value).rowIndex; /*获取选中行的索引号*/
                     document.getElementById("shopping").deleteRow(index);
                     document.getElementById("shopping").deleteRow(index-1);
        }
    }
    totalprice();
}