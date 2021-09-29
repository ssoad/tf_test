const links = document.querySelectorAll('.nav-link')
links.forEach(link => {
  if (link.href == document.URL) {
    link.classList.add("active")
    if (link.classList.contains("dropdown-item"))
      link.parentElement.parentElement.style.display = "block"

  } else {
    link.classList.remove("active")
  }
})


const dropdown = document.querySelectorAll(".dropdown-btn");
for (let i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function () {
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}


$(document).ready(function () {
  // console.log('data-table');
  $(window).scroll(function () {
    if ($(window).scrollTop() + $(window).height() > $(document).height() - 5) {
      console.log("came to right place");
      $(".aside-container").css("bottom", $(".footer").outerHeight()+2)
      $(".aside-container").addClass("small-aside")
      $(".footer").removeClass("footer-shrink")
    } else {
      $(".aside-container").css("bottom", "0")
      $(".aside-container").removeClass("small-aside")
      $(".footer").addClass("footer-shrink")
    }
  });
});

const deleteBtn = document.querySelectorAll(".trash, .dlt")

deleteBtn.forEach(btn=>{
    btn.addEventListener("click",()=>{
        btn.parentElement.parentElement.style.display = "none"
    })
})
