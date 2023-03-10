let htmlData =``
fetch(`v1/services/`).then(result=>result.json()).then(data=>populateAllServices(data))
function populateAllServices(products){
products.forEach(product=>
  htmlData+= `<div class="accordion-item">
  <h2 class="accordion-header" id="flush-heading${product.id}">
    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapse${product.id}" aria-expanded="false" aria-controls="flush-collapse${product.id}">
    <strong>${product.name}</strong>
    </button>
  </h2>
  <div id="flush-collapse${product.id}" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
    <div class="accordion-body">
      <div class="custom-control custom-radio custom-control-inline">
        <input type="radio" class="custom-control-input" id="rad${product.id}" name="service" value="${product.name}">
        <label class="custom-control-label" for="rad${product.id}" onClick="populateAddons(${product.id})">${product.name} <span>$ ${product.cost}</span></label> 
      </div>
      <div id="${product.id}testing">
      </div>  
    </div>
  </div>
  </div>`)
  document.querySelector("#accordionService").innerHTML = htmlData
}
let providerData = ``
let slotData = ``
let dateInput = ``
let availableSlots = ``
var input=``
function catgoryIdFetch(event) {
  id = event.target.id
  fetch(`v1/services/category/${id}`).then(res => res.json()).then(data => populateServices(data))
}

function populateServices(data) {
  htmlData = ``
  data.forEach(service => {
    htmlData += 
`<div class="accordion-item">
    <h2 class="accordion-header" id="flush-heading${service.id}">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapse${service.id}" aria-expanded="false" aria-controls="flush-collapse${service.id}">
      <strong>${service.name}</strong>
      </button>
    </h2>
    <div id="flush-collapse${service.id}" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
      <div class="accordion-body">
        <div class="custom-control custom-radio custom-control-inline">
          <input type="radio" class="custom-control-input" id="rad${service.id}" name="service" value="${service.name}">
          <label class="custom-control-label" for="rad${service.id}" onClick="populateAddons(${service.id})">${service.name} <span>$ ${service.cost}</span></label> 
        </div>
        <div id="${service.id}testing">
        </div>  
      </div>
    </div>
  </div>`
  })
  document.querySelector("#accordionService").innerHTML = htmlData
}

function populateAddons(sid) {
  let addonData = `<div class="accordion" id="accordionPanelsStayOpenExample">
  <div class="accordion-item">
    <h2 class="accordion-header" id="panelsStayOpen-headingOne">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseOne" aria-expanded="true" aria-controls="panelsStayOpen-collapseOne">
      SUGGESTED ADD-ONS 
      </button>
    </h2>
    <div id="panelsStayOpen-collapseOne" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingOne">
      <div class="accordion-body">
        <div className="row">
          <div class="custom-control custom-radio custom-control-inline">
          <input type="radio" class="custom-control-input" id="rad" name="addon">
          <label class="custom-control-label" for="rad"">Test</label>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header" id="panelsStayOpen-headingTwo">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseTwo" aria-expanded="true" aria-controls="panelsStayOpen-collapseTwo">
        SELECT A SERVICE PROVIDER
      </button>
    </h2>
    <div id="panelsStayOpen-collapseTwo" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingTwo">
      <div class="accordion-body">
        <div className="row" id="${sid}beautician">     
        </div>
      </div>
    </div>
  </div>
  <div class="accordion-item" id="${sid}date_input">
  </div>
</div>`
  fetch(`v1/services/${sid}`).then(res => res.json()).then(data => fetchBeauticians(data, sid))
  document.getElementById(`${sid}testing`).innerHTML = addonData
  providerData = ``
}

function fetchBeauticians(data, sid) {
  bids = data.beautician
  bids.forEach(b => {
    fetch(`v1/beauticians/${b}`).then(res => res.json()).then(data => populateBeauticians(data, sid))
    function populateBeauticians(data, sid) {
      providerData += `<div class="custom-control custom-radio custom-control-inline">
<input type="radio" class="custom-control-input" id="provider${data.id}" name="provider" value="${data.name}">
<label class="custom-control-label" for="provider${data.id}" onClick="populateDateSelect(${sid})">${data.name}</label>
</div>`
      document.getElementById(`${sid}beautician`).innerHTML = providerData
    }
  })
}

function populateDateSelect(sid) {
  dateInput = `<div class="accordion" id="accordionPanelsStayOpenExample">
<div class="accordion-item">
  <h2 class="accordion-header" id="panelsStayOpen-headingOne">
    <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseOne" aria-expanded="true" aria-controls="panelsStayOpen-collapseOne">
      SELECT PREFERRED DATE & TIME
    </button>
  </h2>
  <div id="panelsStayOpen-collapseOne" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingOne">
    <div class="accordion-body">
      <div className="row">
        <input type="date" id="date_test"/>
      </div>
      <div class="row mt-10" id="slot-result">
        
      </div>
    </div>
  </div>
</div>
</div>`
  //date limit starts
  $(function () {
    var dtToday = new Date();

    var month = dtToday.getMonth() + 1;
    var day = dtToday.getDate();
    var year = dtToday.getFullYear();
    if (month < 10)
      month = '0' + month.toString();
    if (day < 10)
      day = '0' + day.toString();

    let maxDate = year + '-' + month + '-' + day;
    $('#date_test').attr('min', maxDate);
  });
  //date limit ends
  document.getElementById(`${sid}date_input`).innerHTML = dateInput
  document.getElementById("date_test").addEventListener("change", function fetchnew() {
    var input = this.value;
    //dateEntered = new Date(input);//e.g. 2015-11-13
    availableSlots = ``
    fetch(`v1/services/${sid}`).then(res => res.json()).then(data => filterSlots(data.timeslots,input))

  })
}

function filterSlots(timeslots,input) {
  timeslots.forEach(slot => {
    fetch(`v1/timeslots/${slot}`).then(res => res.json()).then(data => populateSlots(data,input))
    function populateSlots(data,input) {
      if(data.date == input){
        if (data.status == "available") {
          availableSlots += `<div class="custom-control custom-radio custom-control-inline">
          <input type="radio" class="custom-control-input" id="slot${data.id}" name="slots">
          <label class="custom-control-label" for="slot${data.id}">${data.time}</label>
          </div>
          <button class="btn btn-success">Book Service</button>`
        }
      }
      document.querySelector("#slot-result").innerHTML = availableSlots
    }
  })
}

