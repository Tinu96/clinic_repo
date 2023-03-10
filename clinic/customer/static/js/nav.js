const activePage=window.location.pathname;
const navLinks=document.querySelectorAll('nav a').forEach(link=>{
    if (link.href.includes(`${activePage}`)){
        if(activePage=="/"){
            document.getElementById("home").classList.add("active")
        }
        
        else{
            link.classList.add("active")
            if(document.getElementById("account")){
                document.getElementById("account").classList.remove("active")
            }
            
        }
    }
})