let htmldata=``;
let  beauticianData=``;

$(function(){
    var dtToday = new Date();
 
    var month = dtToday.getMonth() + 1;
    var day = dtToday.getDate();
    var year = dtToday.getFullYear();
    if(month < 10)
        month = '0' + month.toString();
    if(day < 10)
        day = '0' + day.toString();
    
    var maxDate = year + '-' + month + '-' + day;
    $('#date_test').attr('min', maxDate);
});
document.getElementById("date_test").addEventListener("change", function() {

    var input = this.value;
    var dateEntered = new Date(input);//e.g. 2015-11-13
    id=document.querySelector("#hide").value
    fetch(`/v1/services/${id}`).then(res=>res.json()).then(data=>populateTimeslot(data))
function populateTimeslot(values){
    data=values
    let host=window.location.host
    beautician=data.beautician
    timeslots=data.timeslots
    htmldata=``
    beauticianData=``;
    beautician.forEach(b=>{
        fetch(`/v1/beauticians/${b}`).then(res=>res.json()).then(data=>beauticianInfo(data)) })
    timeslots.forEach(b=>{
        fetch(`/v1/timeslots/${b}`).then(res=>res.json()).then(data=>slotInfo(data)) })
        function slotInfo(slot){
            if (slot.date==input){
                if (slot.status=="available"){
            htmldata+=`
            <div class="custom-control custom-radio custom-control-inline" id="test">
             <input type="radio" class="custom-control-input" id="${slot.id}" name="slot" value="${slot.time}">
             <label class="custom-control-label" for="${slot.id}">${slot.time}</label>
            </div>`
            
        }}
        document.querySelector("#testing").innerHTML=htmldata
    }


function beauticianInfo(beautician){
    if(beautician.status=="available"){
beauticianData+=`<div class="custom-control custom-radio custom-control-inline" id="beautician">
     <input type="radio" class="custom-control-input" id="${beautician.id}" name="beautician" value="${beautician.name}">
     <label class="custom-control-label" for="${beautician.id}">${beautician.name}</label>
    </div>`
    
}if (input){
    document.querySelector("#beautician").innerHTML=beauticianData}
    else{
        document.querySelector("#beautician").innerHTML=``}
    }  





       
    // timeslots.forEach(slot=>{

    //     if (slot.date==input){
    //         htmldata+=`
    //         <div class="custom-control custom-radio custom-control-inline" id="test">
    //         <input type="radio" class="custom-control-input" id="${slot.id}" name="slot" value="${slot.time}">
    //         <label class="custom-control-label" for="${slot.id}">${slot.time}</label>
    //     </div>
    //         `
    //     }

    // })
    // document.querySelector("#testing").innerHTML=htmldata
        
}

});

