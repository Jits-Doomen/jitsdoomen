const menuBtn = document.getElementById("menuBtn");
const closeBtn = document.getElementById("closeBtn");
const sidebar = document.getElementById("sidebar");

if(menuBtn){
    menuBtn.addEventListener("click", () => {
        sidebar.classList.add("active");
    });
}

if(closeBtn){
    closeBtn.addEventListener("click", () => {
        sidebar.classList.remove("active");
    });
}