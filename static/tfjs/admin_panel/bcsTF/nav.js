const navLinks = document.querySelectorAll('.nav-link')
navLinks.forEach(link => {
  if (link.href == document.URL) {
    link.classList.add("active")
    if (link.classList.contains("dropdown-item")) {
      link.parentElement.parentElement.classList.add("show-dropdown-container");
    }

  } else {
    link.classList.remove("active")
    // link.parentElement.parentElement.classList.remove("show-dropdown-container");
  }
})


const dropdown = document.querySelectorAll(".dropdown-btn");
for (let i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function () {
    var dropdownContent = this.nextElementSibling;
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
const sideBarClose = document.querySelector(".sideBarClose")
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
})
// aside.addEventListener("mouseover", () => {
//   if (aside.classList.contains("mouseover"))
//     aside.classList.remove("shrink-container")
// })

// aside.addEventListener("mouseout", () => {
//   if (aside.classList.contains("mouseover"))
//     aside.classList.add("shrink-container")
// })


// if(){
//   console.log("true");
//   aside.addEventListener("mouseover",()=>{
//     if(aside.classList.contains("shrink-container"))
//       aside.classList.remove("shrink-container")
//   })
// }