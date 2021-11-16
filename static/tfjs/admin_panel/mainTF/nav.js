const navLinks = document.querySelectorAll('.nav-link')
navLinks.forEach(link => {
  if (link.href == document.URL) {
    link.classList.add("active")
  } else {
    link.classList.remove("active")
  }
})

const dropdownContainers = document.querySelectorAll(".dropdown-container");

const dropdown = document.querySelectorAll(".dropdown-btn");
for (let i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function () {
    var dropdownContent = this.nextElementSibling;
    dropdownContainers.forEach(item=>{
      item.classList.remove("show-dropdown-container")
      if (item.classList.contains("active-container") && item != dropdownContent) {
        item.classList.remove("active-container");
        item.previousElementSibling.classList.remove("clicked")
      }
    })
    if (dropdownContent.classList.contains("active-container")) {
      dropdownContent.classList.remove("show-dropdown-container");
      dropdownContent.classList.remove("active-container");
      dropdown[i].classList.remove("clicked");
    } else {
      dropdownContent.classList.add("show-dropdown-container");
      dropdownContent.classList.add("active-container");
      dropdown[i].classList.add("clicked");
    }
  });
}
const mainSection = document.querySelector("main")
mainSection.addEventListener("click", ()=>{
  dropdownContainers.forEach(item=>{
    item.classList.remove("show-dropdown-container")
    item.classList.remove("active-container")
  })
  dropdown.forEach(item=>{
    item.classList.remove("clicked");
  })
})


const deleteBtn = document.querySelectorAll(".trash, .dlt")

deleteBtn.forEach(btn => {
    btn.addEventListener("click", () => {
        btn.parentElement.parentElement.style.display = "none"
    })
})


const hamburger = document.querySelector(".hamburger")
const sideBarClose = document.querySelector(".sideBarClose")
const sideBarText = document.querySelectorAll(".nav-text")
const aside = document.querySelector(".aside-container")
const nav = document.querySelector("nav")
const main = document.querySelector("main")
const footer = document.querySelector("footer")

hamburger.addEventListener("click", () => {
  aside.classList.toggle("show-aside")
  aside.classList.contains("shrink-container") && aside.classList.remove("shrink-container")
})

sideBarClose.addEventListener("click", () => {
  aside.classList.remove("show-aside")
})

const shrinkBtn = document.querySelector(".shrink-btn")
shrinkBtn.addEventListener("click", () => {
  aside.classList.toggle("shrink-container")
  nav.classList.toggle("nav-expand")
  main.classList.toggle("main-expand")
  footer.classList.toggle("footer-expand")
  sideBarText.forEach(text=>{
    text.classList.toggle("d-none")
  })

})