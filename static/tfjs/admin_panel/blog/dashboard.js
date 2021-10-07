$(document).ready(function () {
    $("#blogList").DataTable({
        scrollX: true,
        scrollCollapse: true,
        paging: false,
        searching: true,
        info: false,
        sorting: false,
        oLanguage: {
            sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
    });
    $(".js-example-tokenizer").select2({
        tags: true,
        tokenSeparators: [',', ' ']
    })
});

const baseUrl = "http://127.0.0.1:8000/"
const blogCategory = document.getElementById("category")
const blogSubCategory = document.getElementById("subCategory")
const filterOption = document.getElementById("filterOption")
window.addEventListener("load", () => {
    fetch(`${baseUrl}api/blogs/category/`)
        .then(response => response.json())
        .then(result => {
            result.map((item) => {
                const newOption = document.createElement("option");
                newOption.setAttribute("value", item.id)
                newOption.setAttribute("has_subcategory", item.has_subcategory)
                newOption.text = item.category
                // console.log(newOption);
                blogCategory.appendChild(newOption)
            })
        })
})
blogCategory.addEventListener("change", () => {
    const has_subcategory = blogCategory.options[blogCategory.selectedIndex].getAttribute("has_subcategory")
    blogSubCategory.innerHTML = `<option value="" disabled selected>Select a Sub category</option>`
    filterOption.previousElementSibling.classList.add("d-none")
    filterOption.classList.add("d-none")
    if (has_subcategory === "true") {
        blogSubCategory.previousElementSibling.classList.remove("d-none")
        blogSubCategory.classList.remove("d-none")
    } else if (has_subcategory === "false") {
        blogSubCategory.previousElementSibling.classList.add("d-none")
        blogSubCategory.classList.add("d-none")
    }
    fetch(`${baseUrl}api/blogs/category/${blogCategory.value}`)
        .then(response => response.json())
        .then(result => {
            result.map((item) => {
                const newOption = document.createElement("option");
                newOption.setAttribute("value", item.id)
                newOption.setAttribute("has_filter", item.has_filter)
                newOption.text = item.sub_category
                blogSubCategory.appendChild(newOption)
            })
        })
})
blogSubCategory.addEventListener("change", () => {
    const has_filter = blogSubCategory.options[blogSubCategory.selectedIndex].getAttribute("has_filter")
    filterOption.innerHTML = `<option value="" disabled selected>Select a Sub category</option>`
    console.log(`${baseUrl}api/blogs/category/${blogCategory.value}/${blogSubCategory.value}`);
    if (has_filter === "true") {
        filterOption.previousElementSibling.classList.remove("d-none")
        filterOption.classList.remove("d-none")
        filterOption.setAttribute("required", true)
    } else if (has_filter === "false") {
        filterOption.previousElementSibling.classList.add("d-none")
        filterOption.classList.add("d-none")
        filterOption.removeAttribute("required")
    }
    fetch(`${baseUrl}api/blogs/category/${blogCategory.value}/${blogSubCategory.value}`)
        .then(response => response.json())
        .then(result => {
            // console.log(result);
            result.map((item) => {
                // console.log(item.has_subcategory);
                const newOption = document.createElement("option");
                newOption.setAttribute("value", item.id)
                newOption.text = item.filter_name
                filterOption.appendChild(newOption)
            })
        })
})
