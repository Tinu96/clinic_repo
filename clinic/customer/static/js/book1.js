let beauticianData = ``
let slotData = ``
let csrf_token = document.getElementById("csrf-val")
let catId = document.querySelector(".tst")
let user = document.getElementById('user').value
let userStatus = false
let beautician = ``
let addonsData = ``
let addon=``

catgoryIdFetch(catId.id)
userStatusCheck()
function userStatusCheck() {
    if (user == "AnonymousUser") {
        userStatus = false
    }
    else {
        userStatus = true
    }
}
function catgoryIdFetch(event) {
    id = event
    fetch(`v1/services/category/${id}`).then(res => res.json()).then(data => populateServices(data))
}
function populateServices(data) {
    htmlData = ``
    data.forEach(service => {
        htmlData += `<div class="card">
            <div class="card-header collapsed" data-toggle="collapse" data-target="#collapse${service.id}" aria-expanded="false" aria-controls="collapseTwo">
                <span class="title">${service.name}</span>
                <span class="accicon"><i class="fas fa-angle-down rotate-icon"></i></span>
            </div>
            <div id="collapse${service.id}" class="collapse" data-parent="#accordionExample">
                <form action="" id="form">

                    <div class="card-body">

                        <div class="package-box">
                            <div class="row">
                                <div class="col-lg-10">
                                    <p>${service.name}</p>
                                </div>
                                <div class="col-lg-2">
                                    <h6>$ ${service.cost}</h6>
                                    <div class="select-bx"><input type="checkbox" name="service" value="${service.name}" id="check${service.id}" onChange=serviceSelect(${service.id},${service.category}) required ></div>
                                </div>
                            </div>
                        </div>
                        <div class="add_ons">
                            <div class="row">
                                <div class="col-12">
                                    <h5>SUGGESTED Add-onS</h5>
                                </div>
                            </div>
                            <div class="row" id="add-ons-list${service.id}">
                            
                            </div>
                        </div>
                        <div class="provider-section">
                            <h5>Select Service Provider</h5>
                            <div><input type="checkbox" class="checkoption" name="provider" value="Any Service Provider" id="all-beautician${service.id}" onClick="allBeauticians(${service.id})"> Any Service Provider </div>
                            <div><input type="checkbox" class="checkoption" name="provider" value="Any Male Service Provider" id="male-beautician${service.id}" onClick="maleBeautician(${service.id})"> Any Male Service Provider </div>
                            <div><input type="checkbox" class="checkoption" name="provider" value="Any Female Service Provider" id="female-beautician${service.id}" onClick="femaleBeautician(${service.id})"> Any Female Service Provider </div>
                        </div>
                        <div class="provider-list">
                            <div class="col-lg-12 p-0" id="provider-data${service.id}">
                            </div>
                        </div>
                        <div class="date_time">
                            <h5>SELECT DATE AND TIME</h5>
                            <div class="row">
                                <div class="col-lg-6">
                                    <form action="">
                                        <input class="dtp" type="date" id="date${service.id}" name="date" value="" required onChange="dateFetch(event,${service.id})">
                                    </form>
                                </div>
                                <div class="col-lg-6">
                                    <select class="dtp" name="time" value="" id="slots${service.id}">
                                    </select>
                                </div>
                            </div>
                        </div>

                        <div class="booking-forwhome">
                            <h5>Who are you booking for?</h5>

                            <div class="select-box">
                                <select class="dtp" name="booking" id="booking${service.id}" value="" required="required" onChange="test(event)">
                                    <option value="me"> Name (Me)</option>
                                    <option value="family">Add family or freinds</option>
                                </select>
                            </div>

                            <div class="relation_tab" id="relation">
                            </div>


                        </div>

                        <button class="add_service" id="" role="button" tabindex="0" hidden="hidden" type="button">Add anothrer Services </button>
                        <button class="book_btn" id="" role="button" tabindex="0" type="submit" data-toggle="modal" data-target="#exampleModalCenter${service.id}" onClick="bookService(event,${service.id})" >ADD SERVICE</button>
                        <!-- Modal -->
                        <div class="modal fade" id="exampleModalCenter${service.id}" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
                            <div class="modal-dialog modal-dialog-centered" role="document">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalLongTitle">Your Booking Details</h5>
                                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                            <span aria-hidden="true">&times;</span>
                                        </button>
                                    </div>
                                    <div class="modal-body">
                                        <div class="details_popup" id="popup${service.id}">
                                            <p id="p-service${service.id}">Service Name:</p>
                                            <p id="p-addon${service.id}" value="">Add-ons: </p>
                                            <p id="p-provider${service.id}" value="">Service Provider: </p>
                                            <p id="p-date${service.id}">Date:</p>
                                            <p id="p-slot${service.id}">Timeslot:</p>
                                            <p id="p-customer${service.id}">Booking For: </p>
                                            
                                            <p class="waring_date" id="p-warning${service.id}"><i class="fas fa-exclamation-triangle mr-1"></i>Please fill the remaining data</p>
                                            <button class="btn_clear" id="p-button${service.id}" role="button" tabindex="0" type="button" style="display:none">Book Now</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
            </div>
        </form>
        </div > `
    })
    document.querySelector("#accordionExample").innerHTML = htmlData
}
function serviceSelect(sid, cid) {
    service = document.getElementById(`check${sid}`)
    if (service.checked) {
        allBeauticians(sid)
        addonsData=``
        fetch(`v1/addons/category/${cid}`).then(res => res.json()).then(data => data.forEach(p=>addOnsPopulate(sid,p)))
    }
    else {
        addonsData=``
        addonDiv=document.getElementById(`add-ons-list${sid}`)
        addonDiv.innerHTML=addonsData
    }
}
function addOnsPopulate(sid, addon) {
    addonsData+= `<div class="col-lg-6">
        <div class="sub-box">
            <p>${addon.name}</p>
            <div class="add-sug">
                <h6>$ ${addon.cost}</h6>
                <div class="select-bx"><input type="checkbox" name="addon" value="${addon.name}" id="addons${sid}" onClick="addonSelect(event,${sid})"></div>
            </div>
        </div>
    </div>`
addonDiv=document.getElementById(`add-ons-list${sid}`)
addonDiv.innerHTML=addonsData
}
function addonSelect(event,sid){
    id=event.target.id
    value=event.target.value
    
    if (event.target.checked){
        addon=event.target
    }
    else{
        addon=``
    }

}
function allBeauticians(sid) {
    allCheckbox = document.getElementById(`all-beautician${sid}`)
    if (allCheckbox.checked) {
        beauticianData = ``
        provider_data = document.getElementById(`provider-data${sid}`)
        provider_data.innerHTML = beauticianData

    } else {

        beauticianData = ``
        fetch(`v1/services/${sid}/`).then(res => res.json()).then(data => data.beautician.forEach(p => {
            fetch(`v1/beauticians/${p}`).then(res => res.json()).then(data => beauticiansInfo(sid, data))
        }))

    }

}
function maleBeautician(sid){

    maleCheckbox = document.getElementById(`male-beautician${sid}`)
    if (maleCheckbox.checked) {
        beauticianData = ``
        provider_data = document.getElementById(`provider-data${sid}`)
        provider_data.innerHTML = beauticianData

    }else {

        beauticianData = ``
        fetch(`v1/services/${sid}/`).then(res => res.json()).then(data => data.beautician.forEach(p => {
            fetch(`v1/beauticians/${ p }`).then(res => res.json()).then(data => beauticiansInfo(sid, data))
        }))

    }
}

function femaleBeautician(sid){

    femaleCheckbox = document.getElementById(`female-beautician${sid}`)
    if (femaleCheckbox.checked) {
        beauticianData = ``
        provider_data = document.getElementById(`provider-data${ sid }`)
        provider_data.innerHTML = beauticianData

    }else {

        beauticianData = ``
        fetch(`v1/services/${sid}/`).then(res => res.json()).then(data => data.beautician.forEach(p => {
            fetch(`v1/beauticians/${p}`).then(res => res.json()).then(data => beauticiansInfo(sid, data))
        }))

    }
}

function beauticiansInfo(sid, data) {
    beauticianData +=
        `<div class= "col-lg-12 p-0" >
    <div class="pl-box"><input type="checkbox" class="checkoption1" value="${data.name}" name="beautician" id="beautician${data.id}" onChange="beauticianSelect(event,${sid})"> ${data.name} </div>
    </div>`
    provider_data = document.getElementById(`provider-data${sid}`)
    provider_data.innerHTML = beauticianData

}

function beauticianSelect(event,sid){
    id=event.target.id
    value=event.target.value
    
    if (event.target.checked){
        beautician=event.target
    }
    else{
        beautician=``
    }

}
function dateFetch(event, sid) {
    selectedDate = event.target.value
    fetch(`v1/services/${sid}/`).then(res => res.json()).then(data => data.timeslots.forEach(p => {
        fetch(`v1/timeslots/${p}/`).then(res => res.json()).then(data => slotPopulate(selectedDate, data,sid))
    }))
}

function slotPopulate(date, slot,sid) {
    
    if (date == slot.date) {
        if (slot.status == "available"){
            slotData += `<option value="${slot.time}_${slot.id}">${slot.time}</option> `
        }
        
    }
    else{
        slotData = ``
        slotData += `<option value="" ></option>`
    }
    s = document.getElementById(`slots${ sid }`)
    s.innerHTML = slotData
}
function test(event) {
    if (event.target.value == "family") {
        familyData = `< h5 > Add new family of freind</ >
        <h6>relationship to user</h6>

        <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
            <li class="nav-item">
                <a class="nav-link active" id="pills-one-tab" data-toggle="pill" href="#pills-one" role="tab" aria-controls="pills-one" aria-selected="true">Parent</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="pills-two-tab" data-toggle="pill" href="#pills-two" role="tab" aria-controls="pills-two" aria-selected="false">Spouse</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="pills-three-tab" data-toggle="pill" href="#pills-three" role="tab" aria-controls="pills-three" aria-selected="false">Child</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="pills-four-tab" data-toggle="pill" href="#pills-four" role="tab" aria-controls="pills-four" aria-selected="false">Sibling</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="pills-five-tab" data-toggle="pill" href="#pills-five" role="tab" aria-controls="pills-five" aria-selected="false">Pet</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="pills-six-tab" data-toggle="pill" href="#pills-six" role="tab" aria-controls="pills-six" aria-selected="false">Freind</a>
            </li>
        </ul>
        <div class="tab-content" id="pills-tabContent">
            <div class="tab-pane fade show active" id="pills-one" role="tabpanel" aria-labelledby="pills-one-tab">

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="email">Email</label>
                            <input type="email" id="email" name="email" placeholder="" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="phone">Phone Number</label>
                            <input type="tel" onkeypress="return /[0-9]/i.test(event.key)" placeholder="" name="phone" id="phone" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="fname">First Name</label>
                            <input onkeydown="return /[a-z]/i.test(event.key)" type="text" placeholder="" name="fname" id="fname" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="lname">Last Name</label>
                            <input onkeydown="return /[a-z]/i.test(event.key)" type="text" placeholder="" name="lname" id="lname" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="gender">Gender</label>
                            <div class="select-box">
                                <select class="formcontrol_F" name="gender" id="gender">
                                    <option value="user-icon">Select Gender (Optional)</option>
                                    <option value="">Male</option>
                                    <option value="">Female</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
            <div class="tab-pane fade" id="pills-two" role="tabpanel" aria-labelledby="pills-two-tab">

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="email">Email</label>
                            <input type="email" id="email" name="email" placeholder="" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="phone">Phone Number</label>
                            <input type="tel" onkeypress="return /[0-9]/i.test(event.key)" placeholder="" name="phone" id="phone" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="fname">First Name</label>
                            <input onkeydown="return /[a-z]/i.test(event.key)" type="text" placeholder="" name="fname" id="fname" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="lname">Last Name</label>
                            <input onkeydown="return /[a-z]/i.test(event.key)" type="text" placeholder="" name="lname" id="lname" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="gender">Gender</label>
                            <div class="select-box">
                                <select class="formcontrol_F" name="gender" id="gender">
                                    <option value="user-icon">Select Gender (Optional)</option>
                                    <option value="">Male</option>
                                    <option value="">Female</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
            <div class="tab-pane fade" id="pills-three" role="tabpanel" aria-labelledby="pills-three-tab">

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="fname">First Name</label>
                            <input onkeydown="return /[a-z]/i.test(event.key)" type="text" placeholder="" name="fname" id="fname" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="lname">Last Name</label>
                            <input onkeydown="return /[a-z]/i.test(event.key)" type="text" placeholder="" name="lname" id="lname" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="gender">Gender</label>
                            <div class="select-box">
                                <select class="formcontrol_F" name="gender" id="gender">
                                    <option value="user-icon">Select Gender (Optional)</option>
                                    <option value="">Male</option>
                                    <option value="">Female</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="bdate">Birth Date</label>
                            <div class="row">
                                <div class="col-lg-4">
                                    <div class="select-box">
                                        <select class="formcontrol_F" name="month" id="month">
                                            <option value="user-icon">Month</option>
                                            <option value="">Januvary</option>
                                            <option value="">Februvary</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="col-lg-4">
                                    <div class="select-box">
                                        <select class="formcontrol_F" name="month" id="month">
                                            <option value="user-icon">Day</option>
                                            <option value="">1</option>
                                            <option value="">2</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="col-lg-4">
                                    <div class="select-box">
                                        <select class="formcontrol_F" name="month" id="month">
                                            <option value="user-icon">Year</option>
                                            <option value="">2023</option>
                                            <option value="">2022</option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="email">Email (Optional)</label>
                            <input type="email" id="email" name="email" placeholder="" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="phone">Phone Number (Optional)</label>
                            <input type="tel" onkeypress="return /[0-9]/i.test(event.key)" placeholder="" name="phone" id="phone" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                </div>



            </div>
            <div class="tab-pane fade" id="pills-four" role="tabpanel" aria-labelledby="pills-four-tab">

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="email">Email</label>
                            <input type="email" id="email" name="email" placeholder="" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="phone">Phone Number</label>
                            <input type="tel" onkeypress="return /[0-9]/i.test(event.key)" placeholder="" name="phone" id="phone" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="fname">First Name</label>
                            <input onkeydown="return /[a-z]/i.test(event.key)" type="text" placeholder="" name="fname" id="fname" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="lname">Last Name</label>
                            <input onkeydown="return /[a-z]/i.test(event.key)" type="text" placeholder="" name="lname" id="lname" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="gender">Gender</label>
                            <div class="select-box">
                                <select class="formcontrol_F" name="gender" id="gender">
                                    <option value="user-icon">Select Gender (Optional)</option>
                                    <option value="">Male</option>
                                    <option value="">Female</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
            <div class="tab-pane fade" id="pills-five" role="tabpanel" aria-labelledby="pills-five-tab">

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="Category">Pet Category</label>
                            <div class="select-box">
                                <select class="formcontrol_F" name="Category" id="Category">
                                    <option value="user-icon">Select Category</option>
                                    <option value="">Dog</option>
                                    <option value="">Cat</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="gender">Gender</label>
                            <div class="select-box">
                                <select class="formcontrol_F" name="gender" id="gender">
                                    <option value="user-icon">Select Gender (Optional)</option>
                                    <option value="">Male</option>
                                    <option value="">Female</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="email">Email (Optional)</label>
                            <input type="email" id="email" name="email" placeholder="" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="phone">Phone Number (Optional)</label>
                            <input type="tel" onkeypress="return /[0-9]/i.test(event.key)" placeholder="" name="phone" id="phone" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="fname">Name</label>
                            <input onkeydown="return /[a-z]/i.test(event.key)" type="text" placeholder="" name="fname" id="fname" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                </div>

            </div>
            <div class="tab-pane fade" id="pills-six" role="tabpanel" aria-labelledby="pills-six-tab">

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="email">Email</label>
                            <input type="email" id="email" name="email" placeholder="" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="phone">Phone Number</label>
                            <input type="tel" onkeypress="return /[0-9]/i.test(event.key)" placeholder="" name="phone" id="phone" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="fname">First Name</label>
                            <input onkeydown="return /[a-z]/i.test(event.key)" type="text" placeholder="" name="fname" id="fname" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="lname">Last Name</label>
                            <input onkeydown="return /[a-z]/i.test(event.key)" type="text" placeholder="" name="lname" id="lname" required="required" autofocus="autofocus" autocapitalize="none" class="formcontrol_F">
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-lg-6">
                        <div class="form-groupfield">
                            <label for="gender">Gender</label>
                            <div class="select-box">
                                <select class="formcontrol_F" name="gender" id="gender">
                                    <option value="user-icon">Select Gender (Optional)</option>
                                    <option value="">Male</option>
                                    <option value="">Female</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <div class="row">
                <div class="col-lg-6">
                    <button class="btn_save" id="" role="button" tabindex="0" type="button">Save</button>
                </div>
                <div class="col-lg-6">
                    <button class="btn_clear" id="" role="button" tabindex="0" type="button">Clear</button>
                </div>
            </div>

        </div>`
    }
    else {
        familyData = ``
    }
    relation = document.getElementById('relation')
    relation.innerHTML = familyData


}
function bookService(e, sid) {
    let popup=document.getElementById(`popup${ sid }`)
    let messages = []
    let check=0
    let service = document.getElementById(`check${ sid }`)
    let allProvider=document.getElementById(`all-beautician${ sid }`)
    let maleProvider=document.getElementById(`male-beautician${ sid }`)
    let femaleProvider=document.getElementById(`female-beautician${ sid }`)
    let date=document.getElementById(`date${ sid }`)
    let slot=document.getElementById(`slots${ sid }`)
    let slotValue=slot.value
    let slotArray=slotValue.split("_")
    let selectedSlot=slotArray[0]
    let slotId=slotArray[1]
    let customer=document.getElementById(`booking${ sid }`)
    const form = document.getElementById('form')
    let servicePopup=document.getElementById(`p-service${ sid }`)
    let addonPopup=document.getElementById(`p-addon${ sid }`)
    let providerPopup=document.getElementById(`p-provider${ sid }`)
    let datePopup=document.getElementById(`p-date${ sid }`)
    let slotPopup=document.getElementById(`p-slot${ sid }`)
    let customerPopup=document.getElementById(`p-customer${ sid }`)
    let warningPopup=document.getElementById(`p-warning${ sid }`)
    let buttonPopup=document.getElementById(`p-button${ sid }`)
    
    if (service.checked == false || service.value == null) {
        servicePopup.innerHTML=`Service Name: `
    }
    else{
        servicePopup.innerHTML=`Service Name: ${ service.value } `
        check+=1
        e.preventDefault()
    }
    if (addon.checked == false || addon.value == null) {
        addonPopup.innerHTML=`Add-ons: Not selected`
        addonPopup.value=null
    }
    else{
        addonPopup.innerHTML=`Add-ons:  ${ addon.value }`
        addonPopup.value=`${addon.value}`
        e.preventDefault()
    }
    if (allProvider.checked == false || allProvider.value == null) {
        providerPopup.innerHTML=`Service Provider: `
    }
    else{
        providerPopup.innerHTML=`Service Provider: ${ allProvider.value }`
        providerPopup.value=`${ allProvider.value }`
        check+=1
        e.preventDefault()
    }
    if (maleProvider.checked == false || maleProvider.value == null) {
        // providerPopup.innerHTML=`< p > Service Provider: </ > `
    }
    else{
        providerPopup.innerHTML=`Service Provider: ${ maleProvider.value }`
        providerPopup.value=`${ maleProvider.value }`
        check+=1
        e.preventDefault()
    }
    if (femaleProvider.checked == false || femaleProvider.value == null) {
        // providerPopup.innerHTML=`< p > Service Provider: </ > `
    }
    else{
        providerPopup.innerHTML=`Service Provider: ${ femaleProvider.value }`
        providerPopup.value=`${ femaleProvider.value }`
        check+=1
        e.preventDefault()
    }
    if (date.value == null || date.value == '') {
        datePopup.innerHTML=`Date: `
    }
    else{
        datePopup.innerHTML=`Date: ${ date.value }`
        check+=1
        e.preventDefault()
    }
    if (selectedSlot == null || selectedSlot == '') {
        slotPopup.innerHTML=`Timeslot: `
    }
    else{
        
        slotPopup.innerHTML=`Timeslot: ${ selectedSlot }`
        check+=1
        e.preventDefault()
    }
    if (customer.value == null || customer.value == "") {
        customerPopup.innerHTML=`Booking For: `
    }
    else{
        customerPopup.innerHTML=`Booking For: ${ customer.value }`
        check+=1
        e.preventDefault()
    }
    if (beautician.checked == false || beautician.value == null) {
    }
    else{
        providerPopup.innerHTML=`Service Provider: ${ beautician.value }`
        providerPopup.value=`${ beautician.value }`
        check+=1
        e.preventDefault()
    }

    if (check == 5){
        // buttonPopup.style.display="block"
        if (userStatus){
            fetch('v1/cart/add',{
                method:"POST",
                headers: {'Content-type': 'application/json','X-CSRFToken': csrf_token.value},
                body:JSON.stringify({
                    'service': service.value,
                    'sid':sid,
                    'slot_id':slotId,
                    'date':date.value,
                    'addon':addonPopup.value,
                    'beautician': providerPopup.value
                })
                
            }).then(res=> res.json()).then(data => console.log(data))
            warningPopup.innerHTML=`<i class="fas fa-check mr-1" ></i> Hooray! Selected Service added to service cart successfully!`
        }
        else{
            warningPopup.innerHTML=`<i class="fas fa-exclamation-triangle mr-1"></i> Sorry! You must log -in to add the service`
        }
    }
    else{
        
    }

}