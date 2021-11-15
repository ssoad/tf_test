const links = document.querySelectorAll('.nav-link')
links.forEach(link => {
    if (link.href == document.URL) {
        link.classList.add("active")
        if (link.classList.contains("dropdown-item")) {
            console.log("clicked");
            link.parentElement.parentElement.classList.add("show-dropdown-container");
        }

    } else {
        link.classList.remove("active")
    }
})


const dropdown = document.querySelectorAll(".dropdown-btn");
for (let i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function () {
        var dropdownContent = this.nextElementSibling;
        console.log(dropdownContent);
        if (dropdownContent.classList.contains("show-dropdown-container")) {
            dropdownContent.classList.remove("show-dropdown-container");
        } else {
            dropdownContent.classList.add("show-dropdown-container");
        }
    });
}

const deleteBtn = document.querySelectorAll(".trash, .dlt")

deleteBtn.forEach(btn => {
    btn.addEventListener("click", () => {
        btn.parentElement.parentElement.style.display = "none"
    })
})


const hamburger = document.querySelector(".hamburger")
const aside = document.querySelector(".aside-container")

hamburger.addEventListener("click", () => {
    aside.classList.toggle("show-aside")
})