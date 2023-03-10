fetch(`test`).then(res=>res.json()).then(data=>populateValue(data))

function populateValue(values){

    let service=values.services
    let htmlData=` `;
    service.forEach(s=>
    htmlData+=`
    <div class="col-lg-4 col-md-6 col-sm-6 pb-1">
    <div class="product-item bg-light mb-4">
        <div class="product-img position-relative overflow-hidden">
            <img class="img-fluid w-100" style="width:100%;height:230px;" src="/media/${s.image}" alt="">
            <div class="product-action">
                <a class="btn btn-outline-dark btn-square" href="/wishlist/${s.id}"><i class="far fa-heart"></i></a>
                <a class="btn btn-outline-dark btn-square" href="/book/${s.id}"><i class="fa fa-calendar"></i></a>
            </div>
        </div>
        <div class="text-center py-4">
            <a class="h6 text-decoration-none text-truncate" href="/book/${s.id}">${s.name}</a>
            <div class="d-flex align-items-center justify-content-center mt-2">
                <h5>$${s.cost}</h5><h6 class="text-muted ml-2"><del>$${s.cost}</del></h6>
            </div>
            <div class="d-flex align-items-center justify-content-center mb-1">
                <small class="fa fa-star text-primary mr-1"></small>
                <small class="fa fa-star text-primary mr-1"></small>
                <small class="fa fa-star text-primary mr-1"></small>
                <small class="fa fa-star text-primary mr-1"></small>
                <small class="fa fa-star text-primary mr-1"></small>
                <small>(${s.rating_count})</small>
            </div>
        </div>
    </div>
</div>
    `
        
    )
    document.querySelector("#service-list").innerHTML=htmlData
    
    
}
    let htmlData=` `;
    var catCheck=[]
    var catId=0
    let allData=` `

    function customCheckbox(event){
    catId=event.target.name 
    
    check=catCheck.find(t=>t==catId)
    
    if(check){
        service=document.getElementById(catId)
        if (service){ 
        service.remove()}
        doc=document.querySelector("#service-list")
        htmlData=doc.innerHTML
        const indexValue=catCheck.indexOf(catId)
        if (indexValue>-1){
        catCheck.splice(indexValue,1)  }
        
    }
    else{
        catCheck.push(catId)  
        fetch(`/category/${catId}`).then(res=>res.json()).then(data=>populateCategoryFilter(data))
        function populateCategoryFilter(values){
        let service=values.services
        service.forEach(s=>{
        htmlData+=`
    <div class="col-lg-4 col-md-6 col-sm-6 pb-1" id="${s.category_id}">
    <div class="product-item bg-light mb-4">
        <div class="product-img position-relative overflow-hidden">
            <img class="img-fluid w-100" style="width:100%;height:230px;" src="/media/${s.image}" alt="">
            <div class="product-action">
                <a class="btn btn-outline-dark btn-square" href="/wishlist/${s.id}"><i class="far fa-heart"></i></a>
                <a class="btn btn-outline-dark btn-square" href="/book/${s.id}"><i class="fa fa-calendar"></i></a>
            </div>
        </div>
        <div class="text-center py-4">
            <a class="h6 text-decoration-none text-truncate" href="/book/${s.id}">${s.name}</a>
            <div class="d-flex align-items-center justify-content-center mt-2">
                <h5>$${s.cost}</h5><h6 class="text-muted ml-2"><del>$${s.cost}</del></h6>
            </div>
            <div class="d-flex align-items-center justify-content-center mb-1">
                <small class="fa fa-star text-primary mr-1"></small>
                <small class="fa fa-star text-primary mr-1"></small>
                <small class="fa fa-star text-primary mr-1"></small>
                <small class="fa fa-star text-primary mr-1"></small>
                <small class="fa fa-star text-primary mr-1"></small>
                <small>(${s.rating_count})</small>
            </div>
        </div>
    </div>
</div>
    `})
    document.querySelector("#service-list").innerHTML=htmlData
    p=document.querySelector("#all")
    p.checked=false
}
    
       }
    }

function allService(){
    window.location.replace("/shop")
    // document.querySelector(".cat").checked=false
}

function categorySelect(event){
    id=event.target.name
}